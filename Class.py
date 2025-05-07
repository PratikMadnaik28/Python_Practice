class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print(f"Hii, {self.name} your avg score is: ", sum/3)

s1 = Student("Pratik", [99, 90, 95])
s1.get_avg()

s1.name = "Prit"
s1.get_avg() 