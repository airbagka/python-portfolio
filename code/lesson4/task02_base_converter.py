num = int(input("Введите целое число: "))

binary = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:].upper()

print(f"Десятичное:        {num}")
print(f"Двоичное:          {binary}")
print(f"Восьмеричное:      {octal}")
print(f"Шестнадцатеричное: {hexadecimal}")
print()
print(f"  {num} в двоичной содержит {len(binary)} бит")
print(f"  Сумма цифр в десятичной: {sum(int(d) for d in str(num))}")
