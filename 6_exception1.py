"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
    while True:
      how_are_you = input('Как дела? ')
      if how_are_you.lower() == 'хорошо':
        print('Ну и пошел нахуй')
        break
      else:
        print(how_are_you)
  except (KeyboardInterrupt):
    print('Пока!')

print(hello_user())
    
if __name__ == "__main__":
    hello_user()
