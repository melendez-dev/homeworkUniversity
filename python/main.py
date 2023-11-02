def main():
    # ask the length array
    arr = []
    option = 1

    while(option != 0):
        showMenu()

        option_case = int(input("Select a option: ")) 
        option = option_case

        if option == 1:
            insertElements(arr)
        elif option == 2:
            showElements(arr)
        elif option == 3:
            sumElements(arr)
        elif option == 0:
            break
        else:
            print("The option is not valid")
        

def showMenu():
    print("Menu options: \n")
    print("1. Insert a number \n")
    print("2. show vector \n")
    print("3. sum all number \n")
    print("0. exit \n")

def insertElements(arr):
    n = int(input("number to insert: "))
    arr.append(n)

def showElements(arr):
    for i in arr: 
        print(i)

def sumElements(arr):
    num = 0

    for i in arr:
        num += i

    print("the total is ", num)



if __name__ == "__main__":
    main()


