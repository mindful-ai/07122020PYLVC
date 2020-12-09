class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __repr__(self):
        return (self.name.upper() + '  ---->  ' + str(self.salary))

    def __str__(self):
        return ("Name : " + self.name +  "  Salary: " + str(self.salary))

    def __len__(self):
        return len(self.name)
   
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Reference: ", self, " Name : ", self.name,  ", Salary: ", self.salary)

# ------------------------------ Applications/Test

emp1 = Employee("Kumar", 2000)
print("Reference of emp1 ", emp1)
emp2 = Employee("Abhinav", 5000)
print("Reference of emp2 ", emp2)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)


# ---------------------------------------------------


