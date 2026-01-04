class Student:
    def __init__(self, fname , lname , age , category):
        self.firstname = fname
        self.lastname = lname
        self.age = age 
        self.cate = category
        print("Adding Students into the Database")
    
s1 = Student("Atharva","Barve",21,"Hacker")
print("Full name = ",s1.firstname,s1.lastname)
print("Age = ",s1.age)
print("Category = ",s1.cate)
s2 = Student("Mitanshu","Bhanopa",19,"Noobda")
print("Full name = ",s2.firstname,s2.lastname)
print("Age = ",s2.age)
print("Category = ",s2.cate)
s3 = Student("Monty","Carlo",19,"Ladies")
print("Full name = ",s3.firstname,s3.lastname)
print("Age = ",s3.age)
print("Category = ",s3.cate)
