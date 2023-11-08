from random import randrange


# A function that asks the user to provide a number between 0 and 10.
def userinput():
 x = input("Please enter in a numbers")
 return int(x)

# A function that returns a random number between 1 and 10.
def randomNum ():
 return (randrange(10))

 #A function that evaluates the randomly generated number against the user's guess
def guess():
  return (x == (randrange(10)))

x = userinput()
y = randomNum()
 
if y < x:
 print ("Number is too low")

elif  y > x:
    print("Number too high")

else:
  print("You guessed correct")