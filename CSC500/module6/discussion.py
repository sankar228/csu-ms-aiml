def main():
    l = [1, "John", 100]

   

    print(f"original: {l}")
    
    # slice
    sl = l[1:2]
    print(f"slice: {sl}")
    sl.append("200")
    print(f"slice: {sl}")
    

    #append

    l.append(10)

    print(f"append: {l}")

   

    #insert

    l.insert(2, "1111 1st Terr, US xxxx")

    print(f"insert: {l}")

   

    #insert at random index

    # element will be added to the end of the list, if the index is greate than the size of the list

    l.insert(20, "xxx 2st Terr, US xxxx")

    print(f"insert at random index: {l}")

   

    #extend

    sub_list = [35, "Male"]

    l.extend(sub_list)

    print(f"extend: {l}")

   

    #remove

    l.remove(35)

    print(f"remove: {l}")

    ## when element not found, program will throw an exception

    #l.remove(40)

    #print(f"remove: {l}")

   

   

    # pop

    l.pop(2)

    print(f"pop: {l}")

   

    # clear

    l.clear()

    print(f"clear: {l}")
    
if __name__ == "__main__":
    main()