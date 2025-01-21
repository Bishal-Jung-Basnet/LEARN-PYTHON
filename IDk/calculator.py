
def add(num1, num2):
    return (num1 + num2)

def sub(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    if num2==0:
        return"error"
    else:
        return num1/num2
def calculator():
    while True:
        print("Select operator:")
        print("1. Add")
        print("2. Subtract")
        print("3.Multiply")
        print("4. Divide")
        print("5. Exit")
        answer=int(input("Enter your choice (1/2/3/4/5): "))
        if answer==5:
            print("Good bye")
            break
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        if answer==1:
            print(f"The sum of {a} and {b}:", add(a,b))
        elif answer==2:
            print(f"The diffeerence of {a} and {b} is:", sub(a,b))
        elif answer==3:
            print(f"The multiplication {a} and {b} is:", multiply(a,b))
        elif answer==4:
            print(f"The division of {a} and {b} is:", divide(a,b))
        else:
            print("Enter valid opeartior")
calculator()