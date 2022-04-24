from collections import Counter

class ScoreType:

    def __init__(self, name, evaluation):
        self.name = name
        self.evaluation = evaluation

    def evaluate(self, dice_array):
        return self.evaluation(dice_array)

    @staticmethod
    def count_die_with_number(n, dice_array):
        return n * len(list(filter(lambda x: x == n, dice_array)))

    @staticmethod
    def n_of_a_kind(n, dice_array, default_score=None):
        counter = Counter(map(int, dice_array))
        for num in n:
            if num not in counter.values():
                return 0
        return default_score or sum(map(int, dice_array))

    @staticmethod
    def n_in_order(length, dice_array):
        sorted_int_dice_array = sorted(map(int, dice_array))
        if (
            length == 5 and len(sorted_int_dice_array) == 5 and
            ScoreType.is_in_order(sorted_int_dice_array)
        ):
            return 40
        elif (
            length == 4 and
            (
                ScoreType.is_in_order(sorted_int_dice_array[1:]) or
                ScoreType.is_in_order(sorted_int_dice_array[:-1]) or
                (
                    ScoreType.is_in_order(list(set(sorted_int_dice_array))) and
                    len(list(set(sorted_int_dice_array))) == 4
                )
            )
        ):
            return 30
        else:
            return 0

    @staticmethod
    def is_in_order(array):
        for index, x in enumerate(array[1:]):
            if x != (1 + array[index]):
                return False
        return True
