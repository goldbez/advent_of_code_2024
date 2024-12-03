# https://adventofcode.com/2024/day/3

starting_string = "mul("
do = "do()"
dont = "don't()"


def calculate_window(raw, window_start):
	window_end = window_start + len(starting_string)
	window = raw[window_start:window_end]
	if window == starting_string and ")" in raw[window_end:]:
		ending_parentheses = raw[window_end:].index(")") + window_end
		inside_parentheses = raw[window_end:ending_parentheses]
		if (all(character.isdigit() or character == "," for character in inside_parentheses)
				and inside_parentheses.count(",") == 1
				and not (inside_parentheses.startswith(",") or inside_parentheses.endswith(","))):
			num1, num2 = (int(num) for num in inside_parentheses.split(","))
			return num1 * num2
	return 0


def part1(raw):
	return sum(calculate_window(raw, window_start) for window_start in range(len(raw)))


def part2(raw):
	enabled = True
	answer = 0
	for window_start in range(len(raw)):
		if raw[window_start:window_start+len(do)] == do:
			enabled = True
		elif raw[window_start:window_start+len(dont)] == dont:
			enabled = False
		elif enabled:
			answer += calculate_window(raw, window_start)
	return answer


def main():
	with open("input.txt") as f:
		raw = f.read()
	print(part1(raw))
	print(part2(raw))


if __name__ == "__main__":
	main()