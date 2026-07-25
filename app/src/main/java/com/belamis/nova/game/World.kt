package com.belamis.nova.game

import kotlin.math.sqrt
import kotlin.random.Random

/**
 * Cœur de la simulation : chute, collisions et fusion des corps célestes.
 *
 * Physique basée position (Position Based Dynamics) : prédiction puis
 * relaxation itérative des contraintes. Cela donne un empilement stable
 * sans réglages de restitution délicats, idéal pour un jeu de fusion.
 */
class World {

    enum class State { PLAYING, GAME_OVER }

    // --- Géométrie du monde (pixels) ---
    var worldW = 0f; private set
    var worldH = 0f; private set
    var wallLeft = 0f; private set
    var wallRight = 0f; private set
    var floorY = 0f; private set
    var spawnY = 0f; private set
    var dangerY = 0f; private set
    var hudH = 0f; private set

    // --- Contenu ---
    val bodies = ArrayList<Body>(128)
    val particles = ParticleSystem()

    // --- État de jeu ---
    var state = State.PLAYING; private set
    var score = 0; private set
    var best = 0
    var highestTier = 0; private set

    // --- Corps courant (en attente de lâcher, non simulé) ---
    var currentTier = 0; private set
    var currentX = 0f; private set
    var nextTier = 0; private set
    private var dropCooldown = 0f
    var canDrop = false; private set

    // --- Effets renvoyés au rendu ---
    var shake = 0f; private set
    var flash = 0f; private set
    var lastMergeTier = -1; private set
    var lastMergeX = 0f; private set
    var lastMergeY = 0f; private set

    private var overflow = 0f
    private val rnd = Random(System.nanoTime())

    // Réglages
    private val subStep = 1f / 120f
    private val solverIters = 6
    private val damping = 0.999f
    private var gravity = 2600f

    fun configure(w: Int, h: Int) {
        worldW = w.toFloat()
        worldH = h.toFloat()
        wallLeft = 0f
        wallRight = worldW
        floorY = worldH
        hudH = worldH * 0.13f
        gravity = worldW * 2.6f
        val maxDrop = Tiers.radiusPx(MAX_DROP_TIER, worldW)
        spawnY = hudH + maxDrop + worldW * 0.02f
        dangerY = spawnY + maxDrop * 0.5f
        if (state == State.PLAYING && bodies.isEmpty() && currentX == 0f) {
            reset()
        } else {
            currentX = currentX.coerceIn(wallLeft, wallRight)
        }
    }

    fun reset() {
        bodies.clear()
        score = 0
        highestTier = 0
        overflow = 0f
        shake = 0f
        flash = 0f
        state = State.PLAYING
        currentX = worldW / 2f
        currentTier = randomDropTier()
        nextTier = randomDropTier()
        dropCooldown = 0f
        canDrop = true
    }

    private fun randomDropTier(): Int = rnd.nextInt(MAX_DROP_TIER + 1)

    fun onPointerMove(x: Float) {
        val r = Tiers.radiusPx(currentTier, worldW)
        currentX = x.coerceIn(wallLeft + r, wallRight - r)
    }

    /** Lâche le corps courant. Retourne true si le lâcher a eu lieu. */
    fun onDrop(): Boolean {
        if (state != State.PLAYING || !canDrop) return false
        val r = Tiers.radiusPx(currentTier, worldW)
        val b = Body(currentX.coerceIn(wallLeft + r, wallRight - r), spawnY, currentTier, r)
        b.vy = 40f
        bodies.add(b)
        // Prépare le prochain corps après un court délai.
        currentTier = nextTier
        nextTier = randomDropTier()
        canDrop = false
        dropCooldown = DROP_COOLDOWN
        return true
    }

    fun update(dtRaw: Float) {
        val dt = dtRaw.coerceIn(0f, 0.033f)

        // Décroissance des effets visuels.
        if (shake > 0f) shake = (shake - dt * 6f).coerceAtLeast(0f)
        if (flash > 0f) flash = (flash - dt * 3f).coerceAtLeast(0f)
        particles.update(dt)

        // Animations d'apparition des corps.
        for (b in bodies) {
            if (b.spawnScale < 1f) b.spawnScale = (b.spawnScale + dt * 6f).coerceAtMost(1f)
            if (b.pop > 0f) b.pop = (b.pop - dt * 4f).coerceAtLeast(0f)
        }

        if (state == State.PLAYING) {
            if (!canDrop) {
                dropCooldown -= dt
                if (dropCooldown <= 0f) canDrop = true
            }
        }

        // Intégration physique par sous-pas fixes (stabilité).
        var acc = dt
        while (acc > 0f) {
            val h = if (acc > subStep) subStep else acc
            simulate(h)
            acc -= h
        }

        if (state == State.PLAYING) checkGameOver(dt)
    }

