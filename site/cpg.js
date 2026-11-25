// CPG brand work: open a project in a dialog with its gallery.
// Without JavaScript (or without dialog support) each tile links to the project on timimbo.com.
(function () {
  var dlg = document.getElementById('cpg-dlg');
  if (!dlg || typeof dlg.showModal !== 'function') return;
  var img = document.getElementById('cpg-img'), count = document.getElementById('cpg-count');
  var thumbs = document.getElementById('cpg-thumbs');
  var prev = dlg.querySelector('.prev'), next = dlg.querySelector('.next');
  var list = [], i = 0, opener = null;
  function show(n) {
    i = (n + list.length) % list.length;
    img.src = list[i][0]; img.alt = list[i][1];
    count.textContent = (i + 1) + ' / ' + list.length;
    [].forEach.call(thumbs.children, function (b, k) { if (k === i) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
  }
  document.querySelectorAll('.cpg-tile').forEach(function (t) {
    t.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault(); opener = t;
      var p = JSON.parse(t.dataset.project);
      list = p.imgs;
      document.getElementById('cpg-tag').textContent = p.tag;
      document.getElementById('cpg-dlg-h').textContent = p.title;
      document.getElementById('cpg-body').textContent = p.body;
      var ppl = document.getElementById('cpg-people'); ppl.textContent = p.people; ppl.hidden = !p.people;
      document.getElementById('cpg-link').href = p.url;
      thumbs.innerHTML = '';
      list.forEach(function (im, k) {
        var b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', 'Show image ' + (k + 1) + ' of ' + list.length);
        var ti = document.createElement('img'); ti.src = im[0]; ti.alt = ''; b.appendChild(ti);
        b.addEventListener('click', function () { show(k); });
        thumbs.appendChild(b);
      });
      prev.hidden = next.hidden = list.length < 2;
      show(0);
      dlg.showModal();
      document.body.style.overflow = 'hidden';
    });
  });
  prev.addEventListener('click', function () { show(i - 1); });
  next.addEventListener('click', function () { show(i + 1); });
  dlg.querySelector('.cpg-x').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') show(i + 1); if (e.key === 'ArrowLeft') show(i - 1); });
  var sx = null, gal = dlg.querySelector('.cpg-gal');
  gal.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
  gal.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); sx = null; });
  dlg.addEventListener('close', function () { document.body.style.overflow = ''; img.src = ''; if (opener) opener.focus(); });
})();
