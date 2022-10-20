print('Задана натуральная степень k. '
      'Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и '
      'записать в файл многочлен степени k.')

from random import randint

k = int(input('Введите натуральную степень k: '))

def file(f):
      with open('C:\\Users\\Onotole\\Desktop\\pythonDz04\\Dz-04\\file1.txt', 'w') as data:
            data.write(f)

list1 = [randint(0,101) for i in range(k + 1)]
print(list1)
def polynom(spisok):
      arr = spisok[::-1]
      res = ''
      for i in range(len(arr)):
            if i != len(arr) - 1 and arr[i] != 0 and i != len(arr) - 2:
                  res += f'{arr[i]}x^{len(arr) - i - 1}'
                  if arr[i + 1] != 0:
                        res += ' + '
            elif i == len(arr) - 2 and arr[i] != 0:
                  res += f'{arr[i]}x'
                  if arr[i + 1] != 0:
                        res += ' + '
            elif i == len(arr) - 1 and arr[i] != 0:
                  res += f'{arr[i]} = 0'
            elif i == len(arr) - 1 and arr[i] == 0:
                  res += ' = 0'
      return res

file(polynom(list1))