// Interactive parts of the NOW Amazon Creative Guide page.
// Values come from the Figma file (tokens, color systems, review notes).
(function () {
  var root = document.querySelector('.nowg');
  if (!root) return;
  var css = function (k, v) { root.style.setProperty(k, v); };
  var press = function (group, el) { group.forEach(function (b) { b.setAttribute('aria-pressed', b === el ? 'true' : 'false'); }); };
  var nav = document.querySelector('.nav');
  var setNav = function () { if (nav) document.documentElement.style.setProperty('--navh', nav.offsetHeight + 'px'); };
  setNav(); addEventListener('resize', setNav);

  // Color systems: background, text, CTA fill, CTA label, and the contrast note
  var systems = {
    purple: { n: 'Purple', bg: '--brand-purple', t: '--surface', cb: '--surface', ct: '--brand-purple', d: 'Brand purple background with white text and a white CTA.', r: 'White on purple: 13:1' },
    orange: { n: 'Orange', bg: '--brand-orange', t: '--surface', cb: '--surface', ct: '--brand-orange', d: 'Brand orange background. White text stays Black weight and very large, or switch to brand-purple text.', r: 'White on orange: 2.45:1, large only', w: 1 },
    green: { n: 'Green', bg: '--brand-green', t: '--surface', cb: '--surface', ct: '--brand-green', d: 'Brand green background. White text only at 24px and up, Black weight.', r: 'White on green: 2.95:1, large only', w: 1 },
    yellow: { n: 'Yellow', bg: '--brand-yellow', t: '--brand-purple', cb: '--brand-purple', ct: '--surface', d: 'Brand yellow background with brand-purple text and a purple CTA.', r: 'Purple on yellow: 9.8:1' },
    sky: { n: 'Sky', bg: '--campaign-sky-bg', t: '--campaign-sky-text', cb: '--campaign-sky-text', ct: '--surface', d: 'Campaign system 1. Red text for the tagline and large headlines only.', r: 'Red on sky: 3.9:1, large only', w: 1 },
    mint: { n: 'Mint', bg: '--campaign-mint-bg', t: '--campaign-mint-text', cb: '--campaign-mint-text', ct: '--surface', d: 'Campaign system 2. Deep teal text and CTA fill.', r: 'Teal on mint: 5.0:1' },
    lilac: { n: 'Lilac', bg: '--campaign-lilac-bg', t: '--campaign-lilac-text', cb: '--campaign-lilac-text', ct: '--surface', d: 'Campaign system 3. Blue text and CTA fill.', r: 'Blue on lilac: 5.0:1' },
    violet: { n: 'Violet', bg: '--campaign-violet-bg', t: '--campaign-violet-text', cb: '--campaign-violet-text', ct: '--campaign-violet-bg', d: 'Campaign system 4. Yellow text and CTA fill.', r: 'Yellow on violet: 4.8:1' }
  };
  var v = function (name) { return 'var(' + name + ')'; };
  var sysBtns = [].slice.call(document.querySelectorAll('.sys'));
  var ctaFlag = document.getElementById('cta-flag');
  function setSystem(key, btn) {
    var s = systems[key]; if (!s) return;
    css('--sys-bg', v(s.bg)); css('--sys-text', v(s.t)); css('--cta-bg', v(s.cb)); css('--cta-text', v(s.ct));
    document.getElementById('sys-name').textContent = s.n + ' system.';
    document.getElementById('sys-desc').textContent = s.d;
    var r = document.getElementById('sys-ratio'); r.textContent = s.r; r.className = 'ratio' + (s.w ? ' warn' : '');
    if (ctaFlag) ctaFlag.hidden = !(key === 'orange' || key === 'green');
    if (btn) press(sysBtns, btn);
  }
  sysBtns.forEach(function (b) { b.addEventListener('click', function () { setSystem(b.dataset.sys, b); }); });

  // Every-system banner wall
  var wall = document.getElementById('all-banners');
  if (wall) Object.keys(systems).forEach(function (k) {
    var s = systems[k], el = document.createElement('div');
    el.className = 'tb';
    el.setAttribute('role', 'img');
    el.setAttribute('aria-label', s.n + ' tagline banner');
    el.style.cssText = '--sys-bg:' + v(s.bg) + ';--sys-text:' + v(s.t) + ';--cta-bg:' + v(s.cb) + ';--cta-text:' + v(s.ct);
    el.innerHTML = '<div class="tag"><p>Quality Obsessed.</p><p>Priced Less.</p></div><span class="cta">Shop NOW</span><div class="bottle">Bottle</div>';
    wall.appendChild(el);
  });

  // Gradients: hero, section tab and quality strip change together
  var grads = {
    magenta: ['--grad-magenta-start', '--grad-magenta-end'],
    sky: ['--grad-blue-start', '--grad-blue-end', 'Sky'],
    lime: ['--grad-green-start', '--grad-green-end', 'Lime'],
    lavender: ['--grad-lavender-start', '--grad-lavender-end'],
    teal: ['--grad-teal-start', '--grad-teal-end', 'Teal']
  };
  var gBtns = [].slice.call(document.querySelectorAll('.grad'));
  var gFlag = document.getElementById('grad-flag');
  gBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var g = grads[b.dataset.g];
      css('--g-start', v(g[0])); css('--g-end', v(g[1]));
      gFlag.hidden = !g[2];
      if (g[2]) gFlag.textContent = 'Review note: the ' + g[2] + ' light stop cannot hold white text';
      press(gBtns, b);
    });
  });

  // Product colorways: chips, tags, callouts
  var cws = {
    purple: ['--purple-600', '--purple-100', '--purple-900', ''],
    orange: ['--orange-500', '--orange-100', '--orange-500', 'Review note: Orange tags fail contrast with white 13px text'],
    green: ['--green-500', '--green-100', '--green-500', 'Review note: Green tags fail contrast with white 13px text'],
    teal: ['--teal-500', '--teal-100', '--teal-500', 'Review note: Teal tags fail contrast, and Teal titles are 2.0:1 on white: do not use for text'],
    magenta: ['--magenta-500', '--magenta-100', '--magenta-500', '']
  };
  var cwBtns = [].slice.call(document.querySelectorAll('[data-cw]'));
  var cwFlag = document.getElementById('cw-flag');
  cwBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var c = cws[b.dataset.cw];
      css('--cw-500', v(c[0])); css('--cw-100', v(c[1])); css('--cw-title', v(c[2]));
      cwFlag.hidden = !c[3]; cwFlag.textContent = c[3];
      press(cwBtns, b);
    });
  });

  // Section tab bleed
  var bBtns = [].slice.call(document.querySelectorAll('[data-bleed]'));
  var bDemo = document.getElementById('bleed-demo');
  bBtns.forEach(function (b) {
    b.addEventListener('click', function () { bDemo.classList.toggle('right', b.dataset.bleed === 'right'); press(bBtns, b); });
  });

  // Color tokens, with click to copy
  var tokens = [
    ['Brand', [
      ['NOW-purple', '#340d8d', 'Official NOW brand purple. Headline ink on white; background for white text (13:1).'],
      ['NOW-orange', '#fd852e', 'Official brand orange system background. White on it is only 2.45:1: keep text Black weight and very large, or use brand-purple text.'],
      ['NOW-green', '#62a744', 'Official brand green system background. White on it 2.95:1: 24px+ Black only.'],
      ['NOW-yellow', '#f5e003', 'Official brand yellow system background. Text on it is brand-purple (9.8:1).']]],
    ['Surfaces', [
      ['surface', '#ffffff', 'Page and module ground; text on purple, orange and green systems; callout cards.'],
      ['surface-section', '#eff0f5', 'Cool light grey behind second-row A+ modules.'],
      ['surface-stage', '#d7d8d7', 'Light grey pedestal the bottles stand on in the hero.']]],
    ['Text', [
      ['ink', '#1a1a1a', 'Body copy, chip text and dosing notes (13:1 or better).'],
      ['ink-muted', '#555555', 'Diet badge labels, captions and disclaimers on surface (7.5:1).'],
      ['on-purple-soft', '#e3d8f6', 'Secondary text on purple-600 and purple-800.']]],
    ['Campaign systems', [
      ['campaign-sky-bg', '#e0f2ff', 'Campaign system 1 background. Pair only with campaign-sky-text.'],
      ['campaign-sky-text', '#e82218', 'Campaign system 1 text and CTA fill (3.9:1): tagline and large headline only.'],
      ['campaign-mint-bg', '#b6ffde', 'Campaign system 2 background. Pair only with campaign-mint-text.'],
      ['campaign-mint-text', '#007180', 'Campaign system 2 text and CTA fill (5.0:1).'],
      ['campaign-lilac-bg', '#f2c7ff', 'Campaign system 3 background. Pair only with campaign-lilac-text.'],
      ['campaign-lilac-text', '#1753aa', 'Campaign system 3 text and CTA fill (5.0:1).'],
      ['campaign-violet-bg', '#6357d1', 'Campaign system 4 background. Pair only with campaign-violet-text.'],
      ['campaign-violet-text', '#f7f700', 'Campaign system 4 text and CTA fill (4.8:1).']]],
    ['Gradient stops', [
      ['grad-magenta-start', '#d72887', 'Magenta gradient, light stop.'],
      ['grad-magenta-end', '#96285d', 'Magenta gradient, dark stop. White 7.6:1.'],
      ['grad-blue-start', '#5eb9e1', 'Sky gradient, light stop. White 2.2:1: no text here.'],
      ['grad-blue-end', '#2a96c4', 'Sky gradient, dark stop. White 3.4:1: large bold only.'],
      ['grad-green-start', '#b4d03d', 'Lime gradient, light stop. White 1.75:1: never text.'],
      ['grad-green-end', '#007133', 'Lime gradient, dark stop. White 6.2:1.'],
      ['grad-lavender-start', '#8973d8', 'Lavender gradient, light stop. White 3.8:1: large bold only.'],
      ['grad-lavender-end', '#6f53bc', 'Lavender gradient, dark stop. White 5.8:1.'],
      ['grad-teal-start', '#87c4c1', 'Teal gradient, light stop. White 2.0:1: fills only.'],
      ['grad-teal-end', '#408589', 'Teal gradient, dark stop. White 4.3:1: large or bold.']]],
    ['Purple scale', [
      ['purple-900 → brand-purple', '#340d8d', 'Headline ink on white. Alias of brand-purple.'],
      ['purple-800', '#411f98', 'Deep band purple: bottom of hero gradient. White 11:1.'],
      ['purple-600', '#633dad', 'Top of hero gradient, diet badge discs. White 7.5:1.'],
      ['purple-300', '#7d63af', 'Lavender wash in quality module. White bold 4.9:1.'],
      ['purple-100', '#ece7f6', 'Lavender tint for quiet fills on white.']]],
    ['Product colorways', [
      ['orange-500 → brand-orange', '#fd852e', 'Orange product colorway: tiles, tags, tabs, discs.'],
      ['orange-100', '#fdd8bb', 'Orange colorway benefit chips, ink text.'],
      ['green-500 → brand-green', '#62a744', 'Green product colorway: tiles, tags, proof panel.'],
      ['green-100', '#d4f7c3', 'Green colorway benefit chips, ink text.'],
      ['teal-500 → grad-teal-start', '#87c4c1', 'Teal product colorway: fills and tiles only (2.0:1 with white).'],
      ['teal-100', '#c1e8e3', 'Teal colorway benefit chips, ink text.'],
      ['magenta-500 → grad-magenta-start', '#d72887', 'Magenta product colorway: tiles, tags, callout titles (4.6:1 on white).'],
      ['magenta-100', '#fddbed', 'Magenta colorway benefit chips, ink text.']]]
  ];
  var toast = document.getElementById('toast'), tt;
  function say(msg) { toast.textContent = msg; toast.classList.add('show'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('show'); }, 1600); }
  function copy(hex) {
    var done = function () { say('Copied ' + hex); };
    if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(hex).then(done, function () { say(hex); }); }
    else {
      var t = document.createElement('textarea'); t.value = hex; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); done(); } catch (e) { say(hex); }
      t.remove();
    }
  }
  var host = document.getElementById('swatches');
  if (host) tokens.forEach(function (g) {
    var wrap = document.createElement('div'); wrap.className = 'sw-group';
    var h = document.createElement('h3'); h.textContent = g[0]; wrap.appendChild(h);
    var grid = document.createElement('div'); grid.className = 'swatches-g';
    g[1].forEach(function (s) {
      var b = document.createElement('button'); b.className = 'sw-btn'; b.type = 'button';
      b.setAttribute('aria-label', 'Copy ' + s[0] + ' ' + s[1]);
      b.innerHTML = '<div class="chip" style="background:' + s[1] + '"></div><div class="n"></div><div class="h"></div><div class="d"></div>';
      b.querySelector('.n').textContent = s[0]; b.querySelector('.h').textContent = s[1]; b.querySelector('.d').textContent = s[2];
      b.addEventListener('click', function () { copy(s[1]); });
      grid.appendChild(b);
    });
    wrap.appendChild(grid); host.appendChild(wrap);
  });

  // A+ template anatomy
  var mods = {
    brand: ['Shared module', 'From the brand', 'The Brand Story module that opens the page and is shared across listings.', ['Headline and subhead', 'Logo card with the company story', 'The NOW Difference list with an accent rule']],
    m1: ['Premium full image', 'M1 · Hero, full image', 'Swapped per product: the logo on dark, product name, strength and pack count, with the product image on a stage.', ['Logo on dark', 'Two-weight headline and pack count', 'Body line and Spec Pills', 'Product image on the surface-stage pedestal']],
    m2: ['Background image with text', 'M2 · Value, background + text', 'Explains the value of the multipack: a text card on one side and three stat columns on the other.', ['Product Tag and Section Heading', 'Body copy in a white card', 'Three Stat Columns']],
    m3: ['Four images and text', 'M3 · Four images + text', 'Product highlights: a centered headline over four photo tiles, each with a short title and line of copy.', ['Centered two-weight headline', 'Four Highlight Tiles', 'Photo Placeholders until approved photography is in']],
    m4: ['Shared module', 'M4 · Quality, full image', 'NOW\'s quality and testing story, shared across the set.', ['Brand Line tagline', 'Quality copy and certification marks', 'Approved lab photography only']],
    m5: ['Comparison table', 'M5 · Comparison table', 'More multipacks: this item first, then the rest of the line, compared row by row.', ['Six Product Columns, current item highlighted', 'Comparison Rows: bottles in pack, per bottle, total, key amount, highlight']],
    fda: ['Required', 'Footer · FDA disclaimer', 'Every page that carries an asterisked claim ends with the FDA disclaimer.', ['Disclaimer component, Text/fine style']]
  };
  var mBtns = [].slice.call(document.querySelectorAll('[data-m]'));
  function showMod(key, b) {
    var m = mods[key];
    document.getElementById('mi-k').textContent = m[0];
    document.getElementById('mi-h').textContent = m[1];
    document.getElementById('mi-p').textContent = m[2];
    var ul = document.getElementById('mi-l'); ul.innerHTML = '';
    m[3].forEach(function (t) { var li = document.createElement('li'); li.textContent = t; ul.appendChild(li); });
    press(mBtns, b);
  }
  mBtns.forEach(function (b) { b.addEventListener('click', function () { showMod(b.dataset.m, b); }); });
  if (mBtns[0]) showMod('brand', mBtns[0]);

  // Section tabs: highlight the section in view
  var links = [].slice.call(document.querySelectorAll('.g-tabs a'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute('href') === '#' + e.target.id;
          a.classList.toggle('on', on);
          if (on) { a.setAttribute('aria-current', 'true'); var bar = a.parentNode; bar.scrollTo({ left: a.offsetLeft - 20, behavior: 'smooth' }); }
          else a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    links.forEach(function (a) { var s = document.querySelector(a.getAttribute('href')); if (s) io.observe(s); });
  }
})();
