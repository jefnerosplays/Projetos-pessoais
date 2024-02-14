import math
pi = 3.141
r = int(input('Qual é o raio do pnel? '))
p = 2 * pi * r
consumo =  7.5* (10 ** -6)
clc = p / consumo
d = (p * 100) / (consumo * (10 ** -6))
lcl = d / 100
print('{:.1f}'.format(math.ceil(d)))