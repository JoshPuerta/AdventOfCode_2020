"""
Advent of Code 2020: day 3
author: Joshua P.
"""

from typing import Iterator


def input_parser(file_name: str) -> Iterator[tuple]:
    with open(file_name) as infile:
        for row, line in enumerate(infile):
            yield row, line.rstrip()


def tree_finder(levels: Iterator[tuple], _slope: tuple) -> Iterator[tuple]:
    col, n_trees = 0, 0
    n_right, n_down = _slope
    for row, level in levels:
        target_pos = col % (len(level))
        if row % n_down != 0:
            yield n_trees, level
            continue
        elif level[target_pos] == '#':
            n_trees += 1
            drawing = level[:target_pos] + 'X' + level[target_pos + 1:]
        else:
            drawing = level[:target_pos] + 'O' + level[target_pos + 1:]
        col += n_right
        yield n_trees, drawing


if __name__ == '__main__':

    # Part 1
    print(f'Part 1')
    iter_lines = input_parser('input_day3.txt')
    iter_checked_levels = tree_finder(iter_lines, (3, 1))

    for trees, draw_line in iter_checked_levels:
        print(f'\t{trees}:\t{draw_line}')

    # Part 2
    print(f'Part 2')
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    res_cache = {}

    for slope_id, slope in enumerate(slopes):
        iter_lines = input_parser('input_day3.txt')
        iter_checked_levels = tree_finder(iter_lines, slope)

        print(f'\tSlope: {slope}')
        for trees, draw_line in iter_checked_levels:
            print(f'\t\t{trees}:\t{draw_line}')
            res_cache[slope_id] = trees

    acc = 1
    for slope_id in res_cache.keys():
        print(f'Slope {slope_id} <{slopes[slope_id]}> -> {res_cache[slope_id]}')
        acc *= res_cache[slope_id]
    print(f'Awnser (tree mult.): {acc}')

