package com.belamis.nova.render

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.DashPathEffect
import android.graphics.Paint
import android.graphics.RadialGradient
import android.graphics.Shader
import android.graphics.SweepGradient
import android.graphics.Typeface
import com.belamis.nova.game.Tiers
import com.belamis.nova.game.World
import kotlin.math.sin

/**
 * Rendu 2D moderne et lumineux du monde de jeu, entièrement sur Canvas :
 * halos radiaux, orbes en dégradé, reflets, trou noir à disque d'accrétion
 * animé, particules additives et interface néon.
 */
class Renderer {

    private val stars = StarField()

    private val glowPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val bodyPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val rimPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { style = Paint.Style.STROKE }
    private val highlightPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val ringPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { style = Paint.Style.STROKE }
    private val particlePaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val linePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { style = Paint.Style.STROKE }
    private val overlayPaint = Paint()
    private val panelPaint = Paint(Paint.ANTI_ALIAS_FLAG)

    private val titlePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        typeface = Typeface.create("sans-serif-black", Typeface.BOLD)
        textAlign = Paint.Align.CENTER
        color = Color.WHITE
    }
    private val scorePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        typeface = Typeface.create("sans-serif-black", Typeface.BOLD)
        textAlign = Paint.Align.CENTER
        color = Color.WHITE
    }
    private val labelPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        typeface = Typeface.create("sans-serif-medium", Typeface.BOLD)
        color = 0xCCBFC7E0.toInt()
    }

    fun resize(w: Int, h: Int) {
        stars.resize(w.toFloat(), h.toFloat())
    }

    fun draw(canvas: Canvas, world: World, time: Float) {
        val w = world.worldW
        val h = world.worldH
        if (w == 0f) return

        stars.draw(canvas, time)

        // Secousse d'écran sur les grosses fusions.
        val saved = canvas.save()
        if (world.shake > 0f) {
            val s = world.shake
            val dx = sin(time * 90f) * s * w * 0.012f
            val dy = sin(time * 77f + 1.3f) * s * h * 0.010f
            canvas.translate(dx, dy)
        }

        drawContainer(canvas, world)
        drawDangerLine(canvas, world, time)

        // Corps physiques.
        for (b in world.bodies) {
            drawOrb(canvas, b.x, b.y, b.radius, b.tier, b.spawnScale, b.pop, time)
        }

        drawParticles(canvas, world)
        drawCurrent(canvas, world, time)

        canvas.restoreToCount(saved)

        drawHud(canvas, world)

        // Flash lumineux global.
        if (world.flash > 0f) {
            overlayPaint.color = Color.argb((world.flash * 90).toInt().coerceIn(0, 90), 255, 255, 255)
            canvas.drawRect(0f, 0f, w, h, overlayPaint)
        }

        if (world.state == World.State.GAME_OVER) drawGameOver(canvas, world)
    }

    private fun drawContainer(canvas: Canvas, world: World) {
        val w = world.worldW
        // Cadre latéral et sol lumineux subtils.
        linePaint.pathEffect = null
        linePaint.strokeWidth = w * 0.010f
        linePaint.color = 0x33B14CFF.toInt()
        canvas.drawLine(1f, world.hudH, 1f, world.floorY, linePaint)
        canvas.drawLine(w - 1f, world.hudH, w - 1f, world.floorY, linePaint)
        linePaint.color = 0x5590E0FF.toInt()
        canvas.drawLine(0f, world.floorY - 1f, w, world.floorY - 1f, linePaint)
    }

    private fun drawDangerLine(canvas: Canvas, world: World, time: Float) {
        val w = world.worldW
        val danger = world.dangerLevel
        val pulse = 0.4f + 0.6f * (0.5f + 0.5f * sin(time * (4f + danger * 8f)))
        val base = 0x40FF3B6E.toInt()
        val a = ((0.25f + danger * 0.6f) * pulse * 255).toInt().coerceIn(0, 255)
        linePaint.color = Color.argb(a, Color.red(base), Color.green(base), Color.blue(base))
        linePaint.strokeWidth = w * 0.006f
        linePaint.pathEffect = DashPathEffect(floatArrayOf(w * 0.03f, w * 0.02f), time * 40f % (w * 0.05f))
        canvas.drawLine(0f, world.dangerY, w, world.dangerY, linePaint)
        linePaint.pathEffect = null
    }

    private fun drawOrb(
        canvas: Canvas, cx: Float, cy: Float, r: Float,
        tier: Int, scale: Float, pop: Float, time: Float
    ) {
        val t = Tiers.list[tier]
        val er = r * scale * (1f + pop * 0.14f)
        if (er < 0.5f) return

        // Halo.
        glowPaint.shader = RadialGradient(
            cx, cy, er * 1.95f,
            intArrayOf(t.glow, Tiers.withAlpha(t.glow, 0)),
            floatArrayOf(0f, 1f), Shader.TileMode.CLAMP
        )
        canvas.drawCircle(cx, cy, er * 1.95f, glowPaint)

        if (tier == Tiers.max) {
            drawBlackHole(canvas, cx, cy, er, t.core, t.edge, t.glow, time)
            return
        }

        // Corps : dégradé décentré pour un effet volumétrique.
        val lx = cx - er * 0.32f
        val ly = cy - er * 0.32f
        bodyPaint.shader = RadialGradient(
            lx, ly, er * 1.35f,
            intArrayOf(t.core, t.edge, darken(t.edge, 0.72f)),
            floatArrayOf(0f, 0.65f, 1f), Shader.TileMode.CLAMP
        )
        canvas.drawCircle(cx, cy, er, bodyPaint)

        // Liseré lumineux.
        rimPaint.shader = null
        rimPaint.color = Tiers.withAlpha(t.core, 140)
        rimPaint.strokeWidth = er * 0.05f
        canvas.drawCircle(cx, cy, er * 0.985f, rimPaint)

        // Reflet spéculaire.
        highlightPaint.shader = RadialGradient(
            cx - er * 0.38f, cy - er * 0.42f, er * 0.55f,
            intArrayOf(0x99FFFFFF.toInt(), 0x00FFFFFF), floatArrayOf(0f, 1f), Shader.TileMode.CLAMP
        )
        canvas.drawCircle(cx - er * 0.38f, cy - er * 0.42f, er * 0.55f, highlightPaint)
    }

    private fun drawBlackHole(
        canvas: Canvas, cx: Float, cy: Float, er: Float,
        core: Int, edge: Int, glow: Int, time: Float
    ) {
        // Disque d'accrétion tournant.
        val saved = canvas.save()
        canvas.rotate(time * 60f % 360f, cx, cy)
        ringPaint.shader = SweepGradient(
            cx, cy,
            intArrayOf(edge, 0xFFFFFFFF.toInt(), 0xFFFF7AD9.toInt(), edge, edge),
            floatArrayOf(0f, 0.25f, 0.5f, 0.8f, 1f)
        )
        ringPaint.strokeWidth = er * 0.24f
        canvas.drawCircle(cx, cy, er * 0.86f, ringPaint)
        canvas.restoreToCount(saved)

        // Cœur sombre (horizon des événements).
        bodyPaint.shader = RadialGradient(
            cx, cy, er * 0.8f,
            intArrayOf(0xFF05030C.toInt(), 0xFF120A26.toInt(), core),
            floatArrayOf(0f, 0.7f, 1f), Shader.TileMode.CLAMP
        )
        canvas.drawCircle(cx, cy, er * 0.7f, bodyPaint)

        rimPaint.shader = null
        rimPaint.color = Tiers.withAlpha(0xFFB14CFF.toInt(), 200)
        rimPaint.strokeWidth = er * 0.045f
        canvas.drawCircle(cx, cy, er * 0.7f, rimPaint)
    }

    private fun drawParticles(canvas: Canvas, world: World) {
        world.particles.forEachActive { p ->
            val a = (p.alpha * 255).toInt().coerceIn(0, 255)
            particlePaint.color = Tiers.withAlpha(p.color, a)
            canvas.drawCircle(p.x, p.y, p.size * (0.4f + 0.6f * p.alpha), particlePaint)
        }
    }

    private fun drawCurrent(canvas: Canvas, world: World, time: Float) {
        if (world.state != World.State.PLAYING || !world.canDrop) return
        val r = Tiers.radiusPx(world.currentTier, world.worldW)
        val x = world.currentX

        // Ligne de visée en pointillés.
        linePaint.color = 0x40FFFFFF
        linePaint.strokeWidth = world.worldW * 0.004f
        linePaint.pathEffect = DashPathEffect(floatArrayOf(14f, 18f), 0f)
        canvas.drawLine(x, world.spawnY + r, x, world.floorY, linePaint)
        linePaint.pathEffect = null

        val pulse = 1f + 0.05f * sin(time * 5f)
        drawOrb(canvas, x, world.spawnY, r, world.currentTier, pulse, 0f, time)
    }

    private fun drawHud(canvas: Canvas, world: World) {
        val w = world.worldW
        val hud = world.hudH

        // Score central lumineux.
        scorePaint.textSize = hud * 0.5f
        scorePaint.setShadowLayer(hud * 0.18f, 0f, 0f, 0xFFB14CFF.toInt())
        canvas.drawText(world.score.toString(), w * 0.5f, hud * 0.62f, scorePaint)
        scorePaint.clearShadowLayer()

        labelPaint.textAlign = Paint.Align.CENTER
        labelPaint.textSize = hud * 0.14f
        canvas.drawText("MEILLEUR  ${world.best}", w * 0.5f, hud * 0.86f, labelPaint)

        // Aperçu du prochain corps (coin haut-droit).
        val pr = Tiers.radiusPx(world.nextTier, w).coerceAtMost(hud * 0.30f)
        val px = w - hud * 0.5f
        val py = hud * 0.45f
        drawOrb(canvas, px, py, pr, world.nextTier, 1f, 0f, 0f)
        labelPaint.textAlign = Paint.Align.CENTER
        labelPaint.textSize = hud * 0.11f
        canvas.drawText("SUIVANT", px, py + hud * 0.42f, labelPaint)
    }

    private fun drawGameOver(canvas: Canvas, world: World) {
        val w = world.worldW
        val h = world.worldH

        overlayPaint.color = 0xCC060312.toInt()
        canvas.drawRect(0f, 0f, w, h, overlayPaint)

        val cx = w * 0.5f
        val cy = h * 0.42f
        val pw = w * 0.82f
        val ph = h * 0.42f
        panelPaint.shader = RadialGradient(
            cx, cy, pw,
            intArrayOf(0xFF1C1140.toInt(), 0xFF120A2A.toInt()),
            floatArrayOf(0f, 1f), Shader.TileMode.CLAMP
        )
        val rect = android.graphics.RectF(cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
        canvas.drawRoundRect(rect, w * 0.06f, w * 0.06f, panelPaint)
        panelPaint.shader = null

        rimPaint.shader = null
        rimPaint.color = 0x66B14CFF.toInt()
        rimPaint.strokeWidth = w * 0.006f
        canvas.drawRoundRect(rect, w * 0.06f, w * 0.06f, rimPaint)

        titlePaint.textSize = w * 0.085f
        titlePaint.setShadowLayer(w * 0.05f, 0f, 0f, 0xFFFF4FB0.toInt())
        canvas.drawText("PARTIE TERMINÉE", cx, cy - ph * 0.24f, titlePaint)
        titlePaint.clearShadowLayer()

        scorePaint.textSize = w * 0.16f
        scorePaint.setShadowLayer(w * 0.04f, 0f, 0f, 0xFFB14CFF.toInt())
        canvas.drawText(world.score.toString(), cx, cy + w * 0.04f, scorePaint)
        scorePaint.clearShadowLayer()

        labelPaint.textAlign = Paint.Align.CENTER
        labelPaint.textSize = w * 0.045f
        canvas.drawText("MEILLEUR  ${world.best}", cx, cy + ph * 0.20f, labelPaint)

        titlePaint.textSize = w * 0.05f
        titlePaint.color = 0xFFFFFFFF.toInt()
        val bob = 0.5f + 0.5f * sin(System.nanoTime() / 1e9f * 3f)
        titlePaint.alpha = (140 + bob * 115).toInt().coerceIn(0, 255)
        canvas.drawText("Appuyez pour rejouer", cx, cy + ph * 0.40f, titlePaint)
        titlePaint.alpha = 255
    }

    private fun darken(color: Int, f: Float): Int = Color.argb(
        Color.alpha(color),
        (Color.red(color) * f).toInt().coerceIn(0, 255),
        (Color.green(color) * f).toInt().coerceIn(0, 255),
        (Color.blue(color) * f).toInt().coerceIn(0, 255)
    )
}
