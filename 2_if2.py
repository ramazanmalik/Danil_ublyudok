"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):
  if len(str1) == len(str2):
    return 1
  if len(str1) != len(str2) and 'learn' in str2.lower():
    return 3
  elif len(str1) > len(str2):
    return 2

str1 = ' '
str2 = 'learn'
print(main(str1, str2))

if __name__ == "__main__":
    main(str1, str2)
