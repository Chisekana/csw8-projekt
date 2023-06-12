# Step 2 - Intro, and “Quit” option

Restaurant Menu Management System - help with managing a database containing a restaurant’s menu items (i.e. the food and beverage items that would appears on their printed menu, or a display menu on a computer monitor, for example.)


Below features will be implementented for this system:

a. Create an interface that allows the users to interact with the system (will use while True and input() to collect user data).
b. Create a collection to store menu item information that the users can view and maintain by adding and editing entries.
c. Allow the user to save the state of the system by saving the information to file and retrieving it from it.


File 1 - functions.py file
Contains all the relevant Functions
*added the print_main_menu() to the functions.py
*The print_main_menu() function does not return anything, it just prints the correctly-formatted options that are provided in the dictionary.

File 2 - main.py
Contains the Main program
*the_menu dictionary defined
*printed by the print_main_menu() function when the user starts this system.

File 3 - tests.py
Contains the test code. Assert staments collected to help verify that implementation of each function is correct.
Test file is run separately since running the main program will not automatically execute the assert statements. Each function that returns values will need to have the corresponding assert statements to check its correctness. We'll have at least three assert statements for each function.