"""
Advent of Code 2020: day 8
author: Joshua P.
"""

from collections import OrderedDict
from copy import deepcopy


def program_listing(fname: str) -> OrderedDict:
    with open(fname) as infile:
        pmap = OrderedDict()
        for idx, line in enumerate(infile):
            pmap[idx] = {'instr': line.rstrip(), 'uses': 0}
        return pmap


def execute(pmap: OrderedDict, max_uses: int = 1) -> tuple:
    def nop(_instr: str, _reg: int) -> tuple:
        return 1, _reg

    def acc(_instr: str, _reg: int) -> tuple:
        return 1, _reg + int(_instr.split('+')[-1] if '+' in _instr else '-' + _instr.split('-')[-1])

    def jmp(_instr: str, _reg: int) -> tuple:
        return int(_instr.split('+')[-1] if '+' in _instr else '-' + _instr.split('-')[-1]), _reg

    prog_ctr, reg = 0, 0
    op_map = {'nop': nop, 'acc': acc, 'jmp': jmp}
    while prog_ctr < len(pmap):
        pmap[prog_ctr]['uses'] += 1
        if pmap[prog_ctr]['uses'] > max_uses:
            break
        instr = pmap[prog_ctr]['instr']
        op = instr.split(' ')[0]
        nxt, reg = op_map[op](instr, reg)
        prog_ctr += nxt
    return prog_ctr, reg


def prog_correction(pmap: OrderedDict, _from: str, _to: str) -> tuple:
    for instr in {inst_idx for inst_idx in pmap if _from in pmap[inst_idx]['instr']}:
        mod_prog = deepcopy(pmap)
        mod_prog[instr]['instr'] = mod_prog[instr]['instr'].replace(_from, _to)
        halt, acc = execute(mod_prog, max_uses=3)
        if halt == len(mod_prog):
            return instr, acc
        mod_prog.clear()
    return None, -1


def reset_uses(pmap: OrderedDict) -> OrderedDict:
    [pmap[key].update({'uses': 0}) for key in pmap]
    return pmap


if __name__ == '__main__':
    # Part 1
    print(f'Part 1')
    program = program_listing('input_day8.txt')
    halt_instr, accum = execute(program)
    [print(f'\t{item}:{program[item]}') for item in program]
    print(f'\tHalt instruction: {halt_instr}, Accumulator: {accum}')

    # Part 2
    print(f'Part 2')
    mods = (('jmp', 'nop'), ('nop', 'jmp'))
    program = reset_uses(program)
    for mod in mods:
        op_from, op_to = mod
        modified_instr, accum = prog_correction(program, op_from, op_to)
        if modified_instr:
            print(f'\tProgram ending conditions:\n\tOriginal instr. to be modified ->'
                  f'{modified_instr:8}:{program[modified_instr]}, '
                  f'Accumulator: {accum}')
            break
