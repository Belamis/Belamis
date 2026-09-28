# Belamis — plateforme de révision CRPE

Page d'accueil animée : un univers vivant dessiné en temps réel sur `<canvas>`
(nébuleuse, rayons de lumière, fragments en « warp », icosaèdre en fil de fer,
anneaux orbitaux, cœur lumineux pulsant).

- `index.html` : structure de la page
- `style.css` : mise en page, effets de verre, apparitions
- `app.js` : moteur de l'animation + interactions
- `raphael.js` : transition de lancement (étoiles filantes → trou noir → explosion → Raphaël) avec `assets/transition.mp3`
- `auth.js` + `config.js` : connexion par mail sans mot de passe et sauvegarde des révisions (Supabase)
- `supabase/` : script de la base de données et modèle du mail de connexion

**Pour brancher la connexion par mail, suis [SUPABASE.md](SUPABASE.md).**

Interactions : la souris incline l'univers, le scroll accélère les fragments,
un clic sur le fond déclenche une onde d'étincelles. Le mode « mouvement réduit »
du système est respecté.

Aucun build : ouvrir `index.html` dans un navigateur, ou `python3 -m http.server`
dans ce dossier.
