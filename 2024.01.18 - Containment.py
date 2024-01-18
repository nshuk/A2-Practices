class Lesson:
    def __init__(self, t, d, r):
        self.__lessonTitle = t
        self.__durationMinutes = d
        self.__requiresLab = r
    def outputLessonDetails(self):
        return self.__lessonTitle
class Assessment:
    def __init__(self, t, m):
        self.__assessmentTitle = t
        self.__maxMarks = m
    def outputAssessmentDetails(self):
        return self.__assessmentTitle

class Course:
    def __init__(self, t, m):
        self.__courseTitle = t
        self.__maxStudents = m
        self.__numOfLessons = 0
        self.__courseLesson = []  # datatype lesson array
        self.__courseAssessment = Assessment  # datatype assessment
    def addLesson(self, t, d, r):
        self.__numOfLessons = self.__numOfLessons + 1
        self.__courseLesson.append(Lesson(t, d, r))
    def addAssessment (self, t, m):
        self.__courseAssessment = Assessment(t, m)
    def outputCourseDetails(self):
        print(self.__courseTitle, "Maximum Number:", self.__maxStudents)
        for i in range(self.__numOfLessons):
            print(self.__courseLesson[i].outputLessonDetails())


myCourse = Course("Computing", 10)
myCourse.addAssessment("Programming", 100)
myCourse.addLesson("Problem Solving", 60, False)
myCourse.addLesson("Programming", 120, True)
myCourse.addLesson("Theory", 60, False)
myCourse.outputCourseDetails()

