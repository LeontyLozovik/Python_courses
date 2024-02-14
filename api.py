import requests
import asyncio
import time
from aiohttp import ClientSession

cites = ['Kiev', 'Minsk', 'Liverpool', 'Graz']


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
    res = requests.get(url, params)
    j = res.json()
    print(f'{city} - {j["weather"][0]["main"]}')


async def a_get_weather(city):
    async with ClientSession() as session:
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
        async with session.get(url, params=params) as response:
            j = await response.json()
            print(j)


async def a_main(cites):
    tasks = []
    for city in cites:
        tasks.append(asyncio.create_task(a_get_weather(city)))

    for task in tasks:
        q = await task


t = time.time()
for city in cites:
    get_weather(city)
print(time.time() - t)

t = time.time()
asyncio.run(a_main(cites))
print(time.time() - t)