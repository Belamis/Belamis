# Mettre Belamis en ligne sur Netlify

Le site est statique : Netlify l'héberge gratuitement à une adresse du type
`https://belamis.netlify.app`.

## Méthode 1 : glisser-déposer (5 minutes, sans GitHub)

1. Crée un compte sur <https://app.netlify.com> (avec ton adresse mail ou GitHub).
2. Ouvre <https://app.netlify.com/drop>.
3. Glisse le fichier `belamis-netlify.zip` (ou le dossier `revision/dist`, créé par
   `sh revision/netlify-build.sh`) dans la zone de dépôt.
4. Le site est en ligne en quelques secondes. Dans **Site configuration → Change site name**,
   choisis le nom : `belamis` donne `https://belamis.netlify.app` (s'il est libre).

Pour une mise à jour : **Deploys** → glisse le nouveau zip dans la zone « Drag and drop ».

## Méthode 2 : relier le dépôt GitHub (mises à jour automatiques)

1. Sur Netlify : **Add new site → Import an existing project → GitHub**,
   autorise l'accès, puis choisis le dépôt `Belamis/Belamis`.
2. **Branch to deploy** : la branche qui contient la plateforme
   (aujourd'hui `claude/affectionate-pascal-87hjnl`, ou `main` après fusion).
3. Laisse les réglages proposés : ils sont lus dans `netlify.toml`
   (commande `sh revision/netlify-build.sh`, dossier publié `revision/dist`).
4. **Deploy**. Ensuite, chaque modification poussée sur cette branche remet le site à jour.

## Après la mise en ligne

- **Connexion par mail et sauvegarde des révisions** : tant que `config.js` est vide,
  le site tourne en mode démonstration (sauvegarde dans le navigateur).
  Suis `SUPABASE.md`, et dans Supabase mets l'adresse Netlify dans
  *Authentication → URL Configuration* (Site URL et Redirect URLs).
- **Nom de domaine à toi** (facultatif, environ 10 € par an) : Netlify →
  **Domain management → Add a domain**, puis suis les instructions DNS.
  Le certificat HTTPS est automatique et gratuit.
