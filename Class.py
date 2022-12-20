import json


class Person:
    # Construtor
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    # To String
    def __str__(self):
        return f"{self.name} ({self.age}) anos"

    def hello(self):
        print("Hello, my name is", self.name)


# Herança
class Student(Person):
    def __init__(self, id, name, age, school, course):
        super().__init__(id, name, age)
        self.school = school
        self.course = course

    # To String
    def __str__(self):
        return f"{self.name} ({self.age}) anos, {self.course} - {self.school}"


# -----------------------------------------------------------------------------------------------
person = Person(1, "Jhon", 32)
print(person.id, person.name, person.age)
print(person)
person.hello()

student = Student(1, "Kayque", 30, "Unifei", "Ciência da computação")
print(student)
student.hello()

convert = {
    "name": student.name,
    "age": student.age,
    "school": student.school,
    "course": student.course,
}

jsonNew = json.dumps(convert)
print(jsonNew)

jsonConverted = json.loads(jsonNew)
print(jsonConverted["name"], jsonConverted["age"], jsonConverted["course"])

try:
  print(x)
except NameError:
  print("Variable x is not defined", NameError)
except:
  print("Something else went wrong")
finally:
  print("The 'try except' is finished")