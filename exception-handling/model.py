import os
class Model:
    def __init__(self,FirstName,LastName,Gender,Mobile,Email,Age,Country,DressSize,OtherAgencies) -> None:
        self.__fName = FirstName
        self.__lName = LastName
        self.__gender = Gender
        self.__PhoneNo = Mobile
        self.__email = Email
        self.__age = Age
        self.country = Country
        self.dress = DressSize
        self.Other = OtherAgencies


list = []
try:
    with open("modeldata.txt","r") as f:
      for i in f:
           list.append(Model(i))
except IOError:
    print(os.path.isfile('modeldata.txt'))
print(list)