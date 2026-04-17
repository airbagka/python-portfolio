text = str(input("Введите числа через пробел: "))

amount = 0
sumi = 0
average = 0 
mini = 0
maxi = 0
numbers = text.split(" ")
numbers_int=[float(i) for i in numbers]

amount = len(numbers_int)
mini = min(numbers_int)
maxi = max(numbers_int)
sumi = sum(numbers_int)
average = sumi/amount

print(f'Количество {amount}')
print(f'Сумма: {sumi} ')
print(f'Среднее: {average}')
print(f'Минимум: {mini}')
print(f'Максимум: {maxi}')