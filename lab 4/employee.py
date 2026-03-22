from person import Person


class Employee(Person):

    def __init__(self, name, money, emp_id, car,email, salary, distanceToWork):
        super().__init__(name, money)

        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = max(1000, value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            print("Invalid email")

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, velocity):
        self.car.run(velocity, self.distanceToWork)

    def refuel(self, gasAmount=100):
        if gasAmount < 0 :
            print("gasAmount can not be negative")
            return
        self.car.fuelRate += gasAmount

        