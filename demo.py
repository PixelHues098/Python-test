def print_square_matrix():
    print("\nHELLOOO! WELCOME TO PART 2: THE SQUARE MATRIX!\n")
    n = int(input("Enter the square matrix size: "))
    num = 1  
    for i in range(1, n * n + 1):
        print(f"{num:2}", end=" ")
        if i % n == 0:  
            print()
        num += 1  

def password_verification():
    """
    Verifies if the password is valid. The valid password is "python123".
    """
    print("\nHELLOOO! WELCOME TO PART 2: THE PASSWORD VERIFICATION!\n")
    valid_password = "python123"
    while True:
        password = input("Enter the password: ")
        if password == valid_password:
            print("Password is valid. Access granted!")
            break
        else:
            print("Invalid password. Try again.")

def print_even_numbers():
    """
    Prints even numbers between 1 and 100 without using a conditional statement.
    """
    print("\nHELLOOO! WELCOME TO PART 3: THE PRINT EVEN NUMBERS!")
    even_numbers = list(range(2, 101, 2))
    print("Even numbers between 1 and 100:")
    print(even_numbers)

def main():
    """
    Main function to display the menu and handle user choices.
    """
    print("\nWelcome to the menu! If you think this works, you already have done half the battle!")
    while True:
        print("\nMenu:")
        print("[1] Do Part 1")
        print("[2] Do Part 2")
        print("[3] Do Bonus")
        print("[0] Exit Application")
        choice = input("Enter your choice: ")

        if choice == "1":
            print_square_matrix()
        elif choice == "2":
            password_verification()
        elif choice == "3":
            print_even_numbers()
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
