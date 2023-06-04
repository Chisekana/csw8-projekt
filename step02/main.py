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
  {
    "name": "ugali",
    "calories": 500,
    "price": 12.50,
    "is_vegetarian": "no",
    "spicy_level": 1
  },
  {
    "name": "pilau bowl",
    "calories": 400,
    "price": 18.90,
    "is_vegetarian": "yes",
    "spicy_level": 3
  },
  {
    "name": "nyama",
    "calories": 800,
    "price": 25.90,
    "is_vegetarian": "no",
    "spicy_level": 4
  },
  {
    "name": "kienyeji",
    "calories": 250,
    "price": 5.90,
    "is_vegetarian": "yes",
    "spicy_level": 2
  }
]

    list_menu = {
        "A": "complete menu",
        "V": "vegetarian dishes only",
    }

    spicy_scale_map = {
        1: "Not spicy",
        2: "Low key spicy",
        3: "Hot",
        4: "Diabolical",
    }
 
    
    opt = None

    while True:
        def print_main_menu(menu):
            print("Welcome to Alinjos Restaurant!")
        opt = input("How may I assist you ?")

        if opt == "Q" or opt == "q":
            print("Goodbye!\n")
            break
        else:
            if opt == "L" or "A" or "U" or "D" or "M" or "S" or "R":
                print(f"You selected option {opt} to > {the_menu[opt]}")
            else:
                print(f"WARNING: {opt} is an invalid option.\n")
            #list_helper(list_menu, restaurant_menu_list, spicy_scale_map)


    print("Have a delicious day!")