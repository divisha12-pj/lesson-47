#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name.
#  Create a child class Student (attributes - fname, lname, year).
#  Access the attributes of parent class in child class using super() function.
#  Then, create an object for the child class and call the display method to display the full name. Also, print the graduation year.


class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def display(self):
        print("first name of student is",self.fname,"and last name is",self.lname)

#child class
class student(person):
    def __init__(self,fname,lname,gradyear):
        self.gradyear=gradyear
        super().__init__(fname,lname)

student1=student("Ayana","jain",2026)
student1.display()
print("The graduation year is",student1.gradyear)