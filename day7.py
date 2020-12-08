"""
Advent of Code 2020: day 7
author: Joshua P.
"""


def bag_map_builder(fname: str) -> dict:
    rule_map = dict()
    with open(fname) as infile:
        for line in infile:
            key, pload = line.rstrip().split(' bags contain ')
            pload = pload.replace(' bags', '').replace(' bag', '').replace('.', '').strip().split(', ')
            rule_map[key.rstrip()] = {bag.split(' ', 1)[1]: bag.split(' ', 1)[0] for bag in pload}
    return rule_map


def pathfinder(bagmap: dict, start: str, target: str) -> list:
    # A not-so-fine breadth-first search algorithm
    q = [start]
    while q:
        bag = q.pop(0)
        for nbor in bagmap[bag].keys() - set(q):
            if nbor == target:
                return q + [nbor]
            elif nbor == 'other':
                continue
            else:
                q.append(nbor)


def unroller(bagmap: dict, start: str) -> int:
    acc = 0
    for nbor in bagmap[start]:
        if nbor == 'other':
            return 0
        else:
            inc = int(bagmap[start][nbor])
            acc += (inc + (inc * int(unroller(bagmap, nbor))))
    return acc


if __name__ == '__main__':

    # Part 1
    print(f'Part 1')
    bags = bag_map_builder('input_day7.txt')
    found = 0
    for key in bags.keys():
        if path := pathfinder(bags, key, 'shiny gold'):
            found += 1
            print(f'\t{key:20}\tPath:\t{path}')
    print(f'\tFound: {found}')

    unrolled = unroller(bags, 'shiny gold')
    print(f'Part 2 -> shiny gold bags: {unrolled}')
