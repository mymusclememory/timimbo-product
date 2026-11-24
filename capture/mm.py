import re
import asyncio, json
from playwright.async_api import async_playwright
SEED=json.load(open("seed.json")); O="out/"
async def btn(pg,name,exact=False):
    loc=pg.get_by_role("button",name=name,exact=exact)
    if not await loc.count(): loc=pg.get_by_text(name,exact=exact)
    await loc.first.click(); await pg.wait_for_timeout(500)
async def fresh(c):
    pg=await c.new_page(); pg.on("pageerror",lambda e:print("ERR",e))
    await pg.goto("http://localhost:8101/"); await pg.wait_for_timeout(800)
    await pg.evaluate("s=>{localStorage.clear();for(const k in s)localStorage.setItem(k,s[k])}",SEED)
    await pg.reload(); await pg.wait_for_timeout(2000); return pg
async def labels(pg):
    return await pg.eval_on_selector_all("button,[role=button]",'els=>els.map(e=>(e.getAttribute("aria-label")||e.innerText||"").trim().replace(/\\n/g," | ").slice(0,60)).filter(Boolean)')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        c=await b.new_context(viewport={"width":393,"height":852},device_scale_factor=3,is_mobile=True,has_touch=True)
        pg=await fresh(c)
        await pg.screenshot(path=O+"mm_days.png")
        await btn(pg,"HISTORY")
        y=await pg.evaluate("(()=>{const e=[...document.querySelectorAll('*')].find(n=>n.innerText&&n.innerText.trim().startsWith('NOVEMBER')&&n.children.length<4);return e?e.getBoundingClientRect().top+scrollY-12:0})()")
        await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(300); await pg.screenshot(path=O+"mm_history.png")
        await btn(pg,"PROGRESS"); await pg.wait_for_timeout(600)
        y=await pg.evaluate("(()=>{const e=[...document.querySelectorAll('*')].find(n=>n.innerText&&n.innerText.trim()==='THIS WEEK');return e?e.getBoundingClientRect().top+scrollY-12:0})()")
        await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(300); await pg.screenshot(path=O+"mm_progress.png")
        await btn(pg,"WORKOUTS"); await pg.evaluate("window.scrollTo(0,0)")
        await pg.locator("button",has_text=re.compile(r"^start$",re.I)).nth(2).click(); await pg.wait_for_timeout(700)
        print("session:",(await labels(pg))[:20])
        await pg.screenshot(path=O+"mm_session_list.png")
        async def hold(t):
            bx=await pg.get_by_text(t,exact=True).first.bounding_box()
            await pg.mouse.move(bx["x"]+10,bx["y"]+8); await pg.mouse.down(); await pg.wait_for_timeout(700); await pg.mouse.up(); await pg.wait_for_timeout(500)
        await hold("Rack Chin")
        await pg.get_by_role("button",name="Link Rack Chin as a superset").click(); await pg.wait_for_timeout(300)
        await pg.get_by_role("button",name="Link Seated Cable Row as a superset").click(); await pg.wait_for_timeout(800)
        print("linked:",(await labels(pg))[:16])
        await pg.screenshot(path=O+"mm_superset.png")
        await b.close(); return
        print("after hold:",(await labels(pg))[:30])
        await pg.get_by_role("button",name="Link Rack Chin as a superset").click(); await pg.wait_for_timeout(300)
        await pg.get_by_role("button",name="Link Seated Cable Row as a superset").click(); await pg.wait_for_timeout(800)
        print("linked:",(await labels(pg))[:16])
        await pg.screenshot(path=O+"mm_superset.png")
        await b.close(); return
        cards=pg.get_by_role("button",name="Open ",exact=False)
        await cards.nth(1).click(); await pg.wait_for_timeout(500)
        try:
            await btn(pg,"LOG SET"); await btn(pg,"LOG SET")
        except Exception as e: print("log miss",e)
        await pg.evaluate("window.scrollTo(0,0)")
        await pg.screenshot(path=O+"mm_session.png")
        await b.close()
asyncio.run(main())
