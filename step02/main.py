from functions import *

if __name__ == "__main__":
    the_menu = {    
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "H" : "Display restaurant expense rating",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
}
    opt = None

    while True:
        def print_main_menu(the_menu):
            print()
        opt = input("Welcome. What would you like to Order?")

        if opt == "Q" or opt == "q":
            print("Goodbye!\n")
            break # exit the main `while` loop
        else:
            if opt != "Q" or opt != "q" in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
                print(f"You selected option {opt} to > {the_menu[opt]}.")
            else:
                print(f"WARNING: {opt} is an invalid option.\n")

    print("Have a delicious day!")
