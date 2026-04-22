questions = [
    {
        "question": "Какой тип данных возвращает выражение 10 / 3?",
        "options": ["A) int", "B) float", "C) str", "D) bool"],
        "answer": "B",
    },
    {
        "question": "Как создать пустое множество (set)?",
        "options": ["A) {}", "B) set()", "C) []", "D) ()"],
        "answer": "B",
        "explanation": "{} создаёт пустой словарь, а не множество.",
    },
    {
        "question": "Какой метод добавляет элемент в конец списка?",
        "options": ["A) add()", "B) append()", "C) insert()", "D) extend()"],
        "answer": "B",
    },
    {
        "question": "Что выведет код: 'Hello'.upper()?",
        "options": ["A) hello", "B) Hello", "C) HELLO", "D) hELLO"],
        "answer": "C",
    },
    {
        "question": "Как получить все ключи словаря?",
        "options": [
            "A) dict.values()",
            "B) dict.keys()",
            "C) dict.items()",
            "D) dict.get()",
        ],
        "answer": "B",
    },
    {
        "question": "Какой метод удаляет элемент из множества?",
        "options": ["A) remove()", "B) delete()", "C) pop()", "D) discard()"],
        "answer": "A",
    },
    {
        "question": "Что выведет f'{2 + 2}'?",
        "options": ["A) 4", "B) '4'", "C) f'4'", "D) 2 + 2"],
        "answer": "A",
    },
    {
        "question": "В чём разница между 'is' и '=='?",
        "options": [
            "A) Они идентичны",
            "B) 'is' проверяет идентичность, '==' проверяет равенство",
            "C) '==' проверяет идентичность, 'is' проверяет равенство",
            "D) Они работают только с числами",
        ],
        "answer": "B",
    },
    {
        "question": "Что вернёт список '[1, 2, 3][::-1]'?",
        "options": ["A) [1, 2, 3]", "B) [3, 2, 1]", "C) [1, 2]", "D) [3, 2]"],
        "answer": "B",
    },
    {
        "question": "Какой метод возвращает отсортированную копию списка?",
        "options": ["A) sort()", "B) sorted()", "C) order()", "D) reorder()"],
        "answer": "B",
    },
]


def run_quiz():
    print("=== Викторина: Основы Python ===\n")

    correct_count = 0

    for i, q in enumerate(questions, 1):
        print(f"Вопрос {i} из {len(questions)}:")
        print(f"  {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        user_answer = input("Ваш ответ: ").strip().upper()

        if user_answer == q["answer"]:
            print("Правильно!\n")
            correct_count += 1
        else:
            print(f"Неправильно! Правильный ответ: {q['answer']}")
            if "explanation" in q:
                print(f"{q['explanation']}\n")
            else:
                print()

    total = len(questions)
    percentage = (correct_count / total) * 100

    if percentage >= 90:
        grade = "Отлично"
    elif percentage >= 70:
        grade = "Хорошо"
    elif percentage >= 50:
        grade = "Удовлетворительно"
    else:
        grade = "Нужно повторить материал"

    print("=== Результаты ===")
    print(f"Правильных ответов: {correct_count} из {total}")
    print(f"Процент: {percentage:.0f}%")
    print(f"Оценка: {grade}")


if __name__ == "__main__":
    run_quiz()
