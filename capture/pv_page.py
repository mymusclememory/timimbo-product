# Builds site/photo-video/index.html from the project data below.
# Images live in site/images/pv/ (<key>-NN.jpg at 1600px and -800.jpg for the grid).
# Run: python3 capture/pv_page.py   (sizes come from capture/pv-dims.json)
import json, html, os
ROOT = os.path.dirname(os.path.abspath(__file__))
DIMS = json.load(open(os.path.join(ROOT, 'pv-dims.json')))
E = html.escape

CHAPTERS = [
 dict(key='experts', brand='NOW', title='Be You NOW', kind='Campaign photography', url='https://www.timimbo.com/now-experts',
  body="NOW's latest campaign uses bold imagery across platforms to build awareness and drive conversions. Each shot inspires confidence and authenticity, supported by trusted female voices in health and wellness sharing motivation, encouragement, and curated products to keep you focused, energized, and unstoppable.",
  people='Featuring Gabby Thomas (5x Olympic medalist), Peloton instructors Kristin McGee and Emma Lovewell, and registered dietitian DJ Blatner.',
  lead=6,
  alts=['Gabby Thomas running on a red track, seen from above','Gabby Thomas seated in a cream cardigan for an interview','A wellness expert in a color-block sweater seated in a green armchair','DJ Blatner seated on a leather sofa in a striped shirt','A wellness expert in a blue leather jacket on a teal sofa by city windows','Gabby Thomas, hands on hips, against a blue sky','A woman in a cream top opening a supplement at home','A woman relaxing on a sofa in cozy slippers with a mug','A woman in headphones smiling in a colorful room full of books','A woman in an orange set holding a supplement','A woman in a pink cardigan scooping NOW powder into an orange NOW bottle','A jar of NOW Slender Hot Cocoa beside a kettle on a kitchen counter','Gabby Thomas in red pajamas holding a mug in her kitchen','A fitness instructor in a retro purple and teal tracksuit dancing in front of a neon sign','A woman in a kitchen opening a supplement bottle','Hands opening NOW Omega-3 fish oil gummy chews beside other NOW products','A woman in a yoga boat pose in a bright living room','A woman doing a kettlebell squat in a home gym','Gabby Thomas standing on a running track, hands on hips','Hands scooping NOW Organic Pea Protein into a shaker','NOW Monk Fruit and oil beside a bowl of popcorn on a dark surface','A woman in a floral blouse in her kitchen with a tray of baked bars','A woman in a pink sweater opening a NOW supplement at a counter','A hand setting a shaker beside a tub of NOW Organic Pea Protein','NOW Slender Sticks pomegranate berry box with glasses of red drink','A woman stretching in a home gym','A woman with a mug curled up in a white chair','Gabby Thomas leaning back on the grass, taking a supplement under a blue sky','A nursery dresser with a basket of NOW baby care products']),
 dict(key='solutions', brand='NOW Solutions', title='NOW Solutions', kind='Photography + video', url='https://www.timimbo.com/now-solutions',
  body="NOW Solutions, a leader in personal care and essential oils, needed assets that aligned with their brand standards while pushing creative boundaries. The project combined photography and video tailored for both e-commerce, print, and social media, with visuals that emphasized purity, quality, and wellness. By unifying content across digital platforms, the imagery reinforced brand consistency while introducing fresh, engaging ways to connect with their audience.",
  lead=2,
  alts=['An open jar of extra strength balm with its lid on grey stone','NOW Solutions vitamin C lotion and gel cleanser with orange slices on an orange background','NOW Solutions coffee oil lying on coffee beans against a tan background','NOW Solutions rose facial mist on a white ledge against a pink wall','A set of NOW Solutions skin care and essential oils on a peach background with palm leaves','An open jar of golden balm on grey stone, seen from above','A swipe of golden balm texture on grey stone','A close-up of white cream texture','NOW Solutions blemish clear skin care bottles with monstera leaves','NOW Solutions coffee oil falling into coffee beans']),
 dict(key='citrus', brand='True Citrus', title='True Citrus', kind='Product + lifestyle photography', url='https://www.timimbo.com/true-citrus',
  body="True Citrus needed photography that captured both product clarity and real-life moments. The direction focused on authentic interactions with friends and family, paired with styled product shots that highlighted freshness and flavor. The result was imagery that evoked joy, reinforced the brand's bright identity, and connected naturally with consumers.",
  lead=4,
  alts=['True Lime and True Lemon drink mixes on grass beside a bowl of citrus, with a hand lifting a glass','True Lemon Kids drink mix and pink lemonade on a camp table, with a mother and child on a tree swing behind','True Lemon mango lemonade box and stick pack with a glass on an orange background','True Lemon lemon lime lemonade box and stick pack with limes and lemons on a wooden board','A woman in a mustard sweater sitting by a window with a glass of True Lemon','True Lemon lemon lime and mango lemonade boxes with lemons and stick packs on orange','True Lemon lemon lime lemonade box and glass on a white tiled kitchen counter','A young boy sipping True Lemon lemonade through a straw','A hand holding a True Lemon raspberry lemonade box over grass with a glass','True Lemon lemon lime and mango lemonade boxes with glasses and lemons on a yellow background','A man in his kitchen holding a glass of lemonade beside a True Lemon box','A woman playfully holding True Lemon stick packs in her mouth','A mother and son laughing on a couch with True Lemon Kids drink mix and juice on the table','True Lemon lemon lime and mango boxes with stick packs on a yellow background','A man on a sofa holding a glass, with a True Lemon box on the side table','A man at a table pouring a True Citrus stick pack into a bottle beside a gym bag','A hand dropping a True Lemon wildberry stick pack beside its box in a white kitchen']),
 dict(key='nuzest', brand='Nuzest', title='Nuzest', kind='UGC-style photography', url='https://www.timimbo.com/nuzest-plant-protein',
  body="Nuzest launched a new plant-based protein and needed visuals that felt authentic to health-conscious consumers. The creative direction centered on UGC-style photography that placed the product in real-life settings, approachable, relatable, and lifestyle driven. Designed for both eCommerce and social media, the imagery highlighted the protein's quality and versatility while providing a cohesive content set to support a seamless, impactful launch across digital platforms.",
  lead=1,
  alts=['A couple in a kitchen looking at a bag of Nuzest Protein plus Probiotics','A Nuzest shaker held over weight plates beside a Protein Greens plus Berries bag','A hand holding a bag of Nuzest Protein Greens plus Berries next to a Nuzest shaker','A woman in a kitchen holding Nuzest Protein plus Probiotics beside a tray of fruit','A hand placing Nuzest Protein plus Probiotics into a gym bag','A hand lifting a Nuzest Greens plus Berries bag beside weights and a shaker','A man by weight plates with a Nuzest shaker and Greens plus Berries bag','A woman holding a Nuzest Protein plus Probiotics pouch by a tray of fruit','Nuzest Protein plus Probiotics and Greens plus Berries bags on a counter with a shaker','A man holding an open bag of Nuzest Greens plus Berries beside a shaker and weights','A hand holding a Nuzest shaker beside a Protein plus Probiotics bag','Both Nuzest protein bags on a counter while a man drinks from a shaker behind them']),
 dict(key='n2', brand='N2 Water', title='N2 Water', kind='Photography + social video', url='https://www.timimbo.com/n2-water',
  body="N2 Water launched with a need for content that highlighted both lifestyle energy and science-backed hydration. The project combined product photography, authentic lifestyle imagery, and social media video content to connect with active consumers. Designed for eCommerce, digital, and campaign use, the visuals reinforced N2 Water's position as a functional hydration brand.",
  lead=1,
  alts=['A pickleball paddle, ball, water bottle and N2 Water stick pack on a court','A hand pouring an N2 Water stick pack into a bottle on a kitchen counter beside the pouch and oranges','A runner with an N2 Water pouch and bottle on a table as a group stretches behind','A pickleball player tearing open an N2 Water stick pack courtside','A pickleball player kneeling on court to pour N2 Water into a bottle','A hand pulling an N2 Water stick pack from a leather bag','Three N2 Water pouches in different flavors on a kitchen counter','An N2 Water pouch and bottle by the net of a pickleball court','Two players passing an N2 Water stick pack over the net','A runner reaching into a bag beside an N2 Water pouch on the grass after a group run','A pickleball player handing an N2 Water stick pack across the net','A hand holding an N2 Water stick pack over a bottle courtside','An N2 Water bottle and stick pack on court with a player in the background','A runner holding an N2 Water stick pack as a group jogs past','An N2 Water pouch and bottle on the grass with runners resting behind','Many hands reaching for N2 Water stick packs on a wooden table','A hand taking an N2 Water stick pack from a bag on a wooden table','A hand holding an N2 Water stick pack as runners pass on a trail']),
 dict(key='more', brand='Selected work', title='More product work', kind='Product photography', url='https://www.timimbo.com',
  body='Studio product photography for health, beauty and food brands.',
  lead=1,
  alts=['Viviscal dry shampoo held between two hands against pink hexagon tile','A hand pumping Viviscal Pro thickening serum','A jar of NOW Prebiotic Inulin Fiber beside a mug on a yellow background','A hot sauce bottle on a yellow plate between two chili peppers against red','An athlete sitting in a stairwell holding a tub of NOW protein']),
]
# Product launch videos, shown in their own "Product videos" grid inside the Video chapter.
# Titles are read from each video's poster (YouTube itself was not reachable when they were added).
PRODUCT_VIDEOS = [
 ('w8LtNlhoau4', 'NOW', 'Vitamin C + Vitamin D3 Gummies', '', 'h'),
 ('Ex-tXA6bGJ4', 'NOW Solutions', 'niteZen Magnesium Body Cream', '', 'h'),
 ('V3jGuraciMI', 'NOW', 'Omega-3 Fish Oil Gummy Chews', '', 'h'),
 ('J8kJ8xOyRWw', 'NOW Solutions', 'Vitamin C Skincare', '', 'h'),
]
VIDEOS = [
 ('Y_XiM882eto', 'NOW', 'Founder tribute', '', 'h', 'AI-generated artwork, voiceover and animated archival photos, for an internal marketing piece honoring NOW\'s founder.'),
 ('O3nR7xAuR7c', 'NOW', 'From Supplements to Self-Care: Discover the NOW Way to Wellness', '0:37', 'h'),
 ('7ki-vWagUd0', 'Worry Free', '30% Vinegar Concentrate, product launch 1', '0:37', 'h'),
 ('-4F3riQobr8', 'Worry Free', '30% Vinegar Concentrate, product launch 2', '0:31', 'h'),
 ('nq0nr6Nl0Ls', 'Kenyon', 'Electric Grills: Urban Grilling Revolution', '0:36', 'v'),
 ('OEJFHi18imU', 'Zend', 'Skincare lifestyle and brand integration', '0:31', 'v'),
 ('9Fb7opBFwTA', 'FINEX', 'Cast Iron social content', '0:25', 'v'),
 ('Ec_zU0zestc', 'Current', 'Backyard Electric Grill', '0:55', 'v'),
 ('L6PvUrEssGQ', 'Whey Matcha', 'Product introduction', '0:14', 'v'),
 ('wix-b15e', 'NOW Solutions', 'Skin Cleanser Instagram reel', '0:15', 'v'),
]
WIX_MP4 = 'https://video.wixstatic.com/video/49ec46_b15e3251211a4762b1f31c288022cd45/720p/mp4/file.mp4'

