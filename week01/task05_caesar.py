text = str(input("Введите текст: "))
n = int(input("Введите сдвиг: "))
new_text = ""

for i in text:
    if  i.isalpha():
        code=ord(str(i))+n
        new_text=new_text+chr(code)
    else:
        new_text=new_text+str(i)

print(new_text)

## функция## функция ord() — это встроенная функция Python, которая возвращает целое число
#  (кодовую точку Unicode) для одного символа
# char()  - обратная функция, по коду возвращает букву