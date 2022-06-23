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

    def game_loop(self, card_draw, player_points, continue_game):
        while continue_game == True:
            if card_draw <= 0:
                card_draw = randint(1, 13)
                print(f"The card is: {card_draw}")

            else:
                print(f"The card is: {card_draw}")

            guess = input("Higher or lower? [h/l] ")

            new_card_draw = randint(1, 13)
            print(f"Next card was: {new_card_draw}")

            if guess == "h":
                if (new_card_draw > card_draw):
                    player_points += 100

                elif (new_card_draw < card_draw):
                    player_points -= 75

                elif (new_card_draw == card_draw):
                    print("No points for you!")

                print(f"Your score is: {player_points}")

            if guess == "l":
                if (new_card_draw < card_draw):
                    player_points += 100

                elif (new_card_draw > card_draw):
                    player_points -= 75

                elif (new_card_draw == card_draw):
                    print("No points for you!")                    

                print(f"Your score is: {player_points}")

            question = input("Play again? [y/n] ")
            card_draw = new_card_draw

            if question.lower() == "n":
                continue_game = False
                

hilo().game_loop(hilo().card_draw, hilo().play_points, hilo().continue_game)