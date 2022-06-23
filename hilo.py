from random import randint

class hilo:
    '''Hilo is a game in which the player guesses 
    if the next card drawn by the dealer will be 
    higher or lower than the previous one. Points 
    are won or lost based on whether or not the 
    player guessed correctly.
    '''
    def __init__(self):
        '''Initializes the game.
        '''
        self.card_draw = randint(1, 13)
        self.play_points = 300
        self.continue_game = True

    def __init__(self, player_points, continue_game):
        while continue_game == True:
            if self.card_draw <= 0:
                self.card_draw = randint(1, 13)
                print(f"The card is: {self.card_draw}")

            else:
                print(f"The card is: {self.card_draw}")

            guess = input("Higher or lower? [h/l] ")

            new_card_draw = randint(1, 13)
            print(f"Next card was: {new_card_draw}")

            if guess == "h":
                if (new_card_draw < self.card_draw):
                    player_points += 100
                
                elif (new_card_draw > self.card_draw):
                    player_points -= 75

                print(f"Your score is: {player_points}")

            if guess == "l":
                if (new_card_draw > self.card_draw):
                    player_points += 100
                
                elif (new_card_draw < self.card_draw):
                    player_points -= 75

                print(f"Your score is: {player_points}")

            question = input("Play again? [y/n] ")
            card_draw = new_card_draw
            
            if question.lower() == "y":
                continue_game = True

            elif question.lower() == "n":
                continue_game = False

            

            






'''
Variables:

player_points = 300
card_draw = random
guess = higher or lower
continue_game = True

if guess is right score +100
if guess wrong score -75
Lose at 0 points
While continue yes, decide to stop

'''