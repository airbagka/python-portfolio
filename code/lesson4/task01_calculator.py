print("=" * 40)
print("  Калькулятор v1.0")
print("  Введите 'help' для справки")
print("=" * 40)

history = []  # список для хранения истории

while True:
    user_input = input("\ncalc> ").strip()

    if not user_input:
        continue

    if user_input.lower() in ("quit", "exit"):
        print("До свидания!")
        break

    if user_input.lower() == "help":
        print("Формат ввода: число1 оператор число2")
        print("Операторы: +  -  *  /  //  %  **")
        print("Команды: history, save, clear, quit")
        continue

    if user_input.lower() == "history":
        if not history:
            print("История пуста.")
        else:
            print("--- История вычислений ---")
            for i, entry in enumerate(history, 1):
                print(f"  {i}. {entry}")
        continue

    if user_input.lower() == "clear":
        history.clear()
        print("История очищена.")
        continue

    if user_input.lower() == "save":
        if not history:
            print("История пуста, нечего сохранять.")
        else:
            with open("calc_history.txt", "w", encoding="utf-8") as f:
                f.write("История вычислений калькулятора\n")
                f.write("=" * 40 + "\n")
                for i, entry in enumerate(history, 1):
                    f.write(f"{i}. {entry}\n")
            print(f"История сохранена в файл 'calc_history.txt' ({len(history)} записей)")
        
        continue


    parts = user_input.split()

    if len(parts) != 3:
        print("Ошибка: введите выражение в формате: число1 оператор число2")
        continue

    num1_str, operator, num2_str = parts
    valid_operators = {'+', '-', '*', '/', '//', '%', '**'}

    if operator not in valid_operators:
        print(f"Ошибка: неизвестный оператор '{operator}'")
        print(f"Доступные операторы: {', '.join(valid_operators)}")
        continue

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Ошибка: введите корректные числа")
        continue

    # Проверка деления на ноль
    if operator in ('/', '//', '%') and num2 == 0:
        print("Ошибка: деление на ноль!")
        continue

    # Вычисление
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '**':
        result = num1 ** num2

    # Вывод результата
    expression = f"{num1} {operator} {num2} = {result}"
    print(f"  {expression}")

    # Сохранение в историю
    history.append(expression)