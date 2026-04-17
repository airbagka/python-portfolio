text = str(input("Введите фразу: "))

text_list = text.split(" ")
string = ""
password = ""

for i in text_list:
    string += str(i[0])

for g, y in enumerate(string):
    print(g)
    print(y)
    if g%2 == 1:
        password += str(string[g]).upper
    else:
        password += str(string[g]).lower

password = password+len(string)+"!"


print(f'Первые буквы: {string}')
print(f'Первые буквы: {string}')
print(f'Сгенерированный пароль: {password}')
