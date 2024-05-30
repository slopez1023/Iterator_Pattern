from Employee import Employee
from Organization import Organization

ceo = Employee('Santiago', 'CEO')
cto = Employee('Camilo', 'QA')
dev1 = Employee('Felipe', 'DESARROLLADOR')
dev2 = Employee('Martin', 'DESARROLLADOR')
cfo = Employee('Andres', 'ARQUITECTO')
accountant = Employee('Maria', 'PROJECT MANAGER')

ceo.add_subordinate(cto)
ceo.add_subordinate(cfo)
cto.add_subordinate(dev1)
cto.add_subordinate(dev2)
cfo.add_subordinate(accountant)

organization = Organization(ceo)

for employee in organization:
    print(employee)