# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.  2*х^2 + 5*х + 33 = 0

from dataclasses import replace
from random import randint, choice

pp = '2*х^2 + 5*х + 33 = 0'
pol = ['2','*x^','2',' + ', '5', '*x + ','33',' = 0']

k = 3

ratios = [str(randint(0, 101)) for x in range(k)]
indexes = [0, 4, 6, 2]

def change_poly(pol, indexes, ratios, k):
    ratios.append(str(k))
    for indexes, replacement in zip(indexes, ratios):
        pol[indexes] = replacement
    return "".join(pol)

pol_new = change_poly(pol, indexes, ratios, k)
print(pol_new)

with open('pol_uncorr33.txt', 'w') as data:
    data.write(pol_new)
