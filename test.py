class Employee():
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

emp1 = Employee('Aden','Choy',30000)
print(emp1.lname)
print(emp1.pay)