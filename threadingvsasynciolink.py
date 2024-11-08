import time
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

# Daftar URL s
urls = [
    f'https://jsonplaceholder.typicode.com/posts/{i}' for i in range(1, 50)
]

# Fungsi untuk melakukan permintaan HTTP (I/O-bound)
def fetch_url(url):
    response = requests.get(url)
    return response.text

# Pengujian dengan Multithreading
def test_multithreading():
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))
    end_time = time.time()
    print(f"Multithreading selesai dalam waktu: {end_time - start_time} detik")
    return results

# Fungsi Asyncio untuk permintaan HTTP
async def test_asyncio(urls):
    start_time = time.time()
    loop = asyncio.get_running_loop()
    
    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, fetch_url, url)
            for url in urls
        ]
        results = await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Asyncio selesai dalam waktu: {end_time - start_time} detik")
    return results

if __name__ == "__main__":
    print("Menggunakan Multithreading:")
    test_multithreading()

    print("\nMenggunakan Asyncio:")
    asyncio.run(test_asyncio(urls))
