#-Task_1-
print('Вычислить число c заданной точностью d')

num = float(input('Введите вещественное число: '))
num_precision = input('Введите точность числа: ')
a = num_precision.split('.')[1]       #Берем дробную часть числа num
print(round(num, len(a)))             #Сокращаем дробную часть числа(num) на количество (num_precision) элементов после точки

# -Task_2-
print('Задайте натуральное число N. Напишите программу,' 
      'которая составит список простых множителей числа N')

number = int(input('Введите число: '))
for i in range(number -1, 1, -1):
      count = 0
      if number % i == 0:
            for j in range(i-1,1,-1):
                  if i % j == 0:
                        count+=1
            if count == 0:
                  print(i, end=' ')

# -Task_3-

print('Задайте последовательность чисел. '
      'Напишите программу, которая выведет список неповторяющихся '
      'элементов исходной последовательности.')

from random import randint

n = int(input('Введите количество элементов: '))
arr = [randint(0,10) for x in range(n)]
print(f'Исходный список -> {arr}')
arr2=[]
for i in range(len(arr)):
      if arr[i] in arr2:
            continue
      else:
            arr2.append(arr[i])
print(f'Список из неповторяющихся элементов -> {arr2}')