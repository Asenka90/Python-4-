#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print("Задача 1")
from math import pi
d = int(input("Введите точность c которой хотите получить число Пи: "))
str1 = str(pi)
lst = []
for i in range(d + 2):
    lst.append(str1[i])
pi = "".join(lst)
print(f"Число Пи с заданной точностью {d} равно {pi}")

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Задача 2")
n=int(input("Введите число: "))
print(f"Простые множетели введенного числа: ")
for i in range(1, n+1):
    if(n%i==0):
        print(i)

#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

print("Задача 3")
list1 = [1, 2, 2, 3, 3, 4, 5]
print("Список: ", list1)
unique = list(set(list1))
print("Список уникальных элементов списка: ", unique)

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

print("Задача 4")
import random
def рolynomial():
    try:
        k = int(input("Введите натуральную степень: "))
        a = int(random.randint(0, 100))
        b = int(random.randint(0, 100))
        c = int(random.randint(0, 100))
    except ValueError:
        print("Некорректный ввод")
        print()
        рolynomial()
    else:
        if a != 0:
            one = (str(a) + "x^" + str(k) + " + ")
        else:
            one = (str())

        if b != 0:
            two = (str(b) + "x" + " + ")
        else:
            two = (str())

        if c != 0:
            three = (str(c) + " = 0")
        else:
            three = (str())
        my_file = open("1.txt", "w+")
        my_file.write(f"{one}{two}{three}")
        my_file.close()
рolynomial()
print("Ответ в файле 1.txt")

#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

print("Задача 5")
polynomial1 = f"{11}x^2 + {27}x + {34}"
print("Первый многочлен:", polynomial1)
polynomial2 = f"{32}x^2 + {16}x + {54}"
print("Второй многочлен:", polynomial2)

with open("f1.txt", "w") as data:
   data.write(polynomial1)
with open("f2.txt", "w") as data:
   data.write(polynomial2)

first_coef_polynomial_1 = int(polynomial1[0] + polynomial1[1])
second_coef_polinomial_1 = int(polynomial1[8] + polynomial1[9])
third_coef_polinomial_1 = int(polynomial1[14] + polynomial1[15])

first_coef_polynomial_2 = int(polynomial2[0] + polynomial2[1])
second_coef_polinomial_2 = int(polynomial2[8] + polynomial2[9])
third_coef_polinomial_2 = int(polynomial2[14] + polynomial2[15])

result1_coef = str(first_coef_polynomial_1 + first_coef_polynomial_2)
result2_coef = str(second_coef_polinomial_1 + second_coef_polinomial_2)
result3_coef = str(third_coef_polinomial_1 + third_coef_polinomial_2)

result = f"{result1_coef}x^2 + {result2_coef}x + {result3_coef}"
with open("result", "w") as data:
    data.write(result)
print("Сумма многочленов:", result)
