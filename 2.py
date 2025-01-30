
# Список студентов, каждый студент - это кортеж: (имя, средний балл)
students = [("Алексей", 4.0), ("Мария", 3.8)]

# Функция для увеличения среднего балла конкретного студента
def increase_average(student, increment):
    name, average = student
    return (name, average + increment)

# Функция для увеличения среднего балла всех студентов
def increase_all_averages(students, increment):
    return [increase_average(student, increment) for student in students]

# Функция для получения среднего балла конкретного студента
def get_average(student):
    return student[1]

# Функция для получения среднего балла всех студентов
def get_all_averages(students):
    return [get_average(student) for student in students]

# Применение функций
students = increase_all_averages(students, 0.2)

for student in students:
    print(f"{student[0]}: новый средний балл = {student[1]}")

