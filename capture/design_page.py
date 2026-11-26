# Builds site/design/index.html from the project data below.
# Boards come from Tim's 2024 design PDF (Drive: timimbo_2024.pdf), one page per board,
# saved in site/images/design/<key>-NN.jpg (2000px) and -1000.jpg (grid), sizes in capture/design-dims.json.
# Run: python3 capture/design_page.py
import json, html, os
ROOT = os.path.dirname(os.path.abspath(__file__))
DIMS = json.load(open(os.path.join(ROOT, 'design-dims.json')))
E = html.escape

PROJECTS = [
 dict(key='jssi', client='Jet Support Services (JSSI)', title='JSSI', kind='Brand identity',
  role='Creative Direction / Design Development / UI / Photography',
  body='A full identity for an aircraft maintenance provider, carried through stationery, brochures, posters, a website and a mobile app.',
  alts=['JSSI brochure spread headed "Our expertise is your advantage", with letterhead, a timeline chart and a birthday card',
        'JSSI identity board: the Gotham typeface, a navy and grey palette, a 30 years mark and an hourglass brochure',
        'A JSSI "A better approach" poster in an airport lightbox, with matching flyers shot over forest and snow',
        'The JSSI website on desktop and tablet, a mobile app, and the style guide with colors and type']),
 dict(key='parsons', client='Parsons Corporation', title='Parsons', kind='Interactive proposal + brand marketing',
  role='Art Direction / Design Development / UI',
  body='Developed various brand marketing materials and interactive proposals to communicate company offerings and technologies.',
  link=('https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:29c17e93-fa90-49eb-afff-7d256093274a', 'View the presentation ↗'),
  alts=['A Parsons "Leading the way" trade show wall, values challenge coins and an orange capabilities brochure',
        'The Parsons interactive proposal on a tablet, with an airport infographic, world project map and project schedule']),
 dict(key='experts', client='NOW Wellness Experts', title='NOW Wellness Experts', kind='Identity for a national campaign',
  role='Creative Direction / Design Development / Video / Photography / Animation',
  body='The "you\'re enough NOW" campaign identity, carried across YouTube, web ads, a weekly wellness calendar and campaign photography.',
  link=('../photo-video/#experts', 'See the campaign photography →'),
  video=('E7w91FyGqnc', 'NOW Wellness Experts', 'You\'re Enough NOW'),
  alts=['Campaign portraits of two NOW wellness experts at home, with NOW products in a kitchen',
        'The NOW Wellness Experts video on YouTube, web ads, and a May 2023 wellness calendar on a phone']),
 dict(key='optimum', client='Optimum Nutrition', title='Optimum Nutrition', kind='Campaign',
  role='Digital Art Director / Design Lead',
  body='Create a viral campaign that engages a wide range of fitness enthusiasts backed by honest ingredients and social influencers.',
  video=('1Q7TY1bTGJA', 'Optimum Nutrition', 'Campaign video'),
  alts=['The Optimum Nutrition website with a Gold Standard Whey contest, a Team ON banner stand, PRO packaging and a print ad',
        'A Platinum PRE- magazine ad, the product on yellow, an icon and dosage chart, and the video on a tablet',
        'An Olympia 2013 VIP pass web page and social posts promoting the Optimum Nutrition booth']),
 dict(key='studio', client='timimbo | designs', title='Studio work', kind='Identity, print + packaging',
  role='Lead creative design',
  body='Lead creative design to help businesses with corporate identity, print, digital media, packaging, video editing, and web development.',
  alts=['A Winning Together logo, a coffee equipment catalog, a report spread and Single Barrel whole bean coffee packaging',
        'SweetRight sell sheets, JustSweet allulose sweetener boxes, nutrition supplement tubs and a pouch, and social posts on phones']),
]

def board(key, i, alt, lead):
    name = f'{key}-{i:02d}'; w, h = DIMS[name]
    return (f'<button type="button" class="pv-it{" lead" if lead else ""}" data-full="../images/design/{name}.jpg" data-alt="{E(alt)}" aria-label="Open board: {E(alt)}">'
            f'<img src="../images/design/{name}-1000.jpg" srcset="../images/design/{name}-1000.jpg 1000w, ../images/design/{name}.jpg 2000w" sizes="(max-width:900px) 92vw, 780px" width="{w}" height="{h}" alt="{E(alt)}" loading="lazy" decoding="async"></button>')

