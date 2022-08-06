import asyncio


# обычная функция
def my_simple_func():
    print("Выполняется обычная фнукция")
    return "Результат обычной функции"


# корутина
async def my_coroutine():
    print("Выполняется корутина")
    return "Результат из корутины"

print("Начало обычной программы")
asyncio.run(my_coroutine())
print("Конец обычной программы")
