# TIMIMBO Product Portfolio - Working Agreement for Claude Code

## What this is

A static microsite of product design case studies for Tim Imbordino
(TIMIMBO LLC). It is hosted on Netlify and linked from timimbo.com (Wix).
Target address: a subdomain such as work.timimbo.com, set up with a CNAME
record in Wix DNS.

Pages:
- site/index.html: home, one card per case study, then a "CPG brand
  work" section (NOW Experts / Be You NOW, NOW Solutions, True Citrus,
  Nuzest, N2 Water). Tiles open a gallery dialog (site/cpg.js) and fall back to
  links to the matching timimbo.com page. Images in site/images/cpg/.
- site/muscle-memory/index.html: Muscle Memory + America's Gym
- site/bannerfactory/index.html: BannerFactory
- site/now-creative-guide/: NOW Amazon Creative Guide, an interactive
  rebuild of Tim's Figma design system. Its own light theme in Nunito
  (guide.css), its own script (guide.js) and the logo and icon SVGs
  exported from Figma (assets/).
- site/styles.css: one shared stylesheet. The BannerFactory page sets
  `<body class="bf">`, which switches the accent from ember to violet.
- site/images/: every visual on the site
- site/404.html: not-found page (Netlify serves it automatically)
- site/motion.js: a few lines that fade and rise sections in on
  scroll. It does nothing for visitors who ask for reduced motion.
  The other scripts are site/cpg.js (home page CPG gallery) and
  site/now-creative-guide/guide.js.
- site/favicon.svg, favicon-32.png, apple-touch-icon.png: icons
- site/images/og-*.jpg: 1200x630 share images (Open Graph and Twitter)

Plain HTML and CSS, plus motion.js, cpg.js and guide.js. No framework, no
build step.
netlify.toml publishes the `site` folder as-is.

## Page patterns

- Screenshot callouts: put the image in `<div class="phone">` or
  `<div class="frame">`, add `<span class="hot" style="--t;--l;--w;--h">`
  boxes (percent of the image) with a numbered `.pin`, and explain each
  number in `<ol class="notes">` below. Add class `r` to move the pin
  to the right corner. Hotspots are `aria-hidden`; the notes carry the
  meaning.
- Share tags point at https://work.timimbo.com. If the final domain
  changes, update canonical, og:url, og:image and twitter:image on
  every page.

## Rules

- Never use em dashes anywhere: copy, code comments, commit messages,
  or chat replies to Tim.
- Tim is a designer, not a developer. Report in short plain-language
  bullets, framed as what he needs to do next.
- No invented stats, results or quotes. A missing fact gets a visible
  [PLACEHOLDER] and gets flagged to Tim.
- Every image needs real alt text. Keep pages working at 375px wide with
  no sideways scrolling.
- Work on a branch, open a pull request, and give Tim the Netlify deploy
  preview link. Merges are Tim's call.

## Design tokens (borrowed from the Muscle Memory app)

- Background #0D1015, alt section #10141A, surface #161B22, raised
  #1D242E, line #2A3340
- Text #EDF1F7, muted #93A0B4, faint #7D899B (lightened from #5B6779 in
  Nov 2026 so small text passes 4.5:1 contrast)
- Ember #FF6B3D (Muscle Memory accent), glacier #43C6E8, green #5BD08B,
  gold #E8B843 (personal records only), violet #9B87FF (BannerFactory
  accent)
- Type: Space Grotesk headings, Inter body, Barlow Condensed for numbers
  and the Muscle Memory type sample (Google Fonts)

## Facts the copy must stay true to

Muscle Memory (repo mymusclememory/imaginative-kashata-2b43c9, live at
mymusclememory.app):
- Free, no paywall. A Stripe Pro tier was built in Sep 2026 and removed
  in Nov 2026. Do not mention pricing.
- Sign-in is a one-time email code (OTP), not a magic link. Signup is
  invite only.
- Local-first: workouts live on the device; cloud backup syncs workouts
  and body weight.
- Photo import is read by Claude server-side and needs sign-in. Pasted
  text, .txt and .pdf are parsed on the phone. The AI parses, it never
  authors.
- Recall coaching notes are deterministic, no AI.
- America's Gym (Wheeling, IL) is the pilot facility for the gym layer.
  The pitch prototype is its own repo, mymusclememory/AmericasGym (one
  index.html, live at americasgym.netlify.app), in the gym's brand: red
  #C10230, blue #002F87, amber #FFAB4D. Member, owner and admin views; the
  owner dashboard is fake on purpose. Videos are stand-ins.

