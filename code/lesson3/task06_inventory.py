inventory = {}

while True:
    command = input("Команда: ")
    parts = command.split()

    if not parts:
        continue

    action = parts[0]

    if action == "quit":
        break

    elif action == "show":
        print("=== Инвентарь ===")
        total = 0
        for item, qty in inventory.items():
            print(f"  {item}: {qty} шт.")
            total += qty
        print(f"Всего предметов: {total}")

    elif action == "add":
        if len(parts) < 3:
            print("Использование: add <предмет> <количество>")
            continue
        item = parts[1]
        try:
            qty = int(parts[2])
        except ValueError:
            print("Количество должно быть числом")
            continue
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
        print(f"Добавлено: {item} x{qty}")

    elif action == "remove":
        if len(parts) < 3:
            print("Использование: remove <предмет> <количество>")
            continue
        item = parts[1]
        try:
            qty = int(parts[2])
        except ValueError:
            print("Количество должно быть числом")
            continue
        if item not in inventory:
            print(f"Предмет '{item}' не найден")
            continue
        if inventory[item] < qty:
            print(f"Недостаточно предметов: {item} (есть {inventory[item]})")
            continue
        inventory[item] -= qty
        if inventory[item] == 0:
            del inventory[item]
        print(f"Убрано: {item} x{qty}")

    else:
        print("Неизвестная команда")
