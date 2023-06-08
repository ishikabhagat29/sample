student = {
    "student1" : "ishika",
    "student2": "neal",
    "student3": "purna",
    }

print(student.get("student1"))
print(student.get("student3"))
print(student.get("student4","irfan"))
#print(student["student4"])
a = 20 
print(student.get("student5",a))
t = student
print(t)
t.pop("student1")
print("this is t value:",t)
print("this is student ",student)

print(t.pop("student5",5))
print("this is t value:",t)
print("this is student ",student)

