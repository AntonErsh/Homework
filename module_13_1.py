import asyncio


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования ')

    for ball_number in range(1, 6):
        await asyncio.sleep(10 // power)
        print(f'Силач {name} поднял {ball_number}')

    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Alex', 5))
    task2 = asyncio.create_task(start_strongman('Ivan', 10))
    task3 = asyncio.create_task(start_strongman('Matvey', 3))
    task4 = asyncio.create_task(start_strongman('Mashina-Ubiytsa', 100))
    await task1
    await task2
    await task3
    await task4
    print('Соревнования окончены!')

asyncio.run(start_tournament())
