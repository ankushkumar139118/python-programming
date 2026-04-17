class Student:

    def __init__(self):
        self.name = "Ankush"
        self.inner = self.Inner()   

    def ankush(self):
        print("Hii I am from the outer class")

    class Inner:   
        def innerShow(self):
            print("Hii I am from the inner class")



s = Student()
s.ankush()
s.inner.innerShow()