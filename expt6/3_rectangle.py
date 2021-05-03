class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"The area of the reatangle is {self.length*self.breadth}")


if __name__ == '__main__':
    
    rec = rectangle(12, 23)
    rec.area()
