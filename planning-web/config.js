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
  // Seules les adresses de ce domaine peuvent créer un compte, après confirmation par e-mail.
  // La même règle est appliquée côté serveur dans firestore.rules (fonction member()).
  allowedDomain: "ac-mayotte.fr",
  // Contact affiché dans la note « Données personnelles » (ex. "l'IEN de la circonscription, ce.xxx@ac-mayotte.fr").
  contact: "",
};
