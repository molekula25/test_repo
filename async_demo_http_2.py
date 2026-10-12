import time
import asyncio
import httpx


URL = "https://httpbin.org/delay/60"



async def async_get_data(
    client: httpx.AsyncClient,
    request_number: int,
)    -> None:
    print(f"запрос № {request_number}: начало")
    response = await client.get(URL)
    response.raise_for_status()
    print(f"запрос № {request_number}: завершен")


    #data = response.json()
    #print(f"HTTP status {response.status_code}")
    #print(f"Data {data}")
    #print(type(data))



async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        await asyncio.gather(
           async_get_data(client, 1),
           async_get_data(client, 2),
           async_get_data(client, 3)
)

start = time.perf_counter()
asyncio.run(main())

timer = time.perf_counter() - start
print(f"{timer:.5f} seconds")