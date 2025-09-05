import random

COLORS = ["R", "G","B", "Y", "W", "O"]
TRIES = 10
codeLength = 4
# to make it more difficult we could go for less tries, more colors, length, etc

# here we ask the computer to randomly place the colors that the user can guess
def gameCode():
    code = []
    for _ in range(codeLength): # _ depicts an anonymous variable. Anyone could use i, x, etc
        color = random.choice(COLORS)
        code.append(color)
    return code
code = gameCode()

# now we allow user to guess the color code since it is a user based game.

def guessCode():# we want the user to input something
    # we want all of this to be true so it will go inside the while loop
    while True:
        guess = input("Guess: ").upper().split(" ") # here the split code would take all the input from user and convert it into a list by using spaces as elements in the list        
        # we have limited the length of color code to 4, we want the program to check if the length is 4 or not we do it suing if function
        if len(guess) != codeLength:
            print(f"Guess exactly {codeLength} colors separated by spaces")
            continue # this will bring me back to the top of while loop so that the program can continue to check if the user has given correct input
        # now we want to program to check if the colors choosen are from the list of colors. We do it using for and if statement
        
        valid = True
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Valid colors are: {', '.join(COLORS)}")
                valid = False
                break
        # it will check if the program broke out of the while loop or not. 
        # If nothing  invalid is encountered, then guessed colors are from the list. So "else break" would help break out of the while loop
        
        if valid: 
            # after looping through every single color the user inputs. 
            # If any of the color is not in the list then, we will prompt the user to give right colors from the list
            return guess

def checkCode(guess, realCode):
    # Step 1: Count correct positions (exact matches)
    correctPosition = 0
    for i in range(len(guess)):
        if guess[i] == realCode[i]:
            correctPosition += 1
    
    # Step 2: Count total matching colors
    real_counts = {}
    for color in realCode:
        real_counts[color] = real_counts.get(color, 0) + 1
        
    total_matches = 0
    for color in guess:
        if color in real_counts and real_counts[color] > 0:
            total_matches += 1
            real_counts[color] -= 1
    
    # Step 3: Incorrect positions = total matches - correct positions
    incorrectPosition = total_matches - correctPosition
    return correctPosition, incorrectPosition

def gamePlay():
    print(f"Welcome to MasterMind. Let's see how many colors you can guess in {TRIES} tries")
    print("The valid colors are", *COLORS)
    code = gameCode()
    for attempts in range(1, TRIES + 1):
        guess = guessCode()
        correctPostion, incorrectPosition = checkCode(guess, code)
        if correctPostion == codeLength:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct positions: {correctPostion} | Incorrect positions: {incorrectPosition}")
    else:
        print("You ran out of tries, the code was: ", *code)

if __name__ == "__main__":   
   gamePlay()