def project(p, n):
    k = p['key']
    boards = '\n'.join(board(k, i, a, i == 1) for i, a in enumerate(p['alts'], 1))
    link = f'<a class="pv-src" href="{p["link"][0]}"{" target=\"_blank\" rel=\"noopener\"" if p["link"][0].startswith("http") else ""}>{E(p["link"][1])}</a>' if p.get('link') else ''
    vid = ''
    if p.get('video'):
        v, brand, title = p['video']
        vid = f'''<button type="button" class="pv-vid h ds-vid" data-video="https://www.youtube-nocookie.com/embed/{v}?autoplay=1&amp;rel=0&amp;playsinline=1" data-type="yt" data-alt="{E(brand + ': ' + title)}" aria-label="Play video: {E(brand + ', ' + title)}">
<span class="pv-poster"><img src="../images/design/video-{v}.jpg" width="{960 if v == 'E7w91FyGqnc' else 640}" height="{540 if v == 'E7w91FyGqnc' else 360}" alt="" loading="lazy" decoding="async"><span class="pv-play" aria-hidden="true"></span></span>
<span class="pv-vt"><b>Video</b> {E(title)}</span>
</button>'''
    count = f'{len(p["alts"])} board{"s" if len(p["alts"]) > 1 else ""}' + (' · 1 video' if vid else '')
    return f'''<section class="pv-ch ds-ch" id="{k}" data-brand="{E(p['title'])}" aria-labelledby="{k}-h">
<div class="wrap pv-ch-in">
<header class="pv-ch-head">
<p class="pv-num">{n:02d}<span>/{len(PROJECTS):02d}</span></p>
<p class="pv-brand">{E(p['client'])}</p>
<h2 id="{k}-h">{E(p['title'])}</h2>
<p class="pv-kind">{E(p['kind'])} · {count}</p>
<p class="pv-body">{E(p['body'])}</p>
<dl class="ds-role"><dt>Role</dt><dd>{E(p['role'])}</dd></dl>
{link}
</header>
<div class="pv-gal ds-gal" data-set="{k}">
{boards}
{vid}
</div>
</div>
</section>'''

def index_rows():
    return '\n'.join(f'<li><a href="#{p["key"]}" data-preview="../images/design/{p["key"]}-01-1000.jpg"><span class="i-n">{n:02d}</span><span class="i-t">{E(p["title"])}</span><span class="i-k">{E(p["kind"])}</span><span class="i-c">{len(p["alts"])}</span></a></li>' for n, p in enumerate(PROJECTS, 1))

boards_total = sum(len(p['alts']) for p in PROJECTS)
videos_total = sum(1 for p in PROJECTS if p.get('video'))
chips = ''.join(f'<a href="#{p["key"]}">{E(p["title"])}</a>' for p in PROJECTS)
OG = 'A collage of brand identity, print and packaging design by Tim Imbordino'
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Graphic Design | Tim Imbordino, TIMIMBO</title>
<meta name="description" content="Brand identity, print, packaging and campaign design by Tim Imbordino for JSSI, Parsons, NOW, Optimum Nutrition and more.">
<meta name="theme-color" content="#0D1015">
<link rel="canonical" href="https://design.timimbo.com/design/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TIMIMBO">
<meta property="og:url" content="https://design.timimbo.com/design/">
<meta property="og:title" content="Graphic Design | TIMIMBO">
<meta property="og:description" content="Brand identity, print, packaging and campaign design.">
<meta property="og:image" content="https://design.timimbo.com/images/og-design.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Graphic Design | TIMIMBO">
<meta name="twitter:description" content="Brand identity, print, packaging and campaign design.">
<meta name="twitter:image" content="https://design.timimbo.com/images/og-design.jpg">
<meta name="twitter:image:alt" content="{OG}">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="icon" href="../favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css?v=20261126e">
<script src="../motion.js?v=20261126e" defer></script>
<script src="../pv.js?v=20261126e" defer></script>
</head>
<body class="ui-inter pv-page ds-page">
<a class="skip" href="#main">Skip to content</a>