BannerFactory (repo mymusclememory/NOWbannerflow):
- Next.js, TypeScript, Tailwind, Konva. Built by Claude Code from Tim's
  specs.
- 16 standard ad sizes (Amazon DSP + IAB) from one upload, with
  per-size legibility checks.
- The name on the site is BannerFactory (Tim's call), even though the
  app's own UI currently says "OnSpec".
- Keep it brand-neutral. Do not show NOW Foods names, products, logos or
  the purple. NOW does not know about this tool. Screenshots use
  "Field & Co.", a made-up sample brand (capture/assets).

NOW Amazon Creative Guide (Figma file 8Z97hmdkGYXqRQJKFAgOlT, "NOW
Amazon Creative Design System"):
- Tim chose to show it with full NOW branding (Nov 2026). NOW names,
  logos and colors may appear on this page and in the home page's CPG
  brand work section, and nowhere else.
- Never link it to BannerFactory or suggest NOW knows about that tool.
  BannerFactory stays brand-neutral.
- Do not publish from the file: internal email addresses, the
  reference screenshots of NOW or partner marketing, ASINs, or review
  status notes from the A+ template.
- Tokens, rules, component specs and copy on the page come straight
  from the file, with one change Tim made: rule 1 on the page says
  AI-generated content is produced internally by NOW, following
  approved guidelines.
- The "Example build" section shows Tim's Gut Health set from the
  Approved Layouts page (listing images and the A+ page, desktop and
  mobile), saved in now-creative-guide/build/. Only the Product Sets
  may be shown; never the References frame. The NOW logo is rebuilt from its Figma layers, so keep
  the assets/logo-*.svg files and their positions as they are.

CPG brand work (home page section):
- Copy and images come from the live timimbo.com project pages (the
  session's network allows www.timimbo.com and static.wixstatic.com).
  Keep the project descriptions in his words. Each project has
  <id>-1..6.jpg (max 1600px), <id>-N-t.jpg thumbnails for the dialog,
  and cover-<id>.jpg plus a -700 variant.

## Performance and touch targets

- Large images ship with smaller variants (-420, -700, -800, -1200)
  wired up with srcset/sizes, so phones download small files. Add a
  variant and srcset for any new large image.
- netlify.toml sets cache headers: one week for images and exported
  assets, one hour for CSS and JS.
- Buttons and links keep a touch area of at least 44px tall (menu,
  footer, pills); the guide's pill tabs are 40px.

## Where the visuals came from (capture/)

All screenshots are real screens from the two apps, run locally with
Playwright and Chrome:
- seed.py writes seed.json: 7 weeks of sample PHAT training history,
  body weight and cycle state for Muscle Memory's localStorage.
- mm.py and mm2.py serve the Muscle Memory repo on localhost:8101, load
  the seed, and capture the workout list, session, superset, History,
  Progress and the import flow at 393x852 @3x.
- bf3.py drives BannerFactory on localhost:8102 (`next build && next
  start`), uploads the Field & Co. sample assets, and captures the
  editor, the list view and each banner canvas.
- ag.py serves the AmericasGym repo on localhost:8104 and captures the
  start screen, the floor and a machine tutorial (#/equipment/<slug>).
- site.py renders the finished site at 1440 and 390 wide to check it.
- review.js (Node, Playwright) serves site/ and renders every page at
  1440, 1024, 390 and 375 wide, and reports any sideways overflow.
- share.js (Node, Playwright) rebuilds the og-*.jpg share images and
  the PNG icons from the screenshots and favicon.svg. The NOW guide's
  share image is a render of that page's cover.
Outputs go to capture/out and capture/export (git-ignored). Images were
then resized to 786px wide for phones and 2000px for desktop, saved as
JPEG, and copied into site/images.
The scripts were written for a one-off session: adjust ports, the
Chrome path and repo locations before rerunning.

## Open items

1. BannerFactory "Impact" line is a placeholder until Tim has a real
   result.
2. Domain: work.timimbo.com (or similar) on Netlify, CNAME in Wix DNS.
   Share images only work once this domain is live (see Page patterns).
3. "From a real spec" excerpts on both case studies are placeholders
   until Tim supplies real spec lines.
