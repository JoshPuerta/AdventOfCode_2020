"""
Advent of Code 2020: day 6
author: Joshua P.
"""

from collections import OrderedDict


def awnser_parser(filename: str, opt: str) -> OrderedDict:

    def individual(fname: str) -> OrderedDict:
        group_id = 0
        with open(fname) as infile:
            gmap = OrderedDict()
            gmap[group_id] = set()
            for line in infile:
                if line == '\n':
                    group_id += 1
                    gmap[group_id] = set()
                else:
                    gmap[group_id] |= set(line.rstrip())
            return gmap

    def everyone(fname: str) -> OrderedDict:
        group_id, pass_id = 0, 0
        with open(fname) as infile:
            gmap = OrderedDict()
            gmap[group_id] = OrderedDict()
            for line in infile:
                if line == '\n':
                    awnsers = [gmap[group_id][passenger] for passenger in gmap[group_id].keys()]
                    gmap[group_id]['awnsered'] = set.intersection(*awnsers)
                    group_id += 1
                    pass_id = 0
                    gmap[group_id] = OrderedDict()
                else:
                    gmap[group_id][pass_id] = set(line.rstrip())
                    pass_id += 1
            return gmap

    awnser_type = {'individual': individual, 'everyone': everyone}
    return awnser_type[opt](filename)


if __name__ == '__main__':

    print(f'Part 1')
    answered = 0
    group_map = awnser_parser('input_day6.txt', 'individual')
    for group in group_map.keys():
        answered += len(group_map[group])
        print(f'\tId:{group}, Awns.: {len(group_map[group])}\t\t{group_map[group]}')
    print(f'Awnsered: {answered}')

    print(f'\nPart 2')
    answered = 0
    group_map = awnser_parser('input_day6.txt', 'everyone')
    for group in group_map.keys():
        if 'awnsered' in group_map[group]:
            answered += (awnser := len(group_map[group]['awnsered']))
            print(f'\tId:{group}, Awns.: {awnser}\t\t{group_map[group]["awnsered"]}')
    print(f'Awnsered: {answered}')

