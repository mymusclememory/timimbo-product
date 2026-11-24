import asyncio, sys, json
from playwright.async_api import async_playwright
O="out/"
async def labels(pg):
    return await pg.eval_on_selector_all("button,a,[role=button],[role=tab]",'els=>els.filter(e=>e.offsetParent).map(e=>(e.getAttribute("aria-label")||e.innerText||"").trim().replace(/\\n/g," | ").slice(0,50)).filter(Boolean)')
async def main():
    routes=json.loads(sys.argv[1])
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        c=await b.new_context(viewport={"width":393,"height":852},device_scale_factor=3,is_mobile=True,has_touch=True)
        pg=await c.new_page(); pg.on("pageerror",lambda e:print("ERR",e))
        await pg.goto("http://localhost:8104/"); await pg.wait_for_timeout(2000)
        for name,r in routes:
            if r.startswith("#"):
                await pg.evaluate(f"location.hash='{r}'")
            elif r.startswith("click:"):
                loc=pg.get_by_role("button",name=r[6:],exact=True); loc=loc if await loc.count() else pg.get_by_text(r[6:])
                await loc.first.click()
            elif r.startswith("scroll:"):
                await pg.evaluate(f"scrollTo(0,{r[7:]})")
            await pg.wait_for_timeout(1200)
            if not r.startswith("scroll:"): await pg.evaluate("scrollTo(0,0)")
            await pg.screenshot(path=O+"ag_"+name+".png"); print(name, (await labels(pg))[:30])
        await b.close()
asyncio.run(main())
