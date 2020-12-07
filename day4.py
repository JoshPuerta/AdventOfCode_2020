"""
Advent of Code 2020: day 4
author: Joshua P.
"""

from typing import Iterator


def input_parser(file_name: str) -> Iterator[dict]:

    def passport_to_dict(_passport: str) -> dict:
        return {field.split(':')[0]: field.split(':')[1] for field in _passport.rstrip().split(' ')}

    with open(file_name) as infile:
        passport = ''
        for line in infile:
            if line != '\n':
                passport += (line.replace('\n', ' '))
                continue
            else:
                yield passport_to_dict(passport)
                passport = ''
        if passport:
            yield passport_to_dict(passport)


def passport_validator(passports: Iterator[dict], policy: str) -> Iterator[dict]:

    def simple(_passports: Iterator[dict]) -> Iterator[dict]:
        n_fields = 8
        for passport in _passports:
            if (len(passport) == n_fields) or (len(passport) == (n_fields - 1) and ('cid' not in passport.keys())):
                yield passport

    def strict(_passports: Iterator[dict]) -> Iterator[dict]:

        def byr(pport: dict) -> int:
            return 1 if 1920 <= int(pport['byr']) <= 2002 else 0

        def iyr(pport: dict) -> int:
            return 1 if 2010 <= int(pport['iyr']) <= 2020 else 0

        def eyr(pport: dict) -> int:
            return 1 if 2020 <= int(pport['eyr']) <= 2030 else 0

        def hgt(pport: dict) -> int:
            if 'cm' in pport['hgt']:
                return 1 if 150 <= int(pport['hgt'][:-2]) <= 193 else 0
            elif 'in' in pport['hgt']:
                return 1 if 59 <= int(pport['hgt'][:-2]) <= 76 else 0
            else:
                return 0

        def hcl(pport: dict) -> int:
            # format -> #123abc
            if len(pport['hcl']) == 7:
                return 1 if (pport['hcl'][0] == '#') \
                            and (all((c in '0123456789abcdef') for c in pport['hcl'][1:])) else 0
            return 0

        def ecl(pport: dict) -> int:
            return 1 if (pport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}) else 0

        def pid(pport: dict) -> int:
            return 1 if (len(pport['pid']) == 9) and (pport['pid'].isdigit()) else 0

        rules = (byr, iyr, eyr, hgt, hcl, ecl, pid)
        for passport in simple(_passports):
            passed_tests = sum([rule(passport) for rule in rules])
            if passed_tests == len(rules):
                yield passport

    policy_map = {'simple': simple, 'strict': strict}
    return policy_map[policy](passports)


if __name__ == '__main__':

    # Part 1
    print(f'Part 1')
    iter_passports = input_parser('input_day4.txt')
    iter_valid_pports = passport_validator(iter_passports, 'simple')
    for idx, valid_passport in enumerate(iter_valid_pports, start=1):
        print(f'\t{idx}\tPassport:\t{valid_passport}')

    # Part 2
    print(f'\nPart 2')
    iter_passports = input_parser('input_day4.txt')
    iter_valid_pports = passport_validator(iter_passports, 'strict')
    for idx, valid_passport in enumerate(iter_valid_pports, start=1):
        print(f'\t{idx}\tPassport:\t{valid_passport}')
