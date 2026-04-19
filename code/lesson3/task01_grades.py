text = input("Введите оценки через пробел: ")

listA = text.split(" ")

for i in range(len(listA)):
    listA[i] = int(listA[i])

print(f"Список оценок: {listA}")
print(f"Количество: {len(listA)}")
print(f"Средний балл: {sum(listA)/len(listA)}")
print(f"Лучшая оценка: {max(listA)}")
print(f"Худшая оценка: {min(listA)}")
print(f"Количество пятерок: {listA.count(5)}")
print(f"По убывающей: {sorted(listA, reverse=True)}")
