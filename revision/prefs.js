/*
 * Belamis — préférences de l'appareil (thème, taille du texte, animations, son).
 * Chargé dans <head> pour appliquer le thème avant l'affichage.
 */
(() => {
  "use strict";
  const KEY = "belamis-prefs";
  const DEFAULTS = { theme: "nuit", text: "normal", motion: "complet", sound: true };
  let prefs = { ...DEFAULTS };
  try { prefs = { ...DEFAULTS, ...JSON.parse(localStorage.getItem(KEY) || "{}") }; } catch (_) { /* stockage indisponible */ }

  const listeners = [];
  function apply() {
    const html = document.documentElement;
    html.dataset.theme = prefs.theme;
    html.dataset.text = prefs.text;
    html.dataset.motion = prefs.motion;
  }
  apply();

  window.BelamisPrefs = {
    DEFAULTS,
    get: (k) => (k ? prefs[k] : { ...prefs }),
    set(k, v) {
      prefs[k] = v;
      try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (_) { /* stockage indisponible */ }
      apply();
      listeners.forEach((fn) => fn(k, v));
    },
    onChange: (fn) => listeners.push(fn),
  };
})();
