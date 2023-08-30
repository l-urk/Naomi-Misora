import os
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    clear_screen()
    print(r"@@@@@@@   @@@ @@@  @@@  @@@  @@@@@@@@   @@@@@@   @@@  @@@  @@@  ")
    print(r"@@@@@@@@  @@@ @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@  ")
    print(r"@@!  @@@  @@! !@@  @@!  @@@       @@!  @@!  @@@  @@!  !@@  @@!  ")
    print(r"!@!  @!@  !@! @!!  !@!  @!@      !@!   !@!  @!@  !@!  @!!  !@!  ")
    print(r"@!@!!@!    !@!@!   @!@  !@!     @!!    @!@!@!@!  @!@@!@!   !!@  ")
    print(r"!!@!@!      @!!!   !@!  !!!    !!!     !!!@!!!!  !!@!!!    !!!  ")
    print(r"!!: :!!     !!:    !!:  !!!   !!:      !!:  !!!  !!: :!!   !!:  ")
    print(r":!:  !:!    :!:    :!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:  ")
    print(r"::   :::     ::    ::::: ::   :: ::::  ::   :::   ::  :::   ::  ")
    print(r" :   : :     :      : :  :   : :: : :   :   : :   :   :::  :    ")
    print(r"@@@@@@@   @@@@@@ @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@              ")
    print(r"@@!  @@@ @@!  @@@  @!!   @@!@!@@@ @@!        @!!                ")
    print(r"@!@!@!@  @!@  !@!  @!!   @!@@!!@! @!!!:!     @!!                ")
    print(r"!!:  !!! !!:  !!!  !!:   !!:  !!! !!:        !!:                ")
    print(r":: : ::   : :. :    :    ::    :  : :: ::     :   Created by l_ ")
    print("")
    print("Main Menu:")
    print("1. Populate Victims Panel")
    print("2. ??? ")
    print("3. Options")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    # Options For User
    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    elif choice == '3':
        option_3()
    elif choice == '4':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please select a valid option.")
        main_menu()
        
    # Options Here \/
def option_1():
    clear_screen()
    print("Option 1 Screen:")
    # Add code for Option 1 here
    
    
    
    
    
    
    
    
    
    
    
    
    
    input("Press Enter to go back to the Main Menu.")
    main_menu()

def option_2():
    clear_screen()
    print("Option 2 Screen:")
    input("Press Enter to go back to the Main Menu.")
    main_menu()

def option_3():
    clear_screen()
    print("Option 3 Screen:")
    input("Press Enter to go back to the Main Menu.")
    main_menu()

if __name__ == "__main__":
    main_menu()