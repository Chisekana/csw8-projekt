from functions import *
from main import *

assert opt == "Q" or opt == 'q', "Input option Q/q breaks the loop and prints 'Goodbye!'"

assert opt in the_menu and opt != "Q" and opt != 'q', "Valid options prints corresponding menu items."

assert opt not in the_menu and opt != "Q" and opt != 'q', "Invalid option displays warning message."