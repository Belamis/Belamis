package com.belamis.nova

import android.graphics.Canvas
import android.view.SurfaceHolder

/** Boucle de jeu dédiée : met à jour la simulation et dessine à ~60 fps. */
class GameThread(
    private val holder: SurfaceHolder,
    private val view: GameView
) : Thread() {

    @Volatile private var running = false
    private var lastNs = 0L

    fun setRunning(value: Boolean) { running = value }

    override fun run() {
        lastNs = System.nanoTime()
        while (running) {
            val now = System.nanoTime()
            var dt = (now - lastNs) / 1_000_000_000f
            lastNs = now
            if (dt > 0.05f) dt = 0.05f

            var canvas: Canvas? = null
            try {
                canvas = holder.lockCanvas()
                if (canvas != null) {
                    synchronized(holder) {
                        view.update(dt)
                        view.render(canvas)
                    }
                }
            } finally {
                if (canvas != null) {
                    try { holder.unlockCanvasAndPost(canvas) } catch (_: Exception) {}
                }
            }

            // Limite le rythme pour économiser la batterie (~60 fps).
            val frameNs = System.nanoTime() - now
            val targetNs = 16_666_666L
            if (frameNs < targetNs) {
                try { sleep((targetNs - frameNs) / 1_000_000L) } catch (_: InterruptedException) {}
            }
        }
    }
}
