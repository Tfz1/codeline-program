menu_options = {
    1: 'Print Pattern',
    2: 'Rotate Array ',
    3: ' Help',
    4: 'Exit',
}
 
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
def option1():
      n = int(input('Enter the number of rows for the pattern: '))
      for i in range(n, 0, -1):
        print("* " * i)

 
def option2():
    try:
        n = int(input("Enter the size of the array: "))
        k = int(input("Enter the number of rotations: "))
        arr = list(map(int, input("Enter the array elements: ").split()))

        k = k % n  

        rotated_array = [arr[(i - k) % n] for i in range(n)]
        print("Rotated array:", rotated_array)

    except ValueError:
        print("Invalid input. Please enter valid integers for n, k, and array elements.")
 
def option3():
     print(''' --Help-- 
           Option 1: Print a  pattern with 'n' rows of decreasing asterisks.
            Option 2: Rotate an array of  'n' elements of the right by  'k' steps.
            Option 3: Display this help message.
            Option 4: Exit the program.
        ''')
        
def option4():
    print('Exiting the program. Goodbye!')
    exit()
 
if __name__ == '__main__':
    while True:
        print("Welcome to the Menu-Based program!")
        print("Please select an option: ")
        print_menu()
        
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
            continue 

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
