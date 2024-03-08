class Course:

    def __init__(self, title, qualification, level):
        self.title = title 
        self.qualification = qualification
        self.level = level

    def readTitle(self):
        return self.title

    def readQualification(self):
        return self.qualification

    def readLevel(self):
        return self.level
    
    def stepLevel(self):
        self.level += 1

    def updateQualification(self, qualification):
        self.qualification = qualification
        
    def updateTitle(self, title):
        self.title = title 
            

class Student:

    def __init__(self, sno, name, address, ctitle, cqualification, clevel):
        self._sno = sno
        self._name = name
        self._address = address
        self._course = Course(ctitle, cqualification, clevel)

    def readStudentNo(self):
        return self._sno

    def readStudentName(self):
        return self._name

    def readAddress(self):
        return self._address

    def readCourseTitle(self):
        return self._course.title

    def readCourseQualification(self):
        return self._course.qualification

    def readCourseLevel(self):
        return self._course.level

    def stepCourseLevel(self):
        self._course.level += 1

    def updateAddress(self, address):
        self._address = address

    def updateCourseTitle(self, title):
        self._course.title = title

    def updateCourseQualification(self, qualification):
        self._course.qualification = qualification
