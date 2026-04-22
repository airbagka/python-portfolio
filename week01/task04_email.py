email = str(input("Введите email: "))

correct = "Нет"
if "@" in email and "." in email:
    correct = "Да"
elif "@" not in email:
    correct = "Нет\nОшибка: email должен содержать символ @"  
elif "."  not in email:
    correct = "Нет\nОшибка: email должен содержать символ ."

if correct == "Да":
    index = email.find("@")
    index_dort = email.rfind(".")
    name = email[:index]
    domain = email[index+1:]
    domain_zone = email[index_dort+1:]

    print(f'Email корректен: {correct}')
    print(f'Имя пользователя: {name}')
    print(f'Домен: {domain}')
    print(f'Зона домена: {domain_zone}')
else:
    print(f'Email корректен: {correct}')