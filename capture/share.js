// Builds the 1200x630 share images (site/images/og-*.jpg) and the PNG icons
// from the existing screenshots and favicon.svg.
// Usage: node capture/share.js   (needs Playwright with Chromium, and internet for Google Fonts)
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const site = path.resolve(__dirname, '../site');
const out = path.resolve(__dirname, 'out');
fs.mkdirSync(out, { recursive: true });
const img = f => 'file://' + path.join(site, 'images', f);

const base = (accent, body) => `<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;overflow:hidden;background:#0D1015;color:#EDF1F7;font-family:Inter,sans-serif;position:relative}
.glow{position:absolute;width:760px;height:760px;right:-180px;top:-120px;background:radial-gradient(closest-side,${accent}33,transparent);}
.txt{position:absolute;left:72px;top:72px;bottom:72px;width:520px;display:flex;flex-direction:column}
.logo{font:700 22px 'Space Grotesk';letter-spacing:.12em}
.eb{margin-top:auto;font:600 17px Inter;letter-spacing:.14em;text-transform:uppercase;color:${accent}}
h1{font:700 84px/.95 'Space Grotesk';letter-spacing:-.03em;margin:18px 0 22px}
p{font:400 24px/1.4 Inter;color:#93A0B4}
.bar{position:absolute;left:0;right:0;bottom:0;height:8px;background:${accent}}
.ph{position:absolute;width:250px;border-radius:30px;overflow:hidden;border:1px solid #2A3340;box-shadow:0 30px 60px -10px rgba(0,0,0,.7)}
.ph img{width:100%;display:block}
.fr{position:absolute;border-radius:16px;overflow:hidden;border:1px solid #2A3340;box-shadow:0 30px 60px -10px rgba(0,0,0,.7)}
.fr img{display:block;width:100%}
</style></head><body><div class="glow"></div>${body}<div class="bar"></div></body></html>`;

const cards = {
  'og-home': base('#FF6B3D', `
    <div class="txt"><div class="logo">TIMIMBO</div><div class="eb">Product design + AI</div>
    <h1>Ideas,<br>shipped.</h1><p>Case studies by Tim Imbordino</p></div>
    <div class="fr" style="width:620px;left:660px;top:90px"><img src="${img('bf-editor.jpg')}"></div>
    <div class="ph" style="left:600px;top:230px;width:230px"><img src="${img('mm-session.jpg')}"></div>`),
  'og-muscle-memory': base('#FF6B3D', `
    <div class="txt"><div class="logo">TIMIMBO</div><div class="eb">Case study 01</div>
    <h1>Muscle<br>Memory</h1><p>A strength training app and gym platform, shipped solo with AI.</p></div>
    <div class="ph" style="left:640px;top:110px"><img src="${img('mm-workouts.jpg')}"></div>
    <div class="ph" style="left:905px;top:60px"><img src="${img('mm-session.jpg')}"></div>`),
  'og-bannerfactory': base('#9B87FF', `
    <div class="txt" style="width:540px"><div class="logo">TIMIMBO</div><div class="eb">Case study 02</div>
    <h1 style="font-size:68px">BannerFactory</h1><p>One upload in, 16 on-brand<br>banner sizes out.</p></div>
    <div class="fr" style="width:640px;left:640px;top:130px"><img src="${img('bf-checks.jpg')}"></div>`),
};

(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
  for (const [name, html] of Object.entries(cards)) {
    const f = path.join(out, name + '.html');
    fs.writeFileSync(f, html);
    await pg.goto('file://' + f, { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    await pg.screenshot({ path: path.join(site, 'images', name + '.jpg'), type: 'jpeg', quality: 86 });
    console.log('wrote', name);
  }
  // NOW Creative Guide: render the real page cover over http (the logo masks need it)
  const http = require('node:http');
  const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.png': 'image/png' };
  const server = http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
    const f = path.join(site, p);
    if (!fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
  }).listen(8107);
  await pg.goto('http://localhost:8107/now-creative-guide/', { waitUntil: 'networkidle' });
  await pg.addStyleTag({ content: '.nav,.g-meta,.skip{display:none!important}.nowg .gw{max-width:none!important}.nowg .g-cover{min-height:630px!important;height:630px;padding:64px 80px 72px!important;justify-content:space-between}.g-cover .t{font-size:100px!important;margin:0 0 20px!important}body::after{content:"";position:fixed;left:0;right:0;top:622px;height:8px;background:#fd852e}' });
  await pg.evaluate(() => document.fonts.ready);
  await pg.screenshot({ path: path.join(site, 'images', 'og-now-creative-guide.jpg'), type: 'jpeg', quality: 88 });
  console.log('wrote og-now-creative-guide');
  server.close();

  const svg = 'file://' + path.join(site, 'favicon.svg');
  for (const [name, size] of [['favicon-32.png', 32], ['apple-touch-icon.png', 180]]) {
    await pg.setViewportSize({ width: size, height: size });
    fs.writeFileSync(path.join(out, 'icon.html'), `<body style="margin:0;background:#0D1015"><img src="${svg}" style="width:${size}px;height:${size}px;display:block"></body>`);
    await pg.goto('file://' + path.join(out, 'icon.html'));
    await pg.screenshot({ path: path.join(site, name), omitBackground: name.startsWith('favicon') });
    console.log('wrote', name);
  }
  await b.close();
})();
