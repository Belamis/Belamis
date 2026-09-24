# Qui est où · Planning de la circonscription de Koungou Nord

Planning partagé de l'équipe : IEN, conseillers pédagogiques, ERUN, Maîtres E, E EREH nord, UPE2A, secrétariat, psychologues.

- Chacun se connecte avec **l'adresse e-mail de son choix** (Gmail, Outlook, Hotmail, La Poste, académique…) et un mot de passe, confirme son adresse, puis saisit son nom, sa fonction et le **code d'équipe**.
- Chacun remplit **son propre** planning. Personne ne peut modifier celui d'un collègue : c'est le serveur qui le refuse, pas seulement l'affichage.
- Tout le monde voit tout, **en temps réel** : une saisie apparaît en une seconde chez les autres.
- Ergonomie : sur ordinateur, planning plein écran avec jours, noms et totaux fixes et mode Compact ; sur téléphone, semaine en liste jour par jour, barre de navigation en bas et bouton « + ».
- Vues Jour, Semaine, Mois, Année (rotations A/B, vacances, jours fériés 2026-2027), Synthèse et Écoles.
- Annonces d'équipe, reprise de la semaine précédente, impression ou PDF, export Excel et export vers son agenda (.ics).
- Saisie : disponibilités (onglet « Disponible »), visite en binôme (« Avec »), répétition chaque semaine, toutes les 2 semaines ou en semaines A/B jusqu'à une date, « Ma semaine type » à enregistrer puis appliquer, alertes avant d'enregistrer (chevauchement, journée de plus de 10 h, jour férié ou de vacances, absence le même jour).
- Photo de profil au choix (recadrée et allégée dans le navigateur, environ 15 Ko, enregistrée avec le profil : aucun stockage payant nécessaire), ou illustration (24 personnages dessinés, style « Notionists » de Zoish via DiceBear, licence CC0) et sons discrets à l'ouverture et lors des actions, qu'on peut couper avec le bouton 🔊.

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
4. Créez le **code d'équipe** (voir plus bas, « Code d'équipe »).

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
3. ils confirment leur adresse en cliquant sur le lien reçu par e-mail ;
4. ils indiquent leur prénom, leur nom, leur fonction et le **code d'équipe** (à leur donner de vive voix ou par message, pas dans un lieu public) ;
5. ils arrivent sur le planning.

Sur téléphone, le site s'utilise dans le navigateur. On peut l'ajouter à l'écran d'accueil : dans Safari, *Partager > Sur l'écran d'accueil* ; dans Chrome, *⋮ > Ajouter à l'écran d'accueil*.

---

## Code d'équipe (qui peut entrer)

Toutes les adresses e-mail sont acceptées, une fois confirmées par le lien reçu. Pour entrer dans le planning, il faut en plus le **code d'équipe** : sans lui, on ne peut ni créer de profil ni voir quoi que ce soit (le serveur le refuse).

**Créer ou changer le code** (console Firebase, *Firestore Database > Données*) :
1. **+ Commencer une collection**, identifiant `config`, puis **Suivant**.
2. Identifiant du document : `acces`.
3. Champ `code`, type **string**, valeur en MAJUSCULES, par exemple `KOUNGOU2026`. **Enregistrer**.

Le site met automatiquement en majuscules ce que tape la personne. Changer le code plus tard n'exclut pas ceux déjà inscrits : il bloque seulement les nouvelles inscriptions avec l'ancien code. Ce document n'est lisible par personne depuis le site.

Pour réserver de nouveau le planning à un seul domaine (ex. `ac-mayotte.fr`), renseignez `allowedDomain` dans `config.js` (message à l'écran uniquement ; le serveur, lui, s'appuie sur le code d'équipe).

Conseil : dans *Authentication > Templates*, passez la langue des e-mails en **français**, et prévenez l'équipe que l'e-mail de confirmation peut arriver dans les indésirables.

## Tout remettre à zéro

1. *Authentication > Users* : cochez tous les comptes (case en haut de la liste), puis **Supprimer les comptes**.
2. *Firestore Database > Données* : pour chaque collection `people`, `planning`, `annonces`, `postes`, `motifs`, cliquez sur les **⋮** à côté de son nom, puis **Supprimer la collection** (tapez son nom pour confirmer). Conservez `config`.

Le planning repart alors d'une page blanche : chacun recrée son compte.

## Données personnelles (RGPD)

- Une note « Données personnelles et confidentialité » est accessible depuis l'écran de connexion, le profil et le bouton **i** de la barre latérale. Indiquez la personne à contacter dans `config.js`, ligne `contact`.
- **Arrêt maladie** : les collègues voient seulement « Absent ». Le motif exact et la précision de toute absence sont rangés à part, et le serveur ne les donne qu'à la personne concernée.
- Chacun peut **supprimer son compte et toutes ses données** depuis *Mon profil*. Le mot de passe est redemandé pour confirmer.
- Les données sont hébergées dans l'Union européenne (Firestore, région `europe-west1`, Belgique).

## Protéger la clé Firebase (recommandé)

1. Allez sur <https://console.cloud.google.com/apis/credentials> et choisissez le projet `planning-koungou-nord` en haut de la page.
2. Cliquez sur la clé nommée **Browser key (auto created by Firebase)**.
3. Dans **Restrictions relatives aux applications**, choisissez **Sites Web**, puis ajoutez :
   - `https://planning-koungou-nord.netlify.app/*`
   - `https://planning-koungou-nord.firebaseapp.com/*`, nécessaire pour les e-mails de confirmation et de mot de passe oublié.
4. Cliquez sur **Enregistrer**. La prise en compte peut prendre quelques minutes.

La clé ne pourra alors plus être utilisée depuis un autre site.

## Mettre à jour le site

Après une modification des fichiers, dans Netlify : ouvrez le projet, onglet **Deploys**, puis glissez-déposez à nouveau le dossier dans la zone prévue en bas de la page. Les données de l'équipe ne sont pas touchées. Si `firestore.rules` a changé, recopiez-le aussi dans Firebase (*Firestore > Règles > Publier*).

## Questions fréquentes

- **Mot de passe oublié ?** Le bouton sur l'écran de connexion envoie un e-mail de réinitialisation.
- **Changer d'année scolaire ?** Le calendrier 2026-2027 (rotations, vacances, fériés) est dans `index.html`, dans le bloc `const CAL = {...}`. Pour 2027-2028, il suffit de remplacer ce bloc.
- **Retirer un collègue ?** Le plus simple est qu'il utilise lui-même « Supprimer mon compte » dans son profil. Sinon : Firebase, *Authentication > Users*, supprimer son compte, puis supprimer son document dans *Firestore > people*.
- **Coût ?** Le forfait gratuit de Firebase (Spark) suffit largement : environ 50 000 lectures et 20 000 écritures par jour.
- **Tant que `config.js` n'est pas rempli**, le site s'ouvre en *mode démonstration* avec des collègues fictifs, et rien n'est enregistré.
