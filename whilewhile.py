questions_and_answers = {
'Как дела?': 'Хорошо',
'Что делаешь?': 'Читаю',
'Вилкой в глаз?': 'Не надо',
}

def ask_user(answers_dict):
  while True:
    whereve_u_been = input('Введите вопрос: ')
    for question, answer in answers_dict.items():
        if whereve_u_been == question:
            print(answer)
    else:
      print(whereve_u_been)
    
print(ask_user(questions_and_answers))