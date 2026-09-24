// Configuration du planning « Qui est où » — projet Firebase planning-koungou-nord.
// Ces valeurs identifient le projet ; elles ne sont pas secrètes. La protection des
// données est assurée par les règles de sécurité (firestore.rules).
window.PLANNING_CONFIG = {
  firebase: {
    apiKey: "AIzaSyA5fKAu-GXdNLwYgiB1A0AEPPwQfqrJjrw",
    authDomain: "planning-koungou-nord.firebaseapp.com",
    projectId: "planning-koungou-nord",
    storageBucket: "planning-koungou-nord.firebasestorage.app",
    messagingSenderId: "520616849068",
    appId: "1:520616849068:web:24d82d665d7a7d3251f909",
  },
  // Facultatif : réserver le planning à une adresse e-mail précise, par exemple "ac-mayotte.fr".
  // Laissez "" pour accepter toutes les adresses. Si vous le remplissez, chaque collègue
  // devra confirmer son adresse par e-mail, et pensez à faire la même chose dans firestore.rules.
  allowedDomain: "",
};
