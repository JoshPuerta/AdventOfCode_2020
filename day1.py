"""
Advent of Code 2020: day 1
author: Joshua P.
"""


def input_reader(filename: str) -> list:
    with open(filename) as infile:
        _expenses = [int(line.rstrip()) for line in infile]
    return _expenses


def target_expense_finder(expense_list: list, n_compo: int, target: int) -> tuple:

    def two_comp(_expenses: list, goal: int) -> tuple:
        for expense in _expenses:
            factor = goal - expense
            if factor in _expenses:
                return expense, factor

    def three_comp(_expenses: list, goal: int) -> tuple:
        for expense in _expenses:
            factor_a = expense
            sub_goal = goal - factor_a
            ret = two_comp(expenses, sub_goal)
            if ret:
                factor_b, factor_c = ret
                if (factor_b in expenses) and (factor_c in expenses):
                    return factor_a, factor_b, factor_c

    opt_map = {2: two_comp, 3: three_comp}
    return opt_map[n_compo](expense_list, target)


if __name__ == '__main__':

    # Part A
    expenses = input_reader('input_day1.txt')
    expense_a, expense_b = target_expense_finder(expenses, 2, 2020)
    print(f'Part1 >> 1: {expense_a}, 2: {expense_b} '
          f'Sum: {expense_a + expense_b} '
          f'Result: {expense_a * expense_b}')

    res = target_expense_finder(expenses, 3, 2020)
    if res:
        expense_a, expense_b, expense_c = res
        print(f'Part2 >> 1: {expense_a}, 2: {expense_b}, 3: {expense_c} '
              f'Sum: {expense_a + expense_b + expense_c} '
              f'Result: {expense_a * expense_b * expense_c}')

    # Part B
