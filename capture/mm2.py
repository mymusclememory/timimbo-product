import asyncio, json, re, sys
sys.path.insert(0,".")
from mm import fresh, btn, labels, O
from playwright.async_api import async_playwright
PASTE="""Day 1 Push
Bench Press 4x6-8 185
Incline DB Press 3x8-10 65
Cable Fly 3x12-15
Overhead Press 3x8 115
Tricep Pressdown 3x12

Day 2 Pull
Deadlift 3x5 315
Pull-Up 4x8
Barbell Row 4x8 155
Face Pull 3x15
Hammer Curl 3x10 35

Day 3 Legs
Back Squat 4x6 255
Romanian Deadlift 3x10 185
Walking Lunge 3x12 40
Leg Curl 3x12
Calf Raise 4x15"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        c=await b.new_context(viewport={"width":393,"height":852},device_scale_factor=3,is_mobile=True,has_touch=True)
        pg=await fresh(c)
        await pg.locator("button",has_text=re.compile(r"^start$",re.I)).nth(2).click(); await pg.wait_for_timeout(700)
        await pg.get_by_role("button",name="Open Rack Chin").click(); await pg.wait_for_timeout(500)
        await btn(pg,"LOG SET"); await btn(pg,"LOG SET")
        await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(300)
        await pg.screenshot(path=O+"mm_session.png")
        pg=await fresh(c)
        await btn(pg,"New program"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=O+"mm_new.png")
        print("new:",(await labels(pg))[:20])
        await btn(pg,"Paste as text"); await pg.wait_for_timeout(500)
        ta=pg.locator("textarea:visible").first
        await ta.fill(PASTE); await pg.wait_for_timeout(300)
        await pg.screenshot(path=O+"mm_paste.png")
        print("paste:",(await labels(pg))[:20])
        for t in ["Read","Parse","Review","Continue","Preview"]:
            loc=pg.get_by_role("button",name=t)
            if await loc.count():
                await loc.first.click(); await pg.wait_for_timeout(900); print("clicked",t); break
        await pg.evaluate("window.scrollTo(0,0)")
        await pg.screenshot(path=O+"mm_review.png")
        print("review:",(await labels(pg))[:20])
        await b.close()
asyncio.run(main())
