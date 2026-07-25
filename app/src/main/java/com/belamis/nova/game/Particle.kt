package com.belamis.nova.game

/** Particule légère pour les effets de fusion (étincelles cosmiques). */
class Particle {
    var x = 0f
    var y = 0f
    var vx = 0f
    var vy = 0f
    var life = 0f
    var maxLife = 1f
    var size = 0f
    var color = 0
    var active = false

    fun spawn(x: Float, y: Float, vx: Float, vy: Float, life: Float, size: Float, color: Int) {
        this.x = x; this.y = y
        this.vx = vx; this.vy = vy
        this.life = life; this.maxLife = life
        this.size = size; this.color = color
        this.active = true
    }

    fun update(dt: Float) {
        if (!active) return
        life -= dt
        if (life <= 0f) { active = false; return }
        // Légère gravité + traînée pour un mouvement organique.
        vy += 900f * dt
        vx *= 0.96f
        vy *= 0.96f
        x += vx * dt
        y += vy * dt
    }

    /** Alpha normalisé restant (1 au début, 0 à la fin). */
    val alpha: Float get() = (life / maxLife).coerceIn(0f, 1f)
}

/** Pool de particules pour éviter les allocations pendant le rendu. */
class ParticleSystem(capacity: Int = 240) {
    private val pool = Array(capacity) { Particle() }
    private var cursor = 0

    fun emitBurst(x: Float, y: Float, color: Int, count: Int, spread: Float) {
        var i = 0
        while (i < count) {
            val p = pool[cursor]
            cursor = (cursor + 1) % pool.size
            // Direction pseudo-aléatoire déterministe basée sur le curseur/temps.
            val a = (i.toFloat() / count) * (Math.PI.toFloat() * 2f) + (cursor * 0.13f)
            val sp = spread * (0.35f + ((cursor * 37 % 100) / 100f) * 0.9f)
            p.spawn(
                x, y,
                Math.cos(a.toDouble()).toFloat() * sp,
                Math.sin(a.toDouble()).toFloat() * sp - sp * 0.3f,
                0.45f + ((cursor * 13 % 100) / 100f) * 0.5f,
                (2.5f + (cursor % 5)),
                color
            )
            i++
        }
    }

    fun update(dt: Float) {
        for (p in pool) p.update(dt)
    }

    fun forEachActive(action: (Particle) -> Unit) {
        for (p in pool) if (p.active) action(p)
    }
}
