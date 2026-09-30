class School:
    school_name = "Gyan chakshu High School"   

    def __init__(self, student_name, grade):
        self.student_name = student_name
        self.grade = grade

s1 = School("Sujan", "11")
s2 = School("AADIP", "10")

print(s1.school_name)
print(s2.school_name)

s1.school_name = "Peak point  School"

print("s1:", s1.school_name)
print("s2:", s2.school_name)
print("Class:", School.school_name)
