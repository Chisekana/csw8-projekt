from functions import *

if __name__ == "__main__":
    the_menu = {
        "L" : "List",
        "A" : "Add",
        "U" : "Update",
        "D" : "Delete",
        "M" : "Show average price",
        "S" : "Save the data to file",
        "R" : "Restore data from file",
        "Q" : "Quit this program"
    }

    while True:
        def print_main_menu(the_menu):
            print("Welcome to Alinjos Restaurant!")
            opt = input("Choose from our Menu: ").upper()

            if opt == "Q" or opt == 'q':
                print("Goodbye!\n")
            else:
                if opt in the_menu and opt != "Q" and opt != 'q':
                    print(f"You selected option {opt} to > {the_menu[opt]}.")
                else:
                    print(f"WARNING: {opt} is an invalid option.\n")

        print_main_menu(the_menu)

    print("Have a delicious day!")

