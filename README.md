# Nova — Cosmic Merge 🌌

Un jeu Android de **fusion physique** dans l'esprit de *Fruit Merge / Suika*,
mais avec un concept cosmique original et un style visuel **moderne, néon et
dynamique**.

Au lieu de fruits, vous faites tomber des **corps célestes**. Deux corps
identiques qui se touchent **fusionnent** en un corps du palier supérieur.
Enchaînez les fusions sans faire déborder le conteneur… jusqu'au **trou noir**.

## 🎮 Le concept

11 paliers à débloquer par fusion :

`Poussière d'étoile → Braise → Astéroïde → Comète → Lune → Planète →
Monde corail → Géante gazeuse → Étoile → Nébuleuse → Trou noir`

- On lâche uniquement les 5 premiers paliers (choisis aléatoirement).
- Chaque fusion rapporte des points (progression triangulaire).
- La partie se termine si la pile déborde la **ligne de danger** en haut.
- Le **meilleur score** est sauvegardé localement.

## ✨ Direction artistique

Tout est dessiné à la main sur `Canvas`, sans image externe :

- Fond spatial en dégradé profond avec **nébuleuses dérivantes** et
  **champ d'étoiles scintillantes** en parallaxe.
- Corps célestes rendus comme des **orbes volumétriques** : halo radial,
  dégradé décentré, liseré lumineux et reflet spéculaire.
- Le trou noir final possède un **disque d'accrétion animé** (dégradé
  circulaire en rotation) autour d'un horizon des événements sombre.
- **Particules** de fusion, **flash** lumineux et **secousse d'écran**
  proportionnels à l'importance de la fusion.
- Interface néon : score lumineux, aperçu du prochain corps, ligne de
  danger pulsante.

## 🕹️ Contrôles

- **Glisser** horizontalement : déplace le corps en attente.
- **Relâcher** : lâche le corps.
- Écran de fin : **appuyer** pour rejouer.

## 🧠 Technique

- 100 % **Kotlin**, rendu `SurfaceView` + thread de jeu dédié (~60 fps).
- **Moteur physique maison** basé position (*Position Based Dynamics*) :
  prédiction puis relaxation itérative des contraintes → empilement stable
  des cercles sans réglages de restitution fragiles.
- Aucune dépendance de moteur de jeu ; seulement AndroidX core + appcompat.

### Structure

```
app/src/main/java/com/belamis/nova/
├── MainActivity.kt        Plein écran immersif, monte la vue de jeu
├── GameView.kt            SurfaceView : entrées tactiles, meilleur score
├── GameThread.kt          Boucle de jeu (update + render)
├── game/
│   ├── Tier.kt            Les 11 paliers (rayons, couleurs, halos, score)
│   ├── Body.kt            Corps physique circulaire
│   ├── World.kt           Simulation : chute, collisions, fusion, game over
│   └── Particle.kt        Particules + pool
└── render/
    ├── Renderer.kt        Rendu des orbes, HUD, overlays
    └── StarField.kt       Fond spatial animé
```

## 🔧 Compilation

Projet Android Studio standard (Gradle wrapper inclus).

```bash
# Nécessite le SDK Android (ANDROID_HOME) + JDK 17
./gradlew assembleDebug
# APK : app/build/outputs/apk/debug/app-debug.apk
```

Ou ouvrez le dossier dans **Android Studio** et lancez ▶.

| Paramètre     | Valeur |
|---------------|--------|
| minSdk        | 24 (Android 7.0) |
| targetSdk     | 35 |
| Langage       | Kotlin 2.0 |
| AGP / Gradle  | 8.7.3 / 8.14.3 |
