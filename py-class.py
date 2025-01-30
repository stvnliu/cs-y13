class Student: 
    def __init__(self, name: str, dateOfBirth: str, examMark: int):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark
    def displayExamMark(self):
        print(f"{self.__name} got {self.__examMark} marks")

myStudent = Student("Example Exampleperson", "1989-06-04", 69)
myStudent.displayExamMark()
