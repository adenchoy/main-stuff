import os
class Model:
    def __init__(self,FirstName,LastName,Gender,Mobile,Email,Age,Country,DressSize,OtherAgencies) -> None:
        self.__fName = FirstName
        self.__lName = LastName
        self.__gender = Gender
        self.__PhoneNo = Mobile
        self.__email = Email
        self.__age = int(Age)
        self.__country = Country
        self.__dress = int(DressSize)
        self.__Other = OtherAgencies
    def __repr__(self):
        return self.__fName
    def getter(self,sizelower, sizeupper, agelower, ageupper, country):
        if self.__age >= agelower and self.__age <= ageupper and self.__dress >= sizelower and self.__dress <= sizeupper and self.__country== country:
            return self
        else:
            pass
    def setter(self,FirstName,LastName,Gender,Mobile,Email,Age,Country,DressSize,OtherAgencies):
        try:
            if Country.lower() in ["brunei", "myanmar", "cambodia", "timor-leste", "indonesia", "laos", "malaysia", "philippines", "singapore", "thailand", "vietnam"]:
                self.__country = Country
        except ValueError:
            print("Not a valid country")
        try:
            if Gender.lower() in ["male","female","non-binary"]:
                self.__gender = Gender
        except ValueError:
            print("Not a valid gender")
        try:
            if Gender = Male and DressSize>=46 and DressSize <=58:
                self.__dress = DressSize
            elif Gender = Female and DressSize>=32 and DressSize <=48:
                self.__dress = DressSize 
        except ValueError:
            print("Not a valid dress size (male dress size between 46 - 58 or female dress size between 32 - 48 )")
        


list = []
try:
    with open("main-stuff/modeltest.txt","r") as f:
      f.readline()
      for i in f:
          
          parts = i.split(',')
          list.append(Model(*parts))
except OSError:
    print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())

for j in list:
    print(j.getter(0,50,0,60))