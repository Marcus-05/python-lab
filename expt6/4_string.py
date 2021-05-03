class uprcase:
    def __init__(self, string):
        self.string = string

    def print_upr(self):
        print(f"The string is {self.string.upper()}")


if __name__ == '__main__':
    musheer = uprcase("musheer")
    musheer.print_upr()