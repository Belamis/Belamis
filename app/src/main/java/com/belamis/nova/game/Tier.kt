package com.belamis.nova.game

import android.graphics.Color

/**
 * Définition d'un palier de corps céleste.
 * Le rayon est exprimé en fraction de la largeur du conteneur pour rester
 * indépendant de la résolution de l'écran.
 *
 * @property radiusFrac rayon relatif à la largeur du monde
 * @property core couleur du centre lumineux
 * @property edge couleur du bord
 * @property glow couleur du halo (avec alpha faible)
 */
data class Tier(
    val index: Int,
    val name: String,
    val radiusFrac: Float,
    val core: Int,
    val edge: Int,
    val glow: Int
)

object Tiers {

    /** Palette cosmique — 11 paliers, de la poussière d'étoile au trou noir. */
    val list: List<Tier> = listOf(
        Tier(0, "Poussière", 0.040f, 0xFFFFFFFF.toInt(), 0xFF9FE8FF.toInt(), 0x5590E0FF.toInt()),
        Tier(1, "Braise", 0.052f, 0xFFFFE0A8.toInt(), 0xFFFF9A3C.toInt(), 0x55FF8A2C.toInt()),
        Tier(2, "Astéroïde", 0.066f, 0xFFC7D2E4.toInt(), 0xFF6B7A96.toInt(), 0x557A8AA6.toInt()),
        Tier(3, "Comète", 0.081f, 0xFFCFFFF4.toInt(), 0xFF34D6C0.toInt(), 0x5534D6C0.toInt()),
        Tier(4, "Lune", 0.098f, 0xFFF2F4FA.toInt(), 0xFFAAB4CC.toInt(), 0x55C0CCE6.toInt()),
        Tier(5, "Planète", 0.117f, 0xFF9FD0FF.toInt(), 0xFF2E7DE0.toInt(), 0x552E7DE0.toInt()),
        Tier(6, "Monde corail", 0.138f, 0xFFFFC2E8.toInt(), 0xFFFF4FB0.toInt(), 0x55FF4FB0.toInt()),
        Tier(7, "Géante", 0.161f, 0xFFFFE7A8.toInt(), 0xFFF0A93A.toInt(), 0x55F0A93A.toInt()),
        Tier(8, "Étoile", 0.187f, 0xFFFFFFFF.toInt(), 0xFFFFCB4D.toInt(), 0x66FFD24D.toInt()),
        Tier(9, "Nébuleuse", 0.215f, 0xFFE7C4FF.toInt(), 0xFF9A4CFF.toInt(), 0x669A4CFF.toInt()),
        Tier(10, "Trou noir", 0.246f, 0xFF1A1030.toInt(), 0xFF7A3CFF.toInt(), 0x88B14CFF.toInt())
    )

    val max: Int get() = list.size - 1

    fun radiusPx(index: Int, worldWidth: Float): Float =
        list[index].radiusFrac * worldWidth

    /** Score gagné en créant un corps de ce palier (progression triangulaire). */
    fun scoreForTier(index: Int): Int = index * (index + 1) / 2

    /** Couleur utilitaire avec alpha remplacé. */
    fun withAlpha(color: Int, alpha: Int): Int =
        Color.argb(alpha, Color.red(color), Color.green(color), Color.blue(color))
}
