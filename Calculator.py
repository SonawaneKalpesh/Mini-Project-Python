def add(a,b):
    return a + b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

while True:

    print("Welcome Calculator Program")
    choice=input("Do you want to continue (y/n):")

    if choice == 'y':

            n=int(input("Enter First Number : "))
            n2=int(input("Enter Secound Number : "))
            op = input("add / sub / multi / div : ").strip().lower()

            match op:
                case "add":
                    print(add(n,n2))
                case "sub":
                    print(sub(n,n2))
                case "multi":
                    print(multi(n,n2))
                case "div":
                    print(div(n,n2))
                case _:
                    print("Invalid Operator")
    else:
        print("Thank You")
        break



