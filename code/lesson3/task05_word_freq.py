text = str(input("Введите текст: "))
print("Частотный словарь:")

listA = text.lower().split(" ")
dictA = {}
for i in listA:
    count = 0
    if listA.count(i) > count and i not in dictA: 
        count = listA.count(i)
        print(i, ":", count)
        dictA[i] = count

print("Топ-5 самых частых слов:")
for word, freq in sorted(dictA.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{word}: {freq} раз(а)")