def chapter(c, n):
    k = c['key']; items = []
    for i, alt in enumerate(c['alts'], 1):
        name = f'{k}-{i:02d}'; w, h = DIMS[name]
        cls = 'pv-it' + (' lead' if i == c['lead'] else '')
        items.append(f'<button type="button" class="{cls}" data-full="../images/pv/{name}.jpg" data-alt="{E(alt)}" aria-label="Open image: {E(alt)}">'
                     f'<img src="../images/pv/{name}-800.jpg" srcset="../images/pv/{name}-800.jpg 800w, ../images/pv/{name}.jpg 1600w" sizes="(max-width:700px) 46vw, (max-width:1100px) 34vw, 360px" width="{w}" height="{h}" alt="{E(alt)}" loading="lazy" decoding="async"></button>')
    lead = next(i for i in items if ' lead' in i)
    rest = [i for i in items if i is not lead]
    people = f'<p class="pv-people">{E(c["people"])}</p>' if c.get('people') else ''
    link = f'<a class="pv-src" href="{c["url"]}" target="_blank" rel="noopener">View on timimbo.com ↗</a>' if c['key'] != 'more' else ''
    return f'''<section class="pv-ch" id="{k}" data-brand="{E(c['title'])}" aria-labelledby="{k}-h">
<div class="wrap pv-ch-in">
<header class="pv-ch-head">
<p class="pv-num">{n:02d}<span>/{len(CHAPTERS)+1:02d}</span></p>
<p class="pv-brand">{E(c['brand'])}</p>
<h2 id="{k}-h">{E(c['title'])}</h2>
<p class="pv-kind">{E(c['kind'])} · {len(items)} images</p>
<p class="pv-body">{E(c['body'])}</p>
{people}
{link}
</header>
<div class="pv-gal" data-set="{k}">
{lead}
<div class="pv-cols">
{chr(10).join(rest)}
</div>
</div>
</div>
</section>'''

