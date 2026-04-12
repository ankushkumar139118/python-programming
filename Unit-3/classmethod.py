class Student:
 

    def  ankush(self, name, marks):
        self.name = name
        self.marks = marks

    
    def display_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

obj = Student()
obj.ankush("Ankush", 456)
obj.display_details()