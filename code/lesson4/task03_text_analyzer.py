text = """Python был создан Гвидо ван Россумом в начале 1990-х годов. Python является языком программирования общего назначения. Python используется для веб-разработки, анализа данных, машинного обучения и автоматизации. Python имеет простой и понятный синтаксис. Python поддерживает множество парадигм программирования. Многие компании используют Python в своих проектах."""

text_lower = text.lower()
words = text_lower.split()
sentences = text.count(".")

total_chars = len(text)
chars_no_spaces = len(text.replace(" ", ""))
total_words = len(words)
total_sentences = sentences
avg_word_len = sum(len(w) for w in words) / total_words
avg_sentence_len = total_words / total_sentences if total_sentences > 0 else 0

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

letter_counts = {}
for c in text:
    if c.isalpha():
        letter_counts[c.lower()] = letter_counts.get(c.lower(), 0) + 1

unique_words = len(word_counts)
words_more_than_once = sorted(
    [(w, c) for w, c in word_counts.items() if c > 1], key=lambda x: (-x[1], x[0])
)

top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
top_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)[:5]

print("=== Анализ текста ===")
print()
print("Основная статистика:")
print(f"  Символов (с пробелами):  {total_chars}")
print(f"  Символов (без пробелов): {chars_no_spaces}")
print(f"  Слов:                    {total_words}")
print(f"  Предложений:             {total_sentences}")
print(f"  Средняя длина слова:     {avg_word_len:.2f} символов")
print(f"  Средняя длина предложения: {avg_sentence_len:.2f} слов")
print()
print("Частота слов (топ-10):")
for i, (word, count) in enumerate(top_words, 1):
    spaces = " " * (15 - len(word))
    print(f"  {i}. {word}{spaces}— {count}")
print()
print("Частота букв (топ-5):")
for i, (letter, count) in enumerate(top_letters, 1):
    spaces = " " * (15 - len(letter))
    print(f"  {i}. {letter}{spaces}— {count}")
print()
print(f"Уникальных слов: {unique_words}")
words_list = ", ".join([w for w, c in words_more_than_once])
print(f"Слова, встречающиеся более 1 раза: {words_list}")