def video_cards(items):
    cards = []
    for vid, brand, title, dur, o, *note in items:
        w, h = DIMS['video-' + vid]
        src = WIX_MP4 if vid.startswith('wix') else f'https://www.youtube-nocookie.com/embed/{vid}?autoplay=1&rel=0&playsinline=1'
        typ = 'mp4' if vid.startswith('wix') else 'yt'
        cards.append(f'''<button type="button" class="pv-vid {o}" data-video="{src}" data-type="{typ}" data-alt="{E(brand + ': ' + title)}" aria-label="Play video: {E(brand + ', ' + title)}">
<span class="pv-poster"><img src="../images/pv/video-{vid}.jpg" width="{w}" height="{h}" alt="" loading="lazy" decoding="async"><span class="pv-play" aria-hidden="true"></span>{f'<span class="pv-dur">{dur}</span>' if dur else ''}</span>
<span class="pv-vt"><b>{E(brand)}</b> {E(title)}{f'<span class="pv-note">{E(note[0])}</span>' if note else ''}</span>
</button>''')
    return cards

def videos(n):
    cards = video_cards(VIDEOS)
    prod = video_cards(PRODUCT_VIDEOS)
    return f'''<section class="pv-ch pv-video" id="video" data-brand="Video" aria-labelledby="video-h">
<div class="wrap">
<header class="pv-vhead">
<div><p class="pv-num">{n:02d}<span>/{n:02d}</span></p><p class="pv-brand">Film</p><h2 id="video-h">Video</h2></div>
<p class="pv-body">From concept to final cut, I manage every stage of your video project, capturing engaging footage, editing with precision, and adding animation that elevates your brand. Whether it's a product demo, lifestyle piece, or full campaign, the goal is simple: create video that looks great and communicates your message clearly.</p>
</header>
<div class="pv-vgrid">
{chr(10).join(cards)}
</div>
<div class="pv-sub" id="product-videos">
<header class="pv-subhead"><h3>Product videos</h3><p class="pv-body">Launch videos for new NOW and NOW Solutions products.</p></header>
<div class="pv-vgrid pv-prod">
{chr(10).join(prod)}
</div>
</div>
<a class="pv-src" href="https://www.timimbo.com/video" target="_blank" rel="noopener">All videos on timimbo.com ↗</a>
</div>
</section>'''

