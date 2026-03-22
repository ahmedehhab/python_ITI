class Office:

    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival = moveHour + (distance / velocity)
        return arrival > targetHour

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        self.employees = [e for e in self.employees if e.id != empId]
        Office.employeesNum -= 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for e in self.employees:
            if e.id == empId:
                return e