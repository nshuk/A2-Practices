# lessontype and instructor in constructor

class Lesson:
    def __init__(self):
        self.__LessonType = None # None is used when there is an absence of value
        self.__Instructor = None
    def SetLessonType(self, n):
        self.__LessonType = n
    def SetInstructor(self, n):
        self.__Instructor = n
    def GetLessonType(self):
        return self.__LessonType
    def GetInstructor(self):
        return self.__Instructor
    def GetFee(self, p):
        if p == "B":
            fee = "$45"
            return fee
        elif p == "I":
            fee = "$50"
            return fee
        elif p == "A":
            fee = "$55"
            return fee
        else:
            return -1

myLesson = Lesson()
myLesson.SetLessonType("Improve Your Serve")
myLesson.SetInstructor("David")

print(myLesson.GetLessonType())
print(myLesson.GetInstructor())





