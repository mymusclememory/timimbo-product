# First task for Claude Code

This repo is my product design portfolio microsite. It is plain HTML and
CSS, hosted on Netlify, and linked from timimbo.com. It needs to be
finished and polished.

STEP 0: READ FIRST
Read CLAUDE.md fully. It is the source of truth for facts, colors, fonts
and rules. Report back what you found before changing anything.

WHAT EXISTS
- site/index.html: home page with one card per case study
- site/muscle-memory/index.html: Muscle Memory, plus the America's Gym
  facility layer
- site/bannerfactory/index.html: BannerFactory
- site/styles.css: one shared stylesheet
- site/images/: real screenshots from the apps, already optimized
- capture/: the Playwright scripts that took the screenshots

WHAT TO BUILD
1. Polish: review every page at 1440, 1024, 390 and 375 wide. Tighten
   spacing, type sizes and section rhythm. Keep the current look and
   design tokens. No sideways scrolling at any width.
2. Make the visuals explain themselves: add short captions and small
   callouts that point at what matters in each screenshot: the Recall
   coaching note, the superset link, the legibility checks in
   BannerFactory, the QR tutorial on the gym floor.
3. Add a "Process" section to each case study: I write specs, Claude
   Code builds on a branch, and I review every change on a deploy
   preview before it merges. Use only facts from CLAUDE.md.
4. Motion: a subtle fade and rise as sections scroll in. Turn it off
   for prefers-reduced-motion. Use a few lines of vanilla JS only.
5. Sharing: Open Graph and Twitter card tags on every page, each with a
   1200x630 share image you make from the existing screenshots.
6. Basics: favicon, page titles, meta descriptions, a 404 page in the
   same style, and image alt text checked on every image.

RULES
- Never use em dashes anywhere: copy, comments, commit messages, or
  your replies to me.
- Do not invent numbers, results or quotes. Anything you need from me
  becomes a visible [PLACEHOLDER].
- Keep BannerFactory brand-neutral: no NOW Foods names, logos, products
  or purple. Muscle Memory is free; do not mention pricing.
- No frameworks and no build step. Netlify serves site/ as-is.
- I am a designer, not a developer. Report in short plain-language
  bullets, framed as what I need to do next.

HOW TO DELIVER
Work on a branch, open a pull request, and give me the Netlify deploy
preview link. Do not merge; I review on my phone and call the merge.
End with a list of every [PLACEHOLDER] and anything else you need from
me.
