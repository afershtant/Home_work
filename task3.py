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
    
     def __gt__(self, other):
        if isinstance(other, (Lecturer, Student)):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (Lecturer, Student)):
            return self.average_grade() <= other.average_grade()
        return NotImplemented









some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [10, 3]}
some_student = Student('Ruoy', 'Eman')
some_student.courses_in_progress = 'Python', 'Git'
some_student.finished_courses = 'Введение в программирование'
some_student.grades = {'Python': [10,10,10,10,10,10], 'Git': [9,10,10,10]}
print(some_student > some_lecturer)








print(some_reviewer)
print(some_lecturer)
print(some_student)