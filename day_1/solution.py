# https://adventofcode.com/2024/day/1

def part1(col1, col2):
	answer = 0
	for i in range(len(col1)):
		answer += abs(col1[i] - col2[i])
	print(answer)


def part2(col1, col2):
	answer = 0
	for i in col1:
		answer += i * col2.count(i)
	print(answer)


def main():
	with open("input.txt") as f:
		raw = f.read()
	nums = raw.split()
	col1 = sorted([int(nums[i]) for i in range(len(nums)) if not i % 2])
	col2 = sorted([int(nums[i]) for i in range(len(nums)) if i % 2])
	part1(col1, col2)
	part2(col1, col2)


if __name__ == "__main__":
	main()
