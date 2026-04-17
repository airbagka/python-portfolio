tovar = input(str("Название товара: "))
price =float(input("Цена за единицу: "))
amout = int(input("Количество: "))

tax = price*amout*20/100

print("="*30)
print(" "*15+ "ЧЕК")
print("="*30)

print(f'Товар: {" "*10} {tovar}')
print(f'Цена: {" "*11} {price:,.2f}')
print(f'Количество: {" "*5} {amout}')
print("_"*30)
print(f'Сумма: {" "*10} {price*amout:,.2f}')
print(f'НДС (20%): {" "*6} {tax:,.2f}')
print("_"*30)
print(f'ИТОГО: {" "*10} {price*amout+tax:,.2f}')
