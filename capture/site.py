import asyncio
from playwright.async_api import async_playwright
from PIL import Image
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for w,tag in [(1440,"d"),(390,"m")]:
            c=await b.new_context(viewport={"width":w,"height":900})
            pg=await c.new_page()
            for path,n in [("","home"),("muscle-memory/","mm"),("bannerfactory/","bf")]:
                await pg.goto("http://localhost:8103/"+path); await pg.wait_for_timeout(1500)
                await pg.evaluate("document.querySelectorAll('img[loading]').forEach(i=>i.loading='eager')"); await pg.wait_for_timeout(1500); await pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,80))}scrollTo(0,0)}")
                await pg.wait_for_timeout(800)
                f=f"out/site_{tag}_{n}.png"; await pg.screenshot(path=f,full_page=True)
                ow=await pg.evaluate("document.documentElement.scrollWidth>innerWidth"); print(tag,n,"overflow" if ow else "ok")
        await b.close()
asyncio.run(main())
