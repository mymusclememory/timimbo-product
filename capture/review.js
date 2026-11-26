// Renders every page at 1440, 1024, 390 and 375 wide and reports sideways overflow.
// Usage: node capture/review.js [outdir]   (serves site/ on localhost:8105; runs with reduced motion so nothing is mid-fade)
const { chromium } = require('playwright');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../site');
const out = process.argv[2] || path.resolve(root, '../capture/out');
fs.mkdirSync(out, { recursive: true });
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const f = path.join(root, p);
  if (!fs.existsSync(f)) { res.writeHead(404, { 'content-type': 'text/html' }); return res.end(fs.readFileSync(path.join(root, '404.html'), 'utf8')); }
  res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
}).listen(8105);
const pages = [['', 'home'], ['muscle-memory/', 'mm'], ['bannerfactory/', 'bf'], ['now-creative-guide/', 'now'], ['photo-video/', 'pv'], ['design/', 'design'], ['now-31000/', 'n31'], ['nope/', '404']];
(async () => {
const b = await chromium.launch();
for (const w of [1440, 1024, 390, 375]) {
  const ctx = await b.newContext({ viewport: { width: w, height: 900 }, reducedMotion: 'reduce' });
  const pg = await ctx.newPage();
  for (const [p, n] of pages) {
    if (n === '404' && !fs.existsSync(path.join(root, '404.html'))) continue;
    await pg.goto('http://localhost:8105/' + p, { waitUntil: 'networkidle' });
    await pg.evaluate(async () => { document.querySelectorAll('img[loading]').forEach(i => i.loading = 'eager'); for (let y = 0; y < document.body.scrollHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
    await pg.waitForTimeout(900);
    const over = await pg.evaluate(() => [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1).slice(0, 5).map(e => e.tagName + '.' + e.className));
    const sw = await pg.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    await pg.screenshot({ path: `${out}/${n}_${w}.png`, fullPage: true });
    console.log(w, n, sw > 0 ? 'OVERFLOW ' + sw + 'px ' + over.join(' ') : 'ok');
  }
  await ctx.close();
}
await b.close(); server.close();
})();
