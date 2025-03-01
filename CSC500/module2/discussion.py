
def isXYValidStr(x, y) -> bool:
    if x != None and y != None:
        return True
    
def main():
    x = None
    y = " World !" 
    
    if isXYValidStr(x, y):
        print("valid string")
    else:
        print("invalid string")
                
    
if __name__ == "__main__":
    main()