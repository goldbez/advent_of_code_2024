# https://adventofcode.com/2024/day/6


directions = {
	(-1, 0): (0, 1),	# up to right
	(0, 1): (1, 0),		# right to down
	(1, 0): (0, -1),	# down to left
	(0, -1): (-1, 0),	# left to up
}


def get_starting_position(grid):
	for current_y in range(len(grid)):
		try:
			current_x = grid[current_y].index('^')
			return current_y, current_x
		except ValueError:
			continue


def make_next_move(grid, current_y, current_x, current_direction):
	dy, dx = current_direction
	if current_y + dy >= len(grid) or current_y + dy < 0 or current_x + dx >= len(grid[0]) or current_x + dx < 0:
		return None
	if grid[current_y + dy][current_x + dx] == '#':
		return current_y, current_x, directions[current_direction]
	return current_y + dy, current_x + dx, current_direction


def part1(grid):
	current_y, current_x = get_starting_position(grid)
	current_direction = (-1, 0)
	distinct_positions = {(current_y, current_x)}
	while True:
		data = make_next_move(grid, current_y, current_x, current_direction)
		if data is None:
			break
		current_y, current_x, current_direction = data
		distinct_positions.add((current_y, current_x))
	return len(distinct_positions)


def part2(grid):
	answer = 0
	initial_y, initial_x = get_starting_position(grid)
	initial_direction = (-1, 0)
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '.':
				grid[i][j] = '#'
				current_y, current_x = initial_y, initial_x
				current_direction = initial_direction
				positions_and_directions = {(current_y, current_x, current_direction)}
				while True:
					data = make_next_move(grid, current_y, current_x, current_direction)
					if data is None:
						break
					current_y, current_x, current_direction = data
					if (current_y, current_x, current_direction) in positions_and_directions:
						answer += 1
						break
					positions_and_directions.add((current_y, current_x, current_direction))
				grid[i][j] = '.'
	return answer


def main():
	with open('input.txt') as f:
		raw = f.read().strip()
		grid = [list(i) for i in raw.split('\n')]
	print(part1(grid))
	print(part2(grid))


if __name__ == '__main__':
	main()