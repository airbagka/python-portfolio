text = str(input("Введите текст: "))

listA = text.split(" ")
listB =[]

print(f"Всего слов: {len(listA)}")
print(f"Уникальные слова: {sorted(set(listA))}")
print(f"Количество уникальных слов: {len(set(listA))}")


for i in listA:
    if listA.count(i) > 1:
        listB.append(i)

        
print(f"Повторяющиеся слова: {sorted(set(listB))}")