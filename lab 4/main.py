from car import Car
from employee import Employee
from office import Office


car = Car("Fiat128", 100, 60)

samy = Employee("Samy",5000,1,car,"samy@gmail.com",3000,20)

iti = Office("ITI Smart Village")

iti.hire(samy)

samy.drive(60)