def index_rows():
    rows = []
    for n, c in enumerate(CHAPTERS, 1):
        prev = f"../images/pv/{c['key']}-{c['lead']:02d}-800.jpg"
        rows.append(f'<li><a href="#{c["key"]}" data-preview="{prev}"><span class="i-n">{n:02d}</span><span class="i-t">{E(c["title"])}</span><span class="i-k">{E(c["kind"])}</span><span class="i-c">{len(c["alts"])}</span></a></li>')
    rows.append(f'<li><a href="#video" data-preview="../images/pv/video-O3nR7xAuR7c.jpg"><span class="i-n">{len(CHAPTERS)+1:02d}</span><span class="i-t">Video</span><span class="i-k">Product films and social</span><span class="i-c">{len(VIDEOS)+len(PRODUCT_VIDEOS)}</span></a></li>')
    return '\n'.join(rows)

total = sum(len(c['alts']) for c in CHAPTERS)
chips = ''.join(f'<a href="#{c["key"]}">{E(c["title"])}</a>' for c in CHAPTERS) + '<a href="#video">Video</a>'
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Photography + Video | Tim Imbordino, TIMIMBO</title>
<meta name="description" content="Product, lifestyle and campaign photography and video for CPG and wellness brands by Tim Imbordino: NOW, NOW Solutions, True Citrus, Nuzest, N2 Water and more.">
<meta name="theme-color" content="#0D1015">
<link rel="canonical" href="https://work.timimbo.com/photo-video/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="TIMIMBO">
<meta property="og:url" content="https://work.timimbo.com/photo-video/">
<meta property="og:title" content="Photography + Video | TIMIMBO">
<meta property="og:description" content="Product, lifestyle and campaign photography and video for CPG and wellness brands.">
<meta property="og:image" content="https://work.timimbo.com/images/og-photo-video.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A grid of product and lifestyle photographs for CPG brands">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Photography + Video | TIMIMBO">
<meta name="twitter:description" content="Product, lifestyle and campaign photography and video for CPG and wellness brands.">
<meta name="twitter:image" content="https://work.timimbo.com/images/og-photo-video.jpg">
<meta name="twitter:image:alt" content="A grid of product and lifestyle photographs for CPG brands">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="icon" href="../favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css?v=20261126d">
<script src="../motion.js?v=20261126d" defer></script>
<script src="../pv.js?v=20261126d" defer></script>
</head>
<body class="ui-inter pv-page">
<a class="skip" href="#main">Skip to content</a>

