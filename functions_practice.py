# Function 1 - hello()
# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
# --------------------------------------------------

def hello():
    print("Hello World!")

hello()

# Function 2 - pack()
# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

# --------------------------------------------------
# - First attempt, but realized I have to pass three arguments into the function not a list

# def pack(things):
#     for items in things:
#         print(items)

# things = ["Toothbrush", "Deodorant", "Medicine"]

# pack(things)

def pack(item1, item2, item3):
    return[item1, item2, item3]

print (pack("Toothbrush", "Deodorant", "Medicine"))

# Function 3 - eat_lunch()
# This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
# ---------------------------------------------------

def eat_lunch(lunch_list):
    if len(lunch_list) == 0: # Use len() to return numerical value of how many items are in the lunch_list. "Hamburger" and "Hotdog" would return a value of 2
        print("My lunchbox is empty")
    else:
        for lunches in range(len(lunch_list)): # For loop to iterate thru each item in the lunch_list using len()
            if lunches == 0: # If its the first item in the list
                print(f"First I eat {lunch_list[0]}")
            else: # Else iterate thru all other items in list
                print(f"Next I eat {lunch_list[lunches]}")        
eat_lunch([])
eat_lunch(["Hamburger"])
eat_lunch(["Hamburger", "Hotdog", "Sandwich", "Pizza"])




