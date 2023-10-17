def option1():
    n = ''
    n = int(input('Enter the number of rows for the pattern: '))

    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

def option2():
    try:
        n = int(input("Enter the size of the array: "))
        k = int(input("Enter the number of rotations: "))
        arr = list(map(int, input("Enter the array elements: ").split()))
        temp = []
        for i in range(n - k, n):
            temp.append(arr[i])
        for i in range(0, n - k):
            temp.append(arr[i])
        print("Rotated array: ", temp)
    except ValueError:
        print("Invalid input. Please enter valid integers for n, k, and array elements.")


# except ValueError:
#     print("Invalid input. Please enter valid integers for n, k, and array elements.")
    #
def option3():
    print(''' --Help-- 
           Option 1: Print a  pattern with 'n' rows of decreasing asterisks.
            Option 2: Rotate an array of  'n' elements of the right by  'k' steps.
            Option 3: Display this help message.
            Option 4: Exit the program.
        ''')

def option4():
    print('Exiting the program. Goodbye!')
    exit()  # This will terminate the program immediately

def menu():
    print("welcome to the Menue-Based program!")
    print("Please select an option:")
    print("1.Print Pattern")
    print("2.Rotate Array")
    print("3.Help")
    print("4.exit")
    option = int(input('Enter your choice: '))
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
if __name__ == '__main__':
    menu()



