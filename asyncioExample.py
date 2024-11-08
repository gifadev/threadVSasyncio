import asyncio

async def say_hello(name, delay):
    print(f"Mulai menyapa {name}")
    await asyncio.sleep(delay) 
    print(f"Halo, {name}!")

async def main():
    await asyncio.gather(
        say_hello("Alice", 3),  
        say_hello("Bob", 1),  
        say_hello("Charlie", 2) 
    )
    print("Semua sapaan selesai!")

asyncio.run(main())
