# Brancher la connexion par mail (Supabase)

La plateforme utilise **Supabase** pour deux choses :

- **la connexion sans mot de passe** : l'élève tape son mail et reçoit un lien
  (et un code à 6 chiffres) pour se connecter ;
- **la sauvegarde des révisions** : une ligne par élève dans la table
  `progress`, que lui seul peut lire et modifier.

Tant que ce n'est pas branché, la page tourne en **mode démonstration** :
aucun mail n'est envoyé et la « sauvegarde » reste dans le navigateur.

Compte environ 20 minutes. Tout est gratuit pour démarrer.

## 1. Créer le projet

1. Va sur <https://supabase.com> et crée un compte (bouton *Start your project*).
2. *New project* : nom `belamis`, choisis un mot de passe de base de données
   (garde-le, mais on n'en aura pas besoin ici), région **Europe (Paris ou Francfort)**.
3. Attends 1 à 2 minutes que le projet soit prêt.

## 2. Créer la table de sauvegarde

1. Menu de gauche : **SQL Editor** → *New query*.
2. Colle tout le contenu de [`supabase/schema.sql`](supabase/schema.sql).
3. Clique **Run**. Tu dois voir « Success. No rows returned ».

## 3. Régler la connexion par mail

1. **Authentication → Sign In / Providers → Email** : vérifie que *Email* est activé.
2. **Authentication → URL Configuration** :
   - *Site URL* : l'adresse de ton site en ligne (par exemple `https://belamis.netlify.app`) ;
   - *Redirect URLs* : ajoute cette même adresse, et `http://localhost:8000/**`
     pour tester sur ton ordinateur.
3. **Authentication → Emails → Templates** : dans **Magic Link** *et* dans
   **Confirm signup** (le premier mail d'un nouvel élève), remplace le contenu par
   celui de [`supabase/email-connexion.html`](supabase/email-connexion.html),
   avec comme sujet : `Ta connexion à Belamis`.
   C'est ce modèle qui met le **code à 6 chiffres** dans le mail.

## 4. Relier le site au projet

1. **Project Settings → API** (ou *Data API*) : copie
   - la **Project URL** (`https://xxxx.supabase.co`),
   - la clé **anon / public**.
2. Colle-les dans [`config.js`](config.js) :

   ```js
   window.BELAMIS_CONFIG = {
     supabaseUrl: "https://xxxx.supabase.co",
     supabaseAnonKey: "eyJhbGciOi...",
   };
   ```

La clé *anon* est faite pour être publique : ce sont les règles de l'étape 2
qui protègent les données. **Ne mets jamais la clé `service_role` dans le site.**

## 5. Envoyer des mails à toutes les adresses perso (obligatoire)

La connexion accepte **n'importe quelle adresse** : Gmail, Outlook, Hotmail,
Live, Yahoo, Orange, Wanadoo, Free, SFR, La Poste, iCloud, Proton… Il n'y a
rien à configurer par fournisseur. Deux réglages décident en revanche si le
mail **arrive vraiment**, et pas dans les spams.

### 5a. Un vrai service d'envoi (SMTP)

Le service de mail fourni par Supabase est **réservé aux tests** : il n'envoie
qu'aux adresses des membres de ton équipe Supabase, et seulement quelques mails
par heure. Branche un service d'envoi, par exemple **Brevo** (français,
300 mails/jour gratuits) :

1. Crée un compte sur <https://www.brevo.com>, puis *SMTP & API* → *SMTP* :
   note le serveur, le port, l'identifiant et génère une clé SMTP.
2. Dans Supabase : **Authentication → Emails → SMTP Settings** → *Enable custom SMTP*,
   colle ces informations, nom d'expéditeur `Belamis`.
3. Dans **Authentication → Rate Limits**, monte la limite d'envoi de mails
   (par exemple 100 par heure).

### 5b. Une adresse d'expéditeur sur ton propre nom de domaine

C'est ce qui fait la différence entre « boîte de réception » et « spams ».
Gmail, Outlook/Hotmail, Yahoo et Orange/Wanadoo **refusent ou classent en
indésirable** un mail qui prétend venir d'une adresse `@gmail.com`,
`@hotmail.fr`, `@orange.fr`… mais qui est envoyé par un autre service (Brevo).
L'expéditeur doit donc être une adresse d'un domaine à toi, par exemple
`connexion@belamis.fr`.

1. Achète un nom de domaine (environ 10 € par an chez OVH, Gandi, IONOS…).
2. Dans Brevo : **Expéditeurs, domaines et IP dédiées → Domaines** → ajoute ton
   domaine, puis copie les enregistrements qu'il affiche (SPF, DKIM, DMARC)
   dans la zone DNS de ton domaine, chez ton registraire.
3. Attends que Brevo affiche le domaine comme **authentifié** (quelques minutes
   à quelques heures).
4. Dans Supabase, **SMTP Settings** → *Sender email* : `connexion@ton-domaine.fr`.

Côté élève, la fenêtre de connexion corrige les fautes de frappe courantes
(« gmial.com », « hotmial.fr », « wanado.fr »…), rappelle de regarder dans les
spams et propose de renvoyer le mail au bout d'une minute.

## 6. Tester

Sur ton ordinateur, dans le dossier `revision/` :

```bash
python3 -m http.server 8000
```

puis ouvre <http://localhost:8000>. Clique **Se connecter**, entre ton mail,
et utilise le lien ou le code reçu. Lance ensuite une révision : le message
« Séance n°… » confirme que la sauvegarde fonctionne. Tu peux voir les lignes
enregistrées dans **Table Editor → progress**.
