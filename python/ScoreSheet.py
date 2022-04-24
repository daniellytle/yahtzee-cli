from ScoreType import ScoreType

class ScoreSheet:
    def __init__(self):
        self.score_types = [
            ScoreType(
                "ones",
                lambda dice_array: ScoreType.count_die_with_number(1, dice_array)
            ),
            ScoreType(
                "twos",
                lambda dice_array: ScoreType.count_die_with_number(2, dice_array)
            ),
            ScoreType(
                "threes",
                lambda dice_array: ScoreType.count_die_with_number(3, dice_array)
            ),
            ScoreType(
                "fours",
                lambda dice_array: ScoreType.count_die_with_number(4, dice_array)
            ),
            ScoreType(
                "fives",
                lambda dice_array: ScoreType.count_die_with_number(5, dice_array)
            ),
            ScoreType(
                "sixes",
                lambda dice_array: ScoreType.count_die_with_number(6, dice_array)
            ),
            ScoreType(
                "3 of a kind",
                lambda dice_array: ScoreType.n_of_a_kind([3], dice_array)
            ),
            ScoreType(
                "4 of a kind",
                lambda dice_array: ScoreType.n_of_a_kind([4], dice_array)
            ),
            ScoreType(
                "Full House",
                lambda dice_array: ScoreType.n_of_a_kind([2,3], dice_array, 25)
            ),
            ScoreType(
                "Small Straight",
                lambda dice_array: ScoreType.n_in_order(4, dice_array)
            ),
            ScoreType(
                "Large Straight",
                lambda dice_array: ScoreType.n_in_order(5, dice_array)
            ),
            ScoreType(
                "Yahtzee",
                lambda dice_array: ScoreType.n_of_a_kind([5], dice_array, 50)
            ),
            ScoreType(
                "Chance",
                lambda dice_array: sum(map(int, dice_array))
            ),
        ]
        self.scores = [None] * len(self.score_types)

    def is_filled(self):
        return len(list(filter(lambda x:x == None, self.scores))) == 0

    def evaluate_dice(self, dice_array):
        evalations = []
        for index, score_type in enumerate(self.score_types):
            if self.scores[index] == None:
                print("{: <4} {: <15} {: >2}".format(index, score_type.name, score_type.evaluate(dice_array)))

    def process_score(self, index, dice_array):
        self.scores[index] = self.score_types[index].evaluate(dice_array)

    def display(self):
        print("==== SCORE SHEET ====")
        for index, score_type in enumerate(self.score_types):
            print("{: <15} {: >2}".format(score_type.name, self.scores[index] or 0))
        print("---------------------")
        print("Total: {}".format(sum(map(lambda x: x or 0, self.scores))))
        print("=====================")
