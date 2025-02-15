def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    sum = add(num1, num2)
    print(f"{num1} + {num2} = {sum}")
    
    sub = subtract(num1, num2)
    print(f"{num1} - {num2} = {sub}")
    
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


if __name__ == '__main__':
    main()