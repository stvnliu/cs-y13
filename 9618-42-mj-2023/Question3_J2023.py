#3ai
class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle):
        self.__HourlyPay: float = HourlyPay # Real number
        self.__EmployeeNumber: str = EmployeeNumber # String
        self.__JobTitle: str = JobTitle # String
        self.__PayYear2022: list[float] = [0.0 for i in range(52)] # list of real numbers
    #3aii
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    #3aiii
    def SetPay(self, WeekNumber: int, NumberOfHoursWorked: int):
        WeekPay = NumberOfHoursWorked * self.__HourlyPay
        # index to WeekNumber - 1 because 52nd week would be 51st element, etc.
        self.__PayYear2022[WeekNumber - 1] = WeekPay
    #3aiv
    def GetTotalPay(self):
        RunningTotal = 0
        for pay in self.__PayYear2022:
            RunningTotal += pay
        return RunningTotal
#3bi
class Manager(Employee):
    def __init__(self, BonusValue, HourlyPay, EmployeeNumber, JobTitle):
        Employee.__init__(self, HourlyPay, EmployeeNumber, JobTitle)
        self.__BonusValue: float = BonusValue # Real
    #3bii
    def SetPay(self, WeekNumber: int, NumberOfHoursWorked: float):
        super().SetPay(WeekNumber, NumberOfHoursWorked * self.__BonusValue / 100)
#3c
EMPLOYEE_FILENAME = "Employees.txt"
global EmployeeArray
EmployeeArray = [None for i in range(8)]
with open(EMPLOYEE_FILENAME, 'r') as file:
    trimmed_lines: list[str] = [
        line.strip() 
        for line in file.readlines()
    ]
    file.close()
    i = 0
    count = 0
    while i < len(trimmed_lines):
        #print(f"[{i}] looking at:\n[{i}] {trimmed_lines[i]}\n[{i+1}] {trimmed_lines[i+1]}\n[{i+2}] {trimmed_lines[i+2]}\n[{i+3}] {trimmed_lines[i+3]}")
        HourlyPay = float(trimmed_lines[i])
        EmployeeNumber = trimmed_lines[i+1]
        EmployeeObject = None
        #print(f"Check: {trimmed_lines[i+2]}")
        try:
            float(trimmed_lines[i+2])
            # is manager
            # increment by one more because Managers need one more line
            BonusValue = float(trimmed_lines[i+2])
            JobTitle = trimmed_lines[i+3]
            EmployeeObject = Manager(BonusValue, HourlyPay, EmployeeNumber, JobTitle)
            i += 1
            #print(f"next line: {trimmed_lines[i]}")
        except ValueError:
            JobTitle = trimmed_lines[i+2]
            EmployeeObject = Employee(HourlyPay, EmployeeNumber, JobTitle)
        EmployeeArray[count] = EmployeeObject
        count += 1
        i += 3
#3d
def EnterHours():
    HOURS_WEEK_FILE = "HoursWeek1.txt"
    with open(HOURS_WEEK_FILE, 'r') as file:
        lines = [raw_str.strip() for raw_str in file.readlines()]
        file.close()
        i = 0
        while i < len(lines):
            employeeNumber = lines[i]
            employeeWorkedHours = float(lines[i+1])
            #print(employeeNumber)
            j = 0
            for person in EmployeeArray:
                #print(person)
                if person.GetEmployeeNumber() == employeeNumber:
                    #print("Yes")
                    person.SetPay(1, employeeWorkedHours)
            i += 2
#3ei
EnterHours()
for person in EmployeeArray:
    print(f"EmployeeNumber={person.GetEmployeeNumber()}, TotalPay={person.GetTotalPay()}")
#for i in EmployeeArray:
#    print(i)
