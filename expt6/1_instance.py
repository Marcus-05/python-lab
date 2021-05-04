class Student:
    def __init__(self, id, name, marks_lang, marks_math, marks_science):
        self.name = name
        self.id = id
        self.marks_lang = marks_lang
        self.marks_math = marks_math
        self.marks_science = marks_science

    def display(self):
        print(f"The Student Name is {self.name}")
        print(f"The Student Id is {self.id}")


if __name__ == '__main__':
    name = "MusheerAhmed"
    id = "1910053"
    marks_lang = 85
    marks_math = 95
    marks_science = 93
    musheer = Student(name, id, marks_lang, marks_math, marks_science)
    musheer.display()
    print(musheer.__dict__)
