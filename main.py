import aiohttp
import asyncio
import time

URL = "https://vbr.wocr.tk/badge?page_id=683298968&logo=python&lcolor=black&text=views&color=000000"

async def fetch(session):
    try:
        async with session.get(URL) as response:
            return response.status
    except Exception:
        return "Error"

async def main(TOTAL_REQUESTS):
    # Optimize by removing pre-allocation of results.
    # We'll collect the results directly from the tasks.
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=10000)) as session:
        tasks = [fetch(session) for _ in range(TOTAL_REQUESTS)]
        results = await asyncio.gather(*tasks)

    successful_requests = results.count(200)
    print(f"Successful Requests: {successful_requests}")
    print(f"Errors: {TOTAL_REQUESTS - successful_requests}")

if __name__ == "__main__":
    # Requesting user input for number of requests
    try:
        TOTAL_REQUESTS = int(input("Enter the number of requests: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

    start = time.time()
    asyncio.run(main(TOTAL_REQUESTS))
    end = time.time()
    print(end - start, "seconds")
