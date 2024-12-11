def process_results(*args):
    for result in args:
        number = int(result.split(':')[1].strip()) + 10
        print(number)


process_results(
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2")
