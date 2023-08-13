import asyncio, requests

async def update():
    await asyncio.sleep(1)
    response = requests.get("https://raw.githubusercontent.com/WBRK-dev/minecraft_server_manager/main/main.py")
    response.raise_for_status()

    with open('main.py', 'wb') as file:
        file.write(response.content)

asyncio.run(update())