<nav class="nav" aria-label="Main"><div class="wrap">
<a class="logo" href="https://timimbo.com" target="_top"><img src="../images/logo-timimbo-white.png" width="266" height="68" alt="timimbo creative"></a>
<div class="links">
<a href="../">Product</a>
<a class="on" href="./" aria-current="page">Design</a>
<a href="../photo-video/">Photo + Video</a>
<a href="mailto:heytim@timimbo.com">Contact</a>
</div>
</div></nav>

<main id="main">
<header class="wrap pv-hero">
<p class="eb">Graphic design</p>
<h1 class="pv-h1">Brand systems.<br><span>Built to perform.</span></h1>
<div class="pv-hero-foot">
<p class="pv-lede">Packaging refreshes, campaign identities and brand systems built to perform across e-commerce and retail. Identity, print, digital and packaging work for aviation, engineering and CPG brands.</p>
<dl class="pv-stats"><div><dt>Projects</dt><dd>{len(PROJECTS)}</dd></div><div><dt>Boards</dt><dd>{boards_total}</dd></div><div><dt>Films</dt><dd>{videos_total}</dd></div></dl>
</div>
<ol class="pv-index" aria-label="Projects">
{index_rows()}
</ol>
<img class="pv-peek" id="pv-peek" alt="" aria-hidden="true">
</header>

<nav class="pv-bar" aria-label="Projects"><div class="wrap"><div class="pv-chips">{chips}</div></div></nav>

{chr(10).join(project(p, n) for n, p in enumerate(PROJECTS, 1))}

<section class="ds-more" aria-labelledby="more-h"><div class="wrap">
<p class="eb">More design</p>
<h2 class="h2" id="more-h">See NOW work in depth.</h2>
<a class="ds-card" href="../now-creative-guide/">
<img src="../images/og-now-creative-guide-800.jpg" srcset="../images/og-now-creative-guide-800.jpg 800w, ../images/og-now-creative-guide.jpg 1200w" sizes="(max-width:700px) 92vw, 480px" width="1200" height="630" alt="NOW Amazon Creative Guide cover with the NOW logo" loading="lazy" decoding="async">
<span><b>NOW Amazon Creative Guide</b> The design system behind NOW's Amazon listings and A+ pages, rebuilt as an interactive guide. <i>Open the guide →</i></span>
</a>
<a class="ds-card" href="../now-31000/">
<img src="../images/og-now-31000-800.jpg" srcset="../images/og-now-31000-800.jpg 800w, ../images/og-now-31000.jpg 1200w" sizes="(max-width:700px) 92vw, 480px" width="1200" height="630" alt="A NOW promo film frame reading 31,000 Quality Tests Each Month over lab beakers of softgels" loading="lazy" decoding="async">
<span><b>NOW 31,000 Tests campaign</b> A Q4 campaign built on NOW's 31,000 quality tests each month: films, TV frames, holiday creative and a 166-asset system. <i>See the case study →</i></span>
</a>
</div></section>

<section class="pv-end"><div class="wrap">
<p class="eb">Next project</p>
<h2>Need a brand that holds together everywhere?</h2>
<div class="pv-end-row"><a class="btn" href="mailto:heytim@timimbo.com">Let's talk</a><a class="pv-src" href="https://www.timimbo.com" target="_blank" rel="noopener">More on timimbo.com ↗</a></div>
</div></section>
</main>

<footer><div class="wrap">
<span>© TIMIMBO LLC</span>
<a href="mailto:heytim@timimbo.com">heytim@timimbo.com</a>
</div></footer>

<dialog class="pv-lb" id="pv-lb" aria-label="Viewer">
<div class="pv-lb-top"><span id="pv-lb-cap"></span><span id="pv-lb-n"></span><button type="button" class="pv-lb-x" aria-label="Close">×</button></div>
<div class="pv-lb-stage" id="pv-lb-stage"></div>
<button type="button" class="pv-lb-nav prev" aria-label="Previous">‹</button>
<button type="button" class="pv-lb-nav next" aria-label="Next">›</button>
</dialog>
</body>
</html>
'''
out = os.path.join(ROOT, '..', 'site', 'design', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(page)
print('wrote', out, boards_total, 'boards', videos_total, 'videos')
