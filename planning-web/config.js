// Configuration du planning « Qui est où ».
// Remplacez les valeurs ci-dessous par celles de VOTRE projet Firebase
// (Console Firebase > Paramètres du projet > Vos applications > Configuration du SDK).
// Tant que ces valeurs ne sont pas remplies, le site s'ouvre en mode démonstration.
window.PLANNING_CONFIG = {
  firebase: {
    apiKey: "A_REMPLACER",
    authDomain: "A_REMPLACER.firebaseapp.com",
    projectId: "A_REMPLACER",
    storageBucket: "A_REMPLACER.appspot.com",
    messagingSenderId: "A_REMPLACER",
    appId: "A_REMPLACER",
  },
  // Facultatif : réserver le planning à une adresse e-mail précise, par exemple "ac-mayotte.fr".
  // Laissez "" pour accepter toutes les adresses. Si vous le remplissez, chaque collègue
  // devra confirmer son adresse par e-mail, et pensez à faire la même chose dans firestore.rules.
  allowedDomain: "",
};
