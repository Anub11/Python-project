class Employee:
    no_of_leaves=9

    def __init__(self,aname,asalary,aroll):
        self.name = aname
        self.salary = asalary
        self.roll = aroll

    def printdetails(self):
        return f"name : {self.name} salary : {self.salary} roll : {self.roll}"

    @classmethod
    def changeleves(cls, newleaves):
        cls.no_of_leaves=newleaves


harry = Employee("Harry", 255, "Instructor")

harry.changeleves(43)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
