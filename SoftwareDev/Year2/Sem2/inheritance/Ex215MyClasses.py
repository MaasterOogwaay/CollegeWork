class Person:

    def __init__(self,name, age):
        self._name = name
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def stepAge(self):
        self._age += 1

    # Extended Class

class Student(Person):
    def __init__(self, name, age, course, year):
        super().__init__(name, age)
        self.__course = course
        self.__year = year

    def stepYear(self):
        self.__year += 1

    def getYear(self):
        return self.__year

    def getCourse(self):
        return self.__course

    def updateCourse(self, newCourse):
        self.__course = newCourse