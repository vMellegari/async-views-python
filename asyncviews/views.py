import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org")
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Assincrona, página carregou ao mesmo tempo que a contagem no terminal")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Sincrona, página carregou somente após a contagem no terminal")

def home_view(request):
    return HttpResponse("Digite no link do caminho:<br>/sync/ - para sincrona<br>/async/ - para assincrona")