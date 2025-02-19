class Student: 
    def __init__(self, name: str, dateOfBirth: str, examMark: int):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark
    def displayExamMark(self):
        print(f"{self.__name} got {self.__examMark} marks")


class PartTimeStudent(Student):
    def __init__(self, name: str, dateOfBirth: str, examMark: int):
        self.__isFullTime = False
        super().__init__(name, dateOfBirth, examMark)
    def time(self):
        return "Full time" if self.__isFullTime else "Part time"


class FullTimeStudent(Student):
    def __init__(self, name: str, dateOfBirth: str, examMark: int):
        self.__isFullTime = True
        super().__init__(name, dateOfBirth, examMark)
    def time(self):
        return "Full time" if self.__isFullTime else "Part time"


myStudent = Student("Example Exampleperson", "1989-06-04", 69)
myStudent.displayExamMark()
myFullStudent = FullTimeStudent("Dwayne Johnson", "1999-9-9", 80)
myPartStudent = PartTimeStudent("Jake Paul", "1999-9-9", 0)
myPartStudent.displayExamMark()
myFullStudent.displayExamMark()
