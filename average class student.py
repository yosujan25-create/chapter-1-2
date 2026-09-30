class Student:
    def __init__(self, name, p1, p2, p3):
        self.name = name
        self.m1 = p1
        self.m2 = p2
        self.m3 = p3

    def average(self):
        avg = (self.p1 + self.p2 + self.p3) / 3
        print(f"Average marks of {self.name}: {avg}")


s1 = Student("Sujan", 50, 60, 70)
s1.average()
