import random
import clrscr
import hl_game_data
import higher_lower_art

score = 0 #save the current score of the player
history = [] #keep track of the already used characters
user_won = True # just initialize to start the game
correct_guess = False #since the user have not made any guess yet

def pick_compare():
    """Randomly pick out an unused data"""
    global history
    
    comp = random.choice(hl_game_data.data) #pick a random data
    while comp in history: #if the data has been used in the game
        comp = random.choice(hl_game_data.data) # then pick another one
        
    history.append(comp) # after picking an unsed data, append to the history
    
    return comp

def result(user, compA, compB):
    """take in the user's choice and return the the result"""
    if compA["follower_count"] > compB["follower_count"]:
        return user == 'A'
    else:
        return user == 'B'

compareA = pick_compare()

while user_won == True:
    compareB = pick_compare()

    print(higher_lower_art.logo)
    
    if correct_guess == True: # if the user have made a correct gues, output the current score
        print(f"You're RIGHT! Current score: {score}")
        
    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
    
    print(higher_lower_art.vs)
    
    print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")

    user_choice = input("Who has more follower? Type 'A' or 'B': ").upper()
    while user_choice != 'A' and user_choice != 'B':
        user_choice = input("Please type 'A' or 'B': ").upper()
    user_won = result(user_choice, compareA, compareB)

    clrscr.clear() # clear the screen
    
    if user_won == False: # the user guess wrong, end the game
        print(higher_lower_art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        input("\nPress anything to exit") # prompt for the user to look at the score
    else: # user guess correctly, continue the game
        correct_guess = True
        score += 1
        if user_choice == 'B': #if the user guessed 'B'
            compareA = compareB #then replace compareA with B and pcik a new B from above


