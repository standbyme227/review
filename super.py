class Human:
    def __init__(self, gender, age):
        self.age = age
        self.gender = gender


class Employee:
    def __init__(self, age='dddd'):
        self.age = age


class Student(Human, Employee):
    def __init__(self, age, grade=0):
        super(Human, self).__init__(age)
        self.grade = grade


if __name__ == "__main__":
    student = Student(age=7, grade=5)
    print(student.age)
