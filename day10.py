'''
Advent of Code 2020: day 10
'''

from collections import defaultdict
from typing import DefaultDict

def adapter_collection(filename: str) -> list:
	with open(filename) as infile:
		adpt = sorted([int(line.rstrip()) for line in infile if line != '\n']) 
		return [0] + adpt + [adpt[-1] + 3]


def difference_collection(adapters: list) -> list:
	return [v-u for u, v in zip(adapters[:-1], adapters[1:])]


def adapter_arrangements(adapters: list) -> DefaultDict:

	def adapter_tree() -> DefaultDict:
		return defaultdict(adapter_tree)

	atree = adapter_tree()
	for adapter in adapters:
		atree = atree[adapter]
	return atree


if __name__ == '__main__':
	adapters = adapter_collection('input_day10.txt')
	diffs = difference_collection(adapters)
	ones, threes = diffs.count(1), diffs.count(3)
	print(f'Ones: {ones}, Threes: {threes} -> Mult: {ones * threes}')
	tree = adapter_arrangements(adapters)
	for n in tree:
		print(f'{tree[n]}')
