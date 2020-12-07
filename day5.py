"""
Advent of Code 2020: day 5
author: Joshua P.
"""

from typing import Iterator
from collections import OrderedDict


def input_parser(file_name: str) -> Iterator[str]:
    with open(file_name) as infile:
        for line in infile:
            if len(pload := line.rstrip()) == 10:
                yield pload


def seat_finder(bsp_seats: Iterator[str]) -> Iterator:
    def bsp_walk(path: str, _max: int) -> int:
        upper = _max
        lower = 0
        middle = (upper + lower) // 2
        for char in path:
            upper = middle if char in 'FL' else upper
            lower = lower if char in 'FL' else middle + 1
            middle = (upper + lower) // 2
        return lower

    for s in bsp_seats:
        r_str, c_str = s[:7], s[7:]
        if all(c in 'FB' for c in r_str) and all(c in 'LR' for c in c_str):
            r = bsp_walk(r_str, (2 ** len(r_str)) - 1)
            c = bsp_walk(c_str, (2 ** len(c_str)) - 1)
            s_id = r * 8 + c
            yield s, r, c, s_id


if __name__ == '__main__':

    # Part 1
    print(f'Part 1')
    max_id = 0
    seat_map = {}
    iter_lines = input_parser('input_day5.txt')
    for seat, row, col, seat_id in seat_finder(iter_lines):
        max_id = seat_id if seat_id > max_id else max_id
        seat_map[seat_id] = (row, col, seat)
        print(f'\tSeat[{row},{col}]\tid:{seat_id}\t{seat}')
    print(f'\tMax seat id: {max_id}')

    # Part 2
    print(f'Part 2')
    ord_seats = OrderedDict(sorted(seat_map.items()))
    first_seat = next(iter(ord_seats.keys()))
    intersection = set(range(first_seat, len(ord_seats))) - set(ord_seats.keys())
    print(f'\tMissing seat: {intersection}')
