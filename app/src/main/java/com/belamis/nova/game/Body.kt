package com.belamis.nova.game

/**
 * Corps physique circulaire simulé dans le monde.
 * Masse proportionnelle à la surface (r²) pour des collisions crédibles.
 */
class Body(
    var x: Float,
    var y: Float,
    var tier: Int,
    var radius: Float
) {
    var vx: Float = 0f
    var vy: Float = 0f

    /** Position précédente, utilisée par le solveur basé position (PBD). */
    var prevX: Float = x
    var prevY: Float = y

    /** true tant que le corps est en jeu (false une fois fusionné/consommé). */
    var alive: Boolean = true

    /** true une fois que le corps a touché quelque chose après un lâcher. */
    var landed: Boolean = false

    /** Effet d'apparition : facteur d'échelle animé (0 -> 1). */
    var spawnScale: Float = 1f

    /** Impulsion de "pop" appliquée juste après une fusion (pour l'animation). */
    var pop: Float = 0f

    val mass: Float get() = radius * radius

    fun speedSq(): Float = vx * vx + vy * vy
}
