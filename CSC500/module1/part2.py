def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    mul = multiply(num1, num2)
    print(f"{num1} * {num2} = {mul}")
    
    div = divistion(num1, num2)
    print(f"{num1} / {num2} = {div}")
    
    
def multiply(num1, num2):
    return num1 * num2

def divistion(num1, num2):
    return num1 / num2


if __name__ == '__main__':
    main()