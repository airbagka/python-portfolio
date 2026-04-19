python_course = {"Алиса", "Борис", "Вика", "Глеб", "Дина", "Евгений"}
data_course = {"Вика", "Глеб", "Жанна", "Зинаида", "Евгений", "Ирина"}

print(f"Учатся на обоих курсах: {python_course & data_course}")
print(f"Учатся только на курсе Python: {python_course - data_course}")
print(f"Учатся только на курсе Data Science: {data_course - python_course}")
print(f"Все студенты: {python_course.union(data_course)}")
print(f"Всего уникальных студентов: {len(python_course.union(data_course))}")