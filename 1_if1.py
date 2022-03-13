def main(age):
  if int(age) == 0:
    return "Ясно, автору ноль лет"
  if int(age) > 0 and int(age) < 7:
    return "Ты щенок"
  if int(age) >= 7 and int(age) < 18:
    return "Ясно, ты школьник"
  if int(age) >= 18 and int(age) < 23:
    return "Ты в ВУЗе или на заводе"
  if int(age) >= 23 and int(age) < 60:
    return "Ты работяга"
  if int(age) >= 60 and int(age) < 90:
    return "Ты в доме престарелых"
  if int(age) >= 90:
    return "У нас столько не живут"
  else:
    return "Нормально напиши, чел"

age = input('Сколько тебе лет? ')
print(main(age)) 

if __name__ == "__main__":
    main(age)