def greet(name):
    print ("Hi " + name)


## Takes an argument called *name*. that meets the following criteria:
def name_input():
    name = input("Provide your name ")  
    return name


greet(name_input())


def language_input():
    print("Choose one of these lanuages")
    print ("1. Creole")
    print ("2. English")
    print("3. Spanish")

while True:
    try:
        usersChoice = int(input("Enter your number choice"))
        if choice == 1:
            chosen_language = "Creole"
        elif choice == 2:
            chosen_language = "English"
        elif choice == 3:
            chosen_language == "Spanigh"
        else:
            print("Invalid input")
            continue

        



    