# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Inheritance
from introduction.lesson_2.oop.person import Person


class Student(Person):
    school = "UOIT"

    def __init__(self, sid=None, name=None):
        self.sid = sid
        self.name = name

    def print_info(self):
        print('{0} is a student of {1}, whose student number is {2} and age is {3}'.format(self.name, self.school, self.sid, self.age))

    def speak(self):
        print('I am a university student.')