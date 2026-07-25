package com.belamis.nova

import android.content.Context
import android.graphics.Canvas
import android.view.MotionEvent
import android.view.SurfaceHolder
import android.view.SurfaceView
import com.belamis.nova.game.World
import com.belamis.nova.render.Renderer

/**
 * Surface de jeu : héberge le monde, le rendu et la boucle de jeu,
 * gère les entrées tactiles et la persistance du meilleur score.
 */
class GameView(context: Context) : SurfaceView(context), SurfaceHolder.Callback {

    private val world = World()
    private val renderer = Renderer()
    private var thread: GameThread? = null
    private var time = 0f

    private val prefs = context.getSharedPreferences("nova", Context.MODE_PRIVATE)

    init {
        holder.addCallback(this)
        isFocusable = true
        world.best = prefs.getInt("best", 0)
    }

    fun update(dt: Float) {
        time += dt
        world.update(dt)
    }

    fun render(canvas: Canvas) {
        renderer.draw(canvas, world, time)
    }

    // --- SurfaceHolder ---

    override fun surfaceCreated(h: SurfaceHolder) {
        thread = GameThread(h, this).also {
            it.setRunning(true)
            it.start()
        }
    }

    override fun surfaceChanged(h: SurfaceHolder, format: Int, width: Int, height: Int) {
        synchronized(h) {
            world.configure(width, height)
            renderer.resize(width, height)
        }
    }

    override fun surfaceDestroyed(h: SurfaceHolder) {
        persistBest()
        thread?.let {
            it.setRunning(false)
            var retry = true
            while (retry) {
                try { it.join(); retry = false } catch (_: InterruptedException) {}
            }
        }
        thread = null
    }

    // --- Entrées ---

    override fun onTouchEvent(event: MotionEvent): Boolean {
        when (event.actionMasked) {
            MotionEvent.ACTION_DOWN, MotionEvent.ACTION_MOVE -> {
                if (world.state == World.State.PLAYING) world.onPointerMove(event.x)
            }
            MotionEvent.ACTION_UP -> {
                if (world.state == World.State.GAME_OVER) {
                    world.reset()
                } else {
                    world.onPointerMove(event.x)
                    if (world.onDrop()) persistBest()
                }
            }
        }
        return true
    }

    private fun persistBest() {
        val stored = prefs.getInt("best", 0)
        if (world.best > stored) prefs.edit().putInt("best", world.best).apply()
    }
}