<nav class="nav" aria-label="Main"><div class="wrap">
<a class="logo" href="https://timimbo.com" target="_top"><img src="../images/logo-timimbo-white.png" width="266" height="68" alt="timimbo creative"></a>
<div class="links">
<a href="../">Product</a>
<a href="../design/">Design</a>
<a class="on" href="./" aria-current="page">Photo + Video</a>
<a href="mailto:heytim@timimbo.com">Contact</a>
</div>
</div></nav>

<main id="main">
<header class="wrap pv-hero">
<p class="eb">Photography + video</p>
<h1 class="pv-h1">Real products.<br><span>Real moments.</span></h1>
<div class="pv-hero-foot">
<p class="pv-lede">Photography, video, and creative direction that bring a brand's story to life with authenticity and impact. Product, lifestyle and campaign work for CPG and wellness brands.</p>
<dl class="pv-stats"><div><dt>Projects</dt><dd>{len(CHAPTERS)-1}</dd></div><div><dt>Images</dt><dd>{total}</dd></div><div><dt>Films</dt><dd>{len(VIDEOS)+len(PRODUCT_VIDEOS)}</dd></div></dl>
</div>
<ol class="pv-index" aria-label="Projects">
{index_rows()}
</ol>
<img class="pv-peek" id="pv-peek" alt="" aria-hidden="true">
</header>

<nav class="pv-bar" aria-label="Projects"><div class="wrap"><div class="pv-chips">{chips}</div></div></nav>

{chr(10).join(chapter(c, n) for n, c in enumerate(CHAPTERS, 1))}
{videos(len(CHAPTERS)+1)}

<section class="pv-end"><div class="wrap">
<p class="eb">Next shoot</p>
<h2>Have a product that deserves better pictures?</h2>
<div class="pv-end-row"><a class="btn" href="mailto:heytim@timimbo.com">Let's talk</a><a class="pv-src" href="https://www.timimbo.com" target="_blank" rel="noopener">Book on timimbo.com ↗</a></div>
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
out = os.path.join(ROOT, '..', 'site', 'photo-video', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(page)
print('wrote', out, total, 'images', len(VIDEOS)+len(PRODUCT_VIDEOS), 'videos')
