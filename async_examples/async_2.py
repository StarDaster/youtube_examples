import asyncio

# await - отдаёт контекст исполнения в event loop


async def one_more_async_func(name):
    print("Это функция", name)
    if name == 5:
        print("Функция 5 заснула")
        await asyncio.sleep(5)
        print("Функция 5 закончила спать")


async def sleeper(name):
    print("Спит функция", name)
    await one_more_async_func(name)
    await asyncio.sleep(name)


def yielder():
    print("Это начало")
    yield
    print("Это конец")


async def main():
    tasks = [sleeper(x) for x in range(10)] + [yielder()]
    await asyncio.gather(*tasks)


asyncio.run(main())
