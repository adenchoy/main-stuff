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
    with open("/Users/adenchoy/Desktop/main-stuff/main-stuff/modeltest.txt","r") as f:
      for i in f:
          i.split(",")
          list.append(Model())
except IOError:
    print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())
print(list)