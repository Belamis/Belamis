# Qui est où · Planning de la circonscription de Koungou Nord

Planning partagé de l'équipe : IEN, conseillers pédagogiques, ERUN, Maîtres E, E EREH nord, UPE2A, secrétariat, psychologues.

- Chacun se connecte avec son e-mail et un mot de passe, puis saisit son nom et sa fonction.
- Chacun remplit **son propre** planning. Personne ne peut modifier celui d'un collègue : c'est le serveur qui le refuse, pas seulement l'affichage.
- Tout le monde voit tout, **en temps réel** : une saisie apparaît en une seconde chez les autres.
- Vues Jour, Semaine, Mois, Année (rotations A/B, vacances, jours fériés 2026-2027) et Synthèse.

Le site est un simple dossier de fichiers. Les données sont stockées dans **Firebase** (Google), gratuit pour une équipe de cette taille.

---

## Mise en place (environ 20 minutes, une seule fois)

### 1. Créer le projet Firebase

1. Allez sur <https://console.firebase.google.com> et connectez-vous avec un compte Google.
2. **Ajouter un projet**, par exemple `planning-koungou-nord`. Google Analytics n'est pas nécessaire.

### 2. Activer la connexion par e-mail

1. Menu **Authentication**, puis **Commencer**.
2. Onglet **Sign-in method**, puis **E-mail/Mot de passe**. Activez-le (sans « lien par e-mail ») et enregistrez.
3. Facultatif : dans **Templates**, passez la langue des e-mails en français.

### 3. Créer la base de données

1. Menu **Firestore Database**, puis **Créer une base de données**.
2. Choisissez un emplacement européen (par exemple `europe-west1` ou `europe-west9 (Paris)`), puis **mode production**.
3. Onglet **Règles** : effacez tout, collez le contenu du fichier `firestore.rules`, puis **Publier**.

### 4. Relier le site à votre projet

1. Roue dentée **Paramètres du projet**, rubrique **Vos applications**, icône **`</>`** (Web). Donnez un nom, sans cocher Hosting.
2. Firebase affiche un bloc `firebaseConfig = { apiKey: ..., authDomain: ..., ... }`.
3. Ouvrez le fichier `config.js` et remplacez chaque `A_REMPLACER` par la valeur correspondante.

Ces valeurs ne sont pas des mots de passe. Elles identifient le projet et peuvent être publiques : c'est `firestore.rules` qui protège les données.

### 5. Mettre le site en ligne

**Option A : Netlify (le plus simple, sans ligne de commande)**
1. Allez sur <https://app.netlify.com/drop> et créez un compte gratuit.
2. Glissez-déposez **le dossier `planning-web`** entier dans la page.
3. Netlify donne une adresse du type `https://nom-au-hasard.netlify.app`. Vous pouvez la renommer dans *Site configuration > Change site name*.

**Option B : Firebase Hosting (tout au même endroit)**
Dans un terminal, depuis le dossier `planning-web` :
```
npm install -g firebase-tools
firebase login
firebase use --add        (choisissez votre projet)
firebase deploy
```
L'adresse sera `https://VOTRE-PROJET.web.app`. Les règles de sécurité sont déployées en même temps.

**Option C : GitHub Pages**, si le dépôt est public ou votre compte GitHub payant : *Settings > Pages*, en publiant le dossier `planning-web`.

### 6. Autoriser l'adresse du site

Firebase, **Authentication > Settings > Domaines autorisés > Ajouter un domaine**, puis ajoutez l'adresse du site sans `https://`, par exemple `planning-koungou.netlify.app`. Les adresses `*.web.app` de Firebase Hosting sont déjà autorisées.

### 7. Partager

Envoyez simplement l'adresse du site à vos collègues, par e-mail ou messagerie. À la première visite :
1. une animation présente le logo de la circonscription ;
2. ils cliquent sur **Créer un compte** (e-mail + mot de passe) ;
3. ils indiquent leur prénom, leur nom et leur fonction ;
4. ils arrivent sur le planning.

Sur téléphone, le site s'utilise dans le navigateur. On peut l'ajouter à l'écran d'accueil : dans Safari, *Partager > Sur l'écran d'accueil* ; dans Chrome, *⋮ > Ajouter à l'écran d'accueil*.

---

## Réserver le planning aux adresses académiques (recommandé)

Par défaut, toute personne qui connaît l'adresse du site peut créer un compte. Pour n'accepter que les adresses académiques, par exemple `@ac-mayotte.fr` :

1. Dans `config.js`, mettez `allowedDomain: "ac-mayotte.fr"`. Le site demandera alors à chacun de confirmer son adresse par e-mail.
2. Dans `firestore.rules`, remplacez la fonction `member()` par la version commentée juste en dessous (avec votre domaine), puis republiez les règles.

## Questions fréquentes

- **Mot de passe oublié ?** Le bouton sur l'écran de connexion envoie un e-mail de réinitialisation.
- **Changer d'année scolaire ?** Le calendrier 2026-2027 (rotations, vacances, fériés) est dans `index.html`, dans le bloc `const CAL = {...}`. Pour 2027-2028, il suffit de remplacer ce bloc.
- **Retirer un collègue ?** Firebase, *Authentication > Users*, puis supprimer son compte. Pour effacer aussi son nom du planning, supprimez son document dans *Firestore > people*.
- **Coût ?** Le forfait gratuit de Firebase (Spark) suffit largement : environ 50 000 lectures et 20 000 écritures par jour.
- **Tant que `config.js` n'est pas rempli**, le site s'ouvre en *mode démonstration* avec des collègues fictifs, et rien n'est enregistré.
