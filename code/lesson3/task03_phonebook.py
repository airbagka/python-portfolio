contacts = {}
print("Введите контакты (Имя:Телефон), пустая строка для завершения:")
while True:
    line = input()
    if line == "":
        break
    name, phone = line.split(":")
    if name not in contacts:
        contacts[name] = []
    contacts[name].append(phone)

print("\n=== Телефонная книга ===")
for name, phones in contacts.items():
    if len(phones) > 1:
        print(f"{name}: {', '.join(phones)}")
    else:
        print(f"{name}:  {phones[0]}")

name_to_find = input("\nКого найти? ")
if name_to_find in contacts:
    print(f"Результат поиска: {name_to_find} — {', '.join(contacts[name_to_find])}")
else:
    print(f"Результат поиска: {name_to_find} — не найден")
