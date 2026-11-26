// Photography + video page: index hover preview, chapter bar, full screen viewer.
(function () {
  var nav = document.querySelector('.nav');
  var setNav = function () { if (nav) document.documentElement.style.setProperty('--navh', nav.offsetHeight + 'px'); };
  setNav(); addEventListener('resize', setNav); if (document.fonts) document.fonts.ready.then(setNav);
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Index: a preview image follows the pointer (mouse only)
  var peek = document.getElementById('pv-peek');
  if (peek && matchMedia('(hover: hover) and (pointer: fine)').matches) {
    document.querySelectorAll('.pv-index a').forEach(function (a) {
      a.addEventListener('mouseenter', function () { peek.src = a.dataset.preview; peek.classList.add('on'); });
      a.addEventListener('mouseleave', function () { peek.classList.remove('on'); });
      a.addEventListener('mousemove', function (e) { peek.style.transform = 'translate(' + (e.clientX + 24) + 'px,' + (e.clientY - 120) + 'px)' + (reduce ? '' : ' rotate(-2deg)'); });
    });
  }

  // Chapter bar: highlight the chapter in view
  var chips = [].slice.call(document.querySelectorAll('.pv-chips a'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        chips.forEach(function (c) {
          var on = c.getAttribute('href') === '#' + e.target.id;
          c.classList.toggle('on', on);
          if (on) { c.setAttribute('aria-current', 'true'); var bar = c.parentNode; if (bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: c.offsetLeft - 40, behavior: reduce ? 'auto' : 'smooth' }); }
          else c.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    document.querySelectorAll('.pv-ch').forEach(function (s) { io.observe(s); });
  }

  // Viewer
  var lb = document.getElementById('pv-lb');
  if (!lb || typeof lb.showModal !== 'function') return;
  var stage = document.getElementById('pv-lb-stage'), cap = document.getElementById('pv-lb-cap'), num = document.getElementById('pv-lb-n');
  var list = [], i = 0, opener = null, setName = '';
  function render() {
    var el = list[i]; stage.innerHTML = '';
    if (el.dataset.full) {
      var im = document.createElement('img'); im.src = el.dataset.full; im.alt = el.dataset.alt; stage.appendChild(im);
      var nx = list[(i + 1) % list.length]; if (nx && nx.dataset.full) { var pre = new Image(); pre.src = nx.dataset.full; }
    } else {
      var o = el.classList.contains('v') ? 'v' : 'h', m;
      if (el.dataset.type === 'mp4') {
        m = document.createElement('video'); m.src = el.dataset.video; m.controls = true; m.autoplay = true; m.playsInline = true;
        m.addEventListener('error', function () { stage.innerHTML = '<p class="fallback">This video plays on timimbo.com. <a href="https://www.timimbo.com/video" target="_blank" rel="noopener">Watch it there ↗</a></p>'; });
      } else {
        m = document.createElement('iframe'); m.src = el.dataset.video; m.title = el.dataset.alt;
        m.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; m.allowFullscreen = true;
      }
      m.className = o; stage.appendChild(m);
    }
    cap.textContent = setName + ' · ' + el.dataset.alt;
    num.textContent = (i + 1) + ' / ' + list.length;
  }
  function open(items, n, name, from) { list = items; i = n; setName = name; opener = from; lb.showModal(); document.body.style.overflow = 'hidden'; render(); }
  function go(d) { if (list.length < 2) return; i = (i + d + list.length) % list.length; render(); }
  document.querySelectorAll('.pv-gal').forEach(function (g) {
    var items = [].slice.call(g.querySelectorAll('.pv-it')), name = g.closest('.pv-ch').dataset.brand;
    items.forEach(function (b, k) { b.addEventListener('click', function () { open(items, k, name, b); }); });
  });
  var vids = [].slice.call(document.querySelectorAll('.pv-vid'));
  vids.forEach(function (b, k) { b.addEventListener('click', function () { open(vids, k, 'Video', b); }); });
  lb.querySelector('.prev').addEventListener('click', function () { go(-1); });
  lb.querySelector('.next').addEventListener('click', function () { go(1); });
  lb.querySelector('.pv-lb-x').addEventListener('click', function () { lb.close(); });
  lb.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
  var sx = null;
  stage.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
  stage.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 40) go(dx < 0 ? 1 : -1); sx = null; });
  lb.addEventListener('close', function () { stage.innerHTML = ''; document.body.style.overflow = ''; if (opener) opener.focus(); });
})();