    private fun simulate(h: Float) {
        val n = bodies.size
        if (n == 0) return

        // 1) Prédiction (Euler semi-implicite).
        for (b in bodies) {
            b.vy += gravity * h
            b.vx *= damping
            b.vy *= damping
            b.prevX = b.x
            b.prevY = b.y
            b.x += b.vx * h
            b.y += b.vy * h
        }

        // 2) Relaxation des contraintes.
        var iter = 0
        while (iter < solverIters) {
            // Murs et sol.
            for (b in bodies) {
                if (b.x - b.radius < wallLeft) b.x = wallLeft + b.radius
                if (b.x + b.radius > wallRight) b.x = wallRight - b.radius
                if (b.y + b.radius > floorY) b.y = floorY - b.radius
            }
            // Collisions entre paires.
            var i = 0
            while (i < n) {
                val a = bodies[i]
                var j = i + 1
                while (j < n) {
                    val c = bodies[j]
                    val dx = c.x - a.x
                    val dy = c.y - a.y
                    val minDist = a.radius + c.radius
                    var d2 = dx * dx + dy * dy
                    if (d2 < minDist * minDist && d2 > 0.0001f) {
                        val d = sqrt(d2)
                        val overlap = minDist - d
                        val nx = dx / d
                        val ny = dy / d
                        // Répartition inverse à la masse.
                        val wA = 1f / a.mass
                        val wB = 1f / c.mass
                        val inv = 1f / (wA + wB)
                        val corr = overlap * inv
                        a.x -= nx * corr * wA
                        a.y -= ny * corr * wA
                        c.x += nx * corr * wB
                        c.y += ny * corr * wB
                    }
                    j++
                }
                i++
            }
            iter++
        }

        // 3) Dérivation des vitesses depuis le déplacement (PBD),
        //    avec bornage pour absorber les corrections trop brutales.
        val invH = 1f / h
        val maxV = worldW * 8f
        for (b in bodies) {
            var nvx = (b.x - b.prevX) * invH
            var nvy = (b.y - b.prevY) * invH
            if (nvx > maxV) nvx = maxV else if (nvx < -maxV) nvx = -maxV
            if (nvy > maxV) nvy = maxV else if (nvy < -maxV) nvy = -maxV
            b.vx = nvx
            b.vy = nvy
            if (b.speedSq() > 25f) b.landed = true
            else if (b.y + b.radius >= floorY - 0.5f) b.landed = true
        }

        // 4) Fusion des corps de même palier.
        mergePass()
    }

    private fun mergePass() {
        val n = bodies.size
        val consumed = BooleanArray(n)
        var toAdd: ArrayList<Body>? = null

        var i = 0
        while (i < n) {
            if (consumed[i]) { i++; continue }
            val a = bodies[i]
            if (a.tier >= Tiers.max) { i++; continue }
            var j = i + 1
            while (j < n) {
                if (!consumed[j]) {
                    val c = bodies[j]
                    if (c.tier == a.tier) {
                        val dx = c.x - a.x
                        val dy = c.y - a.y
                        val touch = (a.radius + c.radius) * 0.90f
                        if (dx * dx + dy * dy < touch * touch) {
                            consumed[i] = true
                            consumed[j] = true
                            a.alive = false
                            c.alive = false
                            val nt = a.tier + 1
                            val nx = (a.x + c.x) * 0.5f
                            val ny = (a.y + c.y) * 0.5f
                            val nb = Body(nx, ny, nt, Tiers.radiusPx(nt, worldW))
                            nb.vx = (a.vx + c.vx) * 0.5f
                            nb.vy = (a.vy + c.vy) * 0.5f - 60f
                            nb.spawnScale = 0.35f
                            nb.pop = 1f
                            nb.landed = true
                            (toAdd ?: ArrayList<Body>().also { toAdd = it }).add(nb)

                            score += Tiers.scoreForTier(nt)
                            if (score > best) best = score
                            if (nt > highestTier) highestTier = nt
                            onMergeFx(nx, ny, nt)
                            break
                        }
                    }
                }
                j++
            }
            i++
        }

        if (toAdd != null) {
            // Retire les corps consommés.
            var k = bodies.size - 1
            while (k >= 0) {
                if (!bodies[k].alive) bodies.removeAt(k)
                k--
            }
            bodies.addAll(toAdd!!)
        }
    }

    private fun onMergeFx(x: Float, y: Float, tier: Int) {
        val t = Tiers.list[tier]
        val count = 10 + tier * 3
        val spread = 140f + tier * 40f
        particles.emitBurst(x, y, t.core, count, spread)
        particles.emitBurst(x, y, t.edge, count / 2, spread * 0.7f)
        shake = (0.25f + tier * 0.06f).coerceAtMost(1f)
        flash = (0.15f + tier * 0.05f).coerceAtMost(0.6f)
        lastMergeTier = tier
        lastMergeX = x
        lastMergeY = y
    }

    private fun checkGameOver(dt: Float) {
        var over = false
        for (b in bodies) {
            if (b.landed && b.speedSq() < 3600f && b.y - b.radius < dangerY) {
                over = true
                break
            }
        }
        if (over) {
            overflow += dt
            if (overflow > OVERFLOW_LIMIT) {
                state = State.GAME_OVER
                if (score > best) best = score
            }
        } else {
            overflow = (overflow - dt * 2f).coerceAtLeast(0f)
        }
    }

    /** Intensité 0..1 du danger (pour faire pulser la ligne). */
    val dangerLevel: Float get() = (overflow / OVERFLOW_LIMIT).coerceIn(0f, 1f)

    companion object {
        const val MAX_DROP_TIER = 4
        const val DROP_COOLDOWN = 0.32f
        const val OVERFLOW_LIMIT = 0.9f
    }
}
