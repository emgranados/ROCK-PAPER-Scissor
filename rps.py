import random

game_moves = ['rock', 'paper', 'scissors']

"""This player always plays ROCK"""


class Player():
    def __init__(self):
        self.score = 0

    def play(self):
        return game_moves[0]

    def learn(self, their_move):
        pass


"""This player plays random"""


class Randomized(Player):
    def play(self):
        index = random.randint(0, 2)
        return game_moves[index]


"""This play remembers"""


class Recall(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def play(self):
        if self.their_move is None:
            return Player.play(self)
        return self.their_move

    def learn(self, their_move):
        self.their_move = their_move


"""This player Cycles through three moves"""


class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def play(self):
        move = None
        if self.last_move is None:
            move = Player.play(self)
        else:
            index = game_moves.index(self.last_move) + 1
            if index >= len(game_moves):
                index = 0
            move = game_moves[index]
        self.last_move = move
        return move


"""This is the user player"""


class HumanPlayer(Player):
    def play(self):
        player_move = input('Type your choice (' +
                            ', '.join(game_moves) + '):\n')
        while player_move not in game_moves:
            player_move = input('Well, that didnt work, try again\n')
        return player_move


"""These are the game play specifications."""
"""You can change ComputerPlayer to Random or recall."""


class Game():
    def __init__(self):
        self.player1 = HumanPlayer()
        self.player2 = ComputerPlayer()

    def play_game(self):
        input('Let\'s play Rock, Paper or Scissors!' +
              '\nPress enter to play\n')
        try:
            while True:
                self.play_round()
                print('The score is: ' + str(self.player1.score) + ' x ' +
                      str(self.player2.score) + '\n')
                input('Press enter to play again or ctrl+C to leave\n')
        except KeyboardInterrupt:
            print('\n\nThanks for playing! Come back again!')
            if self.player1.score > self.player2.score:
                print('Player 1 you won!')
            elif self.player1.score > self.player2.score:
                print('I am sorry. Player 2 won!')
            else:
                print('The game was a tie! No one won!')
            print('The final score was ' + str(self.player1.score) + ' x ' +
                  str(self.player2.score))

    def play_round(self):
        player1_move = self.player1.play()
        player2_move = self.player2.play()
        result = Game.score_check(player1_move, player2_move)
        self.player1.learn(player2_move)
        self.player2.learn(player1_move)
        print('Player 1 typed "' + player1_move + '" and player 2 typed "' +
              player2_move + '"')
        if result == 1:
            self.player1.score += 1
            print('=> Player 1 won!\n')
        elif result == 2:
            self.player2.score += 1
            print('=> Try again, player 2 rocked it!\n')
        else:
            print('=> Tie!Try again!\n')

    @classmethod
    def score_check(cls, move1, move2):
        if Game.winner(move1, move2):
            return 1
        elif Game.winner(move2, move1):
            return 2
        else:
            return 0

    @classmethod
    def winner(cls, move1, move2):
        if (move1 == 'rock' and move2 == 'scissors'):
            return True
        elif (move1 == 'scissors' and move2 == 'paper'):
            return True
        elif (move1 == 'paper' and move2 == 'rock'):
            return True
        return False


game = Game()
game.play_game()
