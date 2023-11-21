

from tkinter import *
window = Tk()
window.geometry("300x350")
window.title("Welcome")

class Student:

    def __init__(self, name, course, year):
        self.__name = name
        self.__course = course
        self.__year = year

    def getYear(self):
        return self.__year

    def isFinalYear(self):
        if self.__year == 4:
            return True
        else:
            return False

    def stepYear(self):
        if self.__year < 4:
            self.__year += 1
            return True
        else:
            return False

    def setCourse(self, courseName):
        self.__course = courseName

    def printDetails(self):
        print("Student Details:\n---------------\nName: {0}\nCourse: {1}\nYear: {2}".format(self.__name, self.__course, self.__year))


#------------end of class definition------------------
def main():
    s=Student("T.Lennon", "Software", 3)
    s.printDetails()
    year = s.getYear()
    print('\nCurrent Year = {0}'.format(year))

    result = s.isFinalYear()
    print('\nFinal Year? = {0}'.format(result))
    s.stepYear()
    result = s.isFinalYear()
    print('\nAfter Stepping: Final Year? = {0}'.format(result))
    result = s.stepYear()
    if (result==False):
        print('\nAlready in Final Year\n')
    s.setCourse("Electronics")
    s.printDetails()



main()
