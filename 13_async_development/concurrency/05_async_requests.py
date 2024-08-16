import aiohttp
import asyncio


async def fetch_page(session, url):
    async with session.get(url) as response:
        print(response.status)
        return response.status
        

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

# don't use 50 - Google blocks some of the calls - play it safe with 20
urls = ['http://google.com' for i in range(20)]
loop.run_until_complete(get_multiple_pages(loop, *urls))
