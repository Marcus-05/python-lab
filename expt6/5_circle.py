class circle:
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius

    def print_area(self):
        print(f"The area of the circle is {self.pi*self.radius**2}")

    def print_perimeter(self):
        print(f"The perimeter of the circle is {round(2*self.pi*self.radius,3)}")
if __name__ == '__main__':
    circle1 = circle(5)
    circle1.print_area()
    circle1.print_perimeter()
