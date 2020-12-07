"""
Advent of Code 2020: day 2
author: Joshua P.
"""

from typing import Iterator


def input_parser(file_name: str) -> Iterator[tuple]:
    # Format-> '8-12 g: gggggggggggmgg'
    with open(file_name) as infile:
        for line in infile:
            rules, pwd = [item.strip() for item in line.split(':')]
            interv, char = rules.split(' ')
            nmin, nmax = interv.split('-')
            yield pwd, char, int(nmin), int(nmax)


def password_policy(pwd_pload: Iterator[tuple], opt: str) -> Iterator[str]:
    def rep(pwd_data: Iterator[tuple]) -> Iterator[str]:
        for pwd, char, nmin, nmax in pwd_data:
            if nmin <= pwd.count(char) <= nmax:
                yield f'{char}[{pwd.count(char)}] -> {pwd}'

    def pos(pwd_data: Iterator[tuple]) -> Iterator[str]:
        for pwd, char, nmin, nmax in pwd_data:
            targets = {pwd[nmin - 1], pwd[nmax - 1]}
            if len(targets) == 1:
                continue
            elif char in targets:
                yield f'{char} is strict_subset({targets}) -> {pwd}'

    pol_selector = {'repetition': rep, 'position': pos}
    return pol_selector[opt](pwd_pload)


if __name__ == '__main__':

    # Part 1: Repetition, Part 2: Position
    policies = ['repetition', 'position']
    policy = 'position'

    if policy in policies:
        print(f'Policy is {policy}...')
        iter_pload = input_parser('input_day2.txt')
        for i, hit in enumerate(password_policy(iter_pload, policy), start=1):
            print(f'\t{i}: {hit}')
