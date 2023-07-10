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
    restaurant_menu_list = [
  { "name": "burrito",
    "calories": 500,
    "price": 12.90,
    "is_vegetarian": "yes",
    "spicy_level": 2
  },
  { "name": "rice bowl",
    "calories": 400,
    "price": 14.90,
    "is_vegetarian": "no",
    "spicy_level": 3
  },
  { "name": "fish",
    "calories": 1600,
    "price": 30.50,
    "is_vegetarian": "no",
    "spicy_level": 4
  },
  { "name": "margherita",
    "calories": 800,
    "price": 18.90,
    "is_vegetarian": "no",
    "spicy_level": 2
  },
  { "name": "kienyeji",
    "calories": 250,
    "price": 6.50,
    "is_vegetarian": "yes",
    "spicy_level": 1
  }
]
    list_menu = {
        "A":"Complete menu",
        "V":"Vegeterian dishes only"
    }
    spicy_scale_map = {
        1: "Not spicy",
        2: "Low key spicy",
        3: "Hot",
        4: "Diabolical",
    }
    while True:
        def print_main_menu(the_menu):
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

