# Создайте функцию генератор чисел Фибоначчи

def func(data:int):
    num1 = 0
    num2 = 1
    for _ in range(data):
        yield num1

        next_num = num1 + num2
        num1 = num2
        num2 = next_num


for num in func(10):
    print(f'{num}')

