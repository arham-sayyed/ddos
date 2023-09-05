import aiohttp
import asyncio
import time

URL = "https://vbr.wocr.tk/badge?page_id=683298968&logo=python&lcolor=black&text=views&color=000000"

async def fetch(session, idx, results):
    try:
        async with session.get(URL) as response:
            results[idx] = (response.status, idx)
    except Exception as e:
        results[idx] = ("Error:", str(e))

async def main():
    results = [None] * 1000
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, i, results) for i in range(1000)]
        await asyncio.gather(*tasks)

    for idx, (status, current_iter) in enumerate(results):
        print(status, current_iter)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start, "seconds")
