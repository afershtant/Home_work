class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else: lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for ads in self.grades.values():
            all_grades.extend(ads)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avr = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avr}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {self.finished_courses}'

    def __gt__(self, other):
        if isinstance(other, (Student, Lecturer)):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (Student, Lecturer)):
            return self.average_grade() <= other.average_grade()
        return NotImplemented



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n Фамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for ads in self.grades.values():
            all_grades.extend(ads)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avr = self.average_grade()
        return f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {avr}'

def average_grade_all_students(students,course):
    all_course = []
    for student in students:
        if course in student.grades:
            all_course.extend(student.grades[course])
    return sum(all_course) / len(all_course) if all_course else 0

def average_grade_all_lecturers(lecturers,course):
    all_course = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_course.extend(lecturer.grades[course])
    return sum(all_course) / len(all_course) if all_course else 0









some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_2 = Reviewer('Alex', 'Oushen')
some_reviewer_1.courses_attached = ['Python', 'Git']

some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_2 = Lecturer('Anna', 'Petter')
some_lecturer_1.grades = {'Python': [10, 3]}
some_lecturer_2.grades = {'Python для начинающих': [8, 3,2]}
lecturers = [some_lecturer_1, some_lecturer_2]
some_lecturer_1.courses_attached = ['Python']
some_lecturer_2.courses_attached = ['Python для начинающих']



some_student_1 = Student('Ruoy', 'Eman')
some_student_2 = Student('David', 'Patty')
students = [some_student_1, some_student_2]
some_student_1.courses_in_progress = 'Python', 'Git'
some_student_1.finished_courses = 'Введение в программирование'
some_student_1.grades = {'Python': [10,10,10,10,10,10], 'Git': [9,10,10,10]}
some_student_2.courses_in_progress = ['Python']
some_student_2.finished_courses = []
some_student_2.grades = {'Python': [8, 9, 7]}

print(some_student_1 > some_lecturer_1)

print(average_grade_all_students(students,'Python'))
print(average_grade_all_lecturers(lecturers,'Python'))



#print(some_reviewer_1)
#print(some_reviewer_2)
#print(some_lecturer_1)
#print(some_lecturer_2)
#print(some_student_1)