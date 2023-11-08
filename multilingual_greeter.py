def greet(name):
    print ("Hi " + name)


## Takes an argument called *name*. that meets the following criteria:
def name_input():
    name = input("Provide your name ")  
    return name


greet(name_input())


def language_input():
    print("Choose one of these lanuages")
    print ("1. Creole/ French")
    print ("2. English")
    print("3. Spanish")

    choice_of_language = input("Enter your number choice of the language you prefer")

    if choice_of_language == '1':
            chosen_language = "Creole/ French"
            name = input("Indiquez votre nom ")  
            print("Bonjour, " + name + "!")
    elif choice_of_language == '2':
            chosen_language = "English"
            name = input("Provide your name ")
            print("Hello " + name + "!")
    elif choice_of_language == '3':
            chosen_language = "Spanish"
            name = input("Proporciona tu nombre")
            print("Hola " + name + "!")
    else:
            print("Invalid input. Please choose number 1, 2, or 3")
    
# Call the language_input() function
while True:
      language_input()
      another_choice = input("Do you want to choose another language? (yes/no)")
      if another_choice != 'yes':
            break



    