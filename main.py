import random 

name = input("What is your name? ")
print(f"\nWelcome to Master Mind {name}!")
lst_colors = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "cyan", "silver", "teal"]
lst_color_code = random.sample(lst_colors, 4)
print(f"Answer for demonstration purposes: {lst_color_code}")

def FourColors(lst_guess):
  '''Checks to see if the user input less or more than 4 colours'''
  p = False
  if len(lst_guess) != 4:
    p = True
  return p
  
def NonRecognizable(lst_guess):
  '''Checks to see if one of the inputs is not in the colour list'''
  p = False
  for x in lst_guess:
    if x not in lst_colors:
      p = True
      break
  return p

def MoreThanOne(lst_guess): 
  '''Checks to see if more than one inputs are the same'''
  p = False
  for x in lst_guess:
    if lst_guess.count(x) > 1:
      p = True
      break
  return p
     
# User playing the game

print("The code marker is here. Avaible colors are")
print("Red", "Yellow", "Blue", "Green", "Orange", "Pink", "Purple", "Cyan", "Silver", "Teal")
print("\nYou have 15 guesses, total of 5 penalties are allowed but avoid penalties.")
print("\nThe code marker selected 4 colors. ")
print(f"You can start guessing {name}.")


penalty = 0
e = False


for i in range(0, 15):
  PenaltyResponse = ""
  if penalty == 5:
    print(f"\n{name}, you lost the game by reaching the maximum number of allowed penalties.")
    break
  elif e:
    break

  for j in range(0, 1):
    guess = input(f"\nEnter your guess number {i+1} (Seperate every colour by a space): ")
    print("")
    lst_guess = list(guess.lower().split(" "))

# Penalty operation -----------------------------------------------------------------------
    if FourColors(lst_guess) and MoreThanOne(lst_guess) and NonRecognizable(lst_guess):
      print(f"Sorry {name}, you need to enter at least 4 colors for each guess. Also, repeated colors are not allowed in this game. On top of that, cannot recognize the colors you entered. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")
      
    elif NonRecognizable(lst_guess) and MoreThanOne(lst_guess):
      print(f"Sorry {name}, cannot recognize the colors you entered. Also, repeated colors are not allowed in this game. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")
      
    elif FourColors(lst_guess) and MoreThanOne(lst_guess):
      print(f"Sorry {name}, you need to enter at least 4 colors for each guess. Also,repeated colors are not allowed in this game. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")
      
    elif FourColors(lst_guess) and NonRecognizable(lst_guess):
      print(f"Sorry {name}, you need to enter at least 4 colors for each guess. Also, cannot recognize the colors you entered. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")

    elif FourColors(lst_guess):
      print(f"Sorry {name}, you need to enter at least 4 colors for each guess. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")

    elif NonRecognizable(lst_guess):
      print(f"Sorry {name}, cannot recognize the colors you entered. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")

    elif MoreThanOne(lst_guess):
      print(f"Sorry {name}, repeated colors are not allowed in this game. One penalty is considered.")
      penalty += 1
      print(f"Total penalties = {penalty}")
    
# Black and white operation ----------------------------------------------------------------
    else:
      black = 0
      white = 0
      for x in range(0, 4):
        for y in range(0, 4):
          if lst_guess[x] == lst_color_code[y] and x == y:
            black += 1
            break
          elif lst_guess[x] == lst_color_code[y] and x!=y:
            white += 1
            break
            
      if black == 4:
        print(f'''You got {black} blacks {name}.
You won the game with {i+1} guesses and {penalty} penalties. Congratulations!''')
        e = True
      else:
        print(f"You got {black} black, and {white} white for this guess.")
      
      
  if i == 14 and black != 4:
    print(f"\nSorry {name}, you ran out of guesses and you lost the game with {penalty} penalties.")