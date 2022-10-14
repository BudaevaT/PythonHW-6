# Сформировать список из  N членов последовательности.

number = int(input("Введите число: "))
lst = [(-3)**i for i in range(number)]
print(f"Итоговая последовательность после применения list comprehension: {lst}")