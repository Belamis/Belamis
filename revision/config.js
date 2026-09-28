/*
 * Configuration Supabase (voir SUPABASE.md, étape 4).
 * La clé « anon » est publique par conception : ce sont les règles de sécurité
 * de la base (RLS) qui protègent les données de chaque élève.
 * Tant que ces deux valeurs sont vides, la page tourne en mode démonstration :
 * aucun mail n'est envoyé et la sauvegarde reste dans ce navigateur.
 */
window.BELAMIS_CONFIG = {
  supabaseUrl: "",
  supabaseAnonKey: "",
};
