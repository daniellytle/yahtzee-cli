from Die import Die
from ScoreSheet import ScoreSheet
from ScoreType import ScoreType
import os

class YahtzeeGame:
    def __init__(self):
        import os
        self.dice = [
            Die(),
            Die(),
            Die(),
            Die(),
            Die()
        ]
        self.score_sheet = ScoreSheet()

    def play(self):
        print("LET'S PLAY YAHTZEE!")
        while(not self.score_sheet.is_filled()):
            self.play_turn()
            os.system('clear')
            self.score_sheet.display()
            input("Press any key to continue..")
        os.system('clear')
        print("GAME OVER!")
        self.score_sheet.display()

    def show_die(self):
        output = []
        for die in self.dice:
            output += [str(die)]
        print("----------")
        print("| " + " ".join(output) + " |")
        print("----------")

    def play_turn(self):
        roll = 0
        dice_to_roll = [0,1,2,3,4]
        while roll < 3:
            os.system('clear')
            print("Your dice:")
            self.roll_dice(dice_to_roll)
            self.score_sheet.evaluate_dice(self.dice)
            if roll == 2:
                self.process_score()
            else:
                if (self.prompt_score()):
                    break
                dice_to_roll = self.prompt_dice_to_roll()
            roll += 1


    def prompt_score(self):
        valid = False
        while not valid:
            save_score = input("Save a score? enter y/n: ")
            if save_score == "y":
                self.process_score()
                return True
            elif save_score == "n":
                return False

    def process_score(self):
        valid = False
        while not valid:
            input_index = input("Which score? enter index: ")
            if input_index.isdigit():
                valid = True
                index = int(input_index)
                self.score_sheet.process_score(index, self.dice)

    def prompt_dice_to_roll(self):
        valid = False
        while not valid:
            dice_to_roll = map(int,input("Which dice to re-roll? enter (1 2 3): ").strip().split(" "))
            return dice_to_roll

    def roll_dice(self, die_numbers = [0,1,2,3,4]):
        for die_number in die_numbers:
            self.dice[die_number].roll()
        self.print_dice()

    def print_dice(self):
        print(" ----------- ")
        print("| " + " ".join(map(str, self.dice)) + " |")
        print(" ----------- ")
