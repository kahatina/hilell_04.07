class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'

class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self) -> str:
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= 10:
            raise StudentLimitError("Досягнутий максимальний ліміт студентів")
        self.group.add(student)


    def delete_student(self, last_name: str) -> None:
        result = self.find_student(last_name)
        if result:
            self.group.discard(result)


    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students_list = []
        for student in self.group:
            all_students_list.append(str(student))
        all_students = '\n'.join(all_students_list)
        return f'Number:{self.number}\n{all_students} '

class StudentLimitError(Exception):
    pass

group1 = Group('PD1')

for i in range(1, 11):
    group1.add_student(Student('Male', 21, f'Ім`я{i}', f'Прізвище{i}', f'Група{i}'))

try:
    print("\nСпроба додати 11-го студента...")
    student11 = Student('Female', 22, 'Одинадцята', 'Студентка', 'Група11')
    group1.add_student(student11) # Цей рядок спровокує помилку
except StudentLimitError as e:
    print(f"Помилка: {e}")