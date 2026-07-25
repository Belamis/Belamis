package com.belamis.nova.render

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.LinearGradient
import android.graphics.Paint
import android.graphics.RadialGradient
import android.graphics.Shader
import kotlin.math.sin
import kotlin.random.Random

/**
 * Fond spatial dynamique : dégradé profond, nébuleuses colorées qui dérivent
 * lentement et champ d'étoiles scintillantes sur deux couches de parallaxe.
 */
class StarField {

    private class Star(val x: Float, val y: Float, val r: Float, val phase: Float, val speed: Float, val layer: Int)
    private class Nebula(val x: Float, val y: Float, val r: Float, val color: Int, val speed: Float, val phase: Float)

    private var w = 0f
    private var h = 0f
    private val stars = ArrayList<Star>()
    private val nebulas = ArrayList<Nebula>()

    private var bgShader: LinearGradient? = null
    private val bgPaint = Paint()
    private val starPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val nebulaPaint = Paint(Paint.ANTI_ALIAS_FLAG)

    fun resize(width: Float, height: Float) {
        if (width == w && height == h) return
        w = width; h = height
        bgShader = LinearGradient(
            0f, 0f, 0f, h,
            intArrayOf(0xFF0B0620.toInt(), 0xFF130A2E.toInt(), 0xFF1B0B3A.toInt()),
            floatArrayOf(0f, 0.6f, 1f),
            Shader.TileMode.CLAMP
        )
        bgPaint.shader = bgShader

        val rnd = Random(42)
        stars.clear()
        val count = (w * h / 5200f).toInt().coerceIn(90, 260)
        repeat(count) {
            val layer = if (rnd.nextFloat() < 0.35f) 1 else 0
            stars.add(
                Star(
                    rnd.nextFloat() * w,
                    rnd.nextFloat() * h,
                    (if (layer == 1) 1.6f else 0.9f) + rnd.nextFloat() * 1.4f,
                    rnd.nextFloat() * 6.28f,
                    0.6f + rnd.nextFloat() * 2.2f,
                    layer
                )
            )
        }

        nebulas.clear()
        val palette = intArrayOf(0xFF7A3CFF.toInt(), 0xFFFF4FB0.toInt(), 0xFF2E7DE0.toInt(), 0xFF34D6C0.toInt())
        repeat(4) { i ->
            nebulas.add(
                Nebula(
                    rnd.nextFloat() * w,
                    h * (0.15f + rnd.nextFloat() * 0.7f),
                    w * (0.35f + rnd.nextFloat() * 0.35f),
                    palette[i % palette.size],
                    (if (rnd.nextBoolean()) 1f else -1f) * (4f + rnd.nextFloat() * 8f),
                    rnd.nextFloat() * 6.28f
                )
            )
        }
    }

    fun draw(canvas: Canvas, time: Float) {
        if (w == 0f) return
        canvas.drawRect(0f, 0f, w, h, bgPaint)

        // Nébuleuses dérivantes (halos radiaux très doux).
        nebulaPaint.style = Paint.Style.FILL
        for (n in nebulas) {
            val cx = ((n.x + n.speed * time) % (w + n.r * 2) + (w + n.r * 2)) % (w + n.r * 2) - n.r
            val cy = n.y + sin(time * 0.15f + n.phase) * h * 0.03f
            val alpha = (0.10f + 0.05f * sin(time * 0.3f + n.phase)).coerceIn(0.04f, 0.18f)
            nebulaPaint.shader = RadialGradient(
                cx, cy, n.r,
                intArrayOf(withA(n.color, (alpha * 255).toInt()), withA(n.color, 0)),
                floatArrayOf(0f, 1f),
                Shader.TileMode.CLAMP
            )
            canvas.drawCircle(cx, cy, n.r, nebulaPaint)
        }

        // Étoiles scintillantes.
        starPaint.shader = null
        for (s in stars) {
            val tw = 0.5f + 0.5f * sin(time * s.speed + s.phase)
            val drift = if (s.layer == 1) (time * 6f) else (time * 2.4f)
            val y = (s.y + drift) % h
            val a = (0.35f + 0.65f * tw)
            starPaint.color = Color.argb((a * 255).toInt(), 255, 255, 255)
            canvas.drawCircle(s.x, y, s.r * (0.7f + 0.5f * tw), starPaint)
        }
    }

    private fun withA(color: Int, a: Int): Int =
        Color.argb(a.coerceIn(0, 255), Color.red(color), Color.green(color), Color.blue(color))
}
