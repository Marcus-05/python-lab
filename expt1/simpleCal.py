def add (d):
    a,b,c = input("Enter 3 number : ").split(" ")
    sum = int(a)+int(b)+int(c)
    print(f"The sum is {sum}")

def sub (d) :
    a,b,c = input("Enter 3 number : ").split(" ")
    sub1 = int(a)-int(b)-int(c)
    print(f"The sub is {sub1}")

def div (d):
    a,b,c = input("Enter 3 number : ").split(" ")
    div = int(a)/int(b)/int(c)
    print(f"The div is {div}")
    
def multi(d):
    a,b,c = input("Enter 3 number : ").split(" ")
    multi = int(a)*int(b)*int(c)
    print(f"The multi is {multi}")
    pass

def Myname(name):
    print(f"My name is {name}")
list = [add,sub,div,multi,Myname]

print("1 to add 2 to sub 3 to div 4 to multi")
i = int(input("Enter your choice : "))
list[i-1](i)


