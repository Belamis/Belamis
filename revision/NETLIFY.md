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

## Vérification des réponses par l'IA

Sous chaque exercice rédigé, le bouton **Vérifier avec l'IA** envoie la réponse, l'énoncé et
le corrigé à Claude (Anthropic) via la fonction `revision/netlify/functions/verifier.mts`.
Il renvoie un avis : juste / en partie juste / à revoir, une note sur le barème, ce qui est juste,
ce qu'il faut corriger et un conseil. Le bouton reste caché tant que le service n'est pas activé.

1. **Déploiement par GitHub obligatoire** (méthode 2) : le glisser-déposer d'un zip ne publie pas
   les fonctions Netlify.
2. Crée une clé sur <https://console.anthropic.com> (**API Keys**) et ajoute un peu de crédit
   (**Billing**). Une vérification coûte environ 2 à 4 centimes (plus pour une longue rédaction).
3. Sur Netlify : **Site configuration → Environment variables → Add a variable** :
   `ANTHROPIC_API_KEY` = ta clé. Puis **Deploys → Trigger deploy**.
4. Facultatif : `BELAMIS_IA_MODEL` pour changer de modèle (par défaut `claude-opus-5-5`).

La clé reste sur le serveur Netlify, jamais dans le navigateur. Chaque adresse IP est limitée
à 12 vérifications par minute. Pour suivre ou plafonner la dépense : console Anthropic →
**Limits** (plafond mensuel).
