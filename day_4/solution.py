# https://adventofcode.com/2024/day/4

from itertools import product

target_word = 'XMAS'


def is_xmas(window):
	if window[1][1] == 'A':
		corners_clockwise = ''.join((window[0][0], window[0][2], window[2][2], window[2][0]))
		if corners_clockwise in ['MMSS', 'MSSM', 'SMMS', 'SSMM']:
			return True
	return False


def part2(grid):
	window_size = 3
	count = 0
	for row in range(len(grid) - window_size + 1):
		for column in range(len(grid[0]) - window_size + 1):
			window = [grid[row + window_row][column:column + window_size] for window_row in range(window_size)]
			if is_xmas(window):
				count += 1
	return count


def part1(grid):
	count = 0
	directions = list(product([-1, 0, 1], repeat=2))
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			for dy, dx in directions:
				word = ''
				for i in range(len(target_word)):
					next_y = row + (i * dy)
					next_x = col + (i * dx)
					if not (0 <= next_y < len(grid) and 0 <= next_x < len(grid[0])):
						break
					word += grid[next_y][next_x]
				if word == target_word:
					count += 1
	return count


def main():
	with open('input.txt') as f:
		grid = f.readlines()
	print(part1(grid))
	print(part2(grid))


if __name__ == '__main__':
	main()