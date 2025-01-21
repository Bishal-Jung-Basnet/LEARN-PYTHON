import random
def main():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    x = num1 + num2

    answer = int(input(f"Enter sum of {num1} and {num2}: "))
    if(answer==x):
        print("Correct answer!")
    else:
        print(f"Incorrect answer, correct answer is {x}")
    
main()