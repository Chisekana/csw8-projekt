# functions.py: function definitions for csw8 final project
from main import *

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

def print_main_menu(the_menu):
    for key, value in the_menu.items():
        print(f"{key}: {value}")

print("Welcome to Alinjos Restaurant!")
print_main_menu(the_menu)
