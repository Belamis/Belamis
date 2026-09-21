// Confirmation avant suppression / archivage, et soumission automatique des filtres.
document.addEventListener('submit', function (ev) {
  var f = ev.target;
  if (f.dataset && f.dataset.confirm && !window.confirm(f.dataset.confirm)) ev.preventDefault();
});
document.querySelectorAll('form.filtres select').forEach(function (sel) {
  sel.addEventListener('change', function () { sel.form.submit(); });
});
// Masque le bloc « classe » si le personnel n'est pas dans l'organisation pédagogique.
var caseOrg = document.querySelector('input[name="dans_organisation"]');
var blocClasse = document.getElementById('bloc-classe');
if (caseOrg && blocClasse) {
  var maj = function () { blocClasse.classList.toggle('masque', !caseOrg.checked); };
  caseOrg.addEventListener('change', maj); maj();
}
// Totaux en direct dans la grille de saisie des effectifs.
var grille = document.getElementById('grille-effectifs');
if (grille) {
  var recalculer = function () {
    var totauxCol = {};
    grille.querySelectorAll('tr[data-ligne]').forEach(function (tr) {
      var total = 0;
      tr.querySelectorAll('input[data-niveau]').forEach(function (inp) {
        var v = parseInt(inp.value, 10) || 0;
        if (inp.dataset.niveau !== 'eff_ulis') total += v;
        totauxCol[inp.dataset.niveau] = (totauxCol[inp.dataset.niveau] || 0) + v;
      });
      tr.querySelector('.total-ligne').textContent = total;
    });
    var general = 0;
    Object.keys(totauxCol).forEach(function (k) {
      var c = grille.querySelector('.total-col[data-niveau="' + k + '"]');
      if (c) c.textContent = totauxCol[k];
      if (k !== 'eff_ulis') general += totauxCol[k];
    });
    var g = grille.querySelector('.total-general'); if (g) g.textContent = general;
  };
  grille.addEventListener('input', recalculer); recalculer();
}
