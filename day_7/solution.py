# https://adventofcode.com/2024/day/7


def is_possible_equation(answer, operands, part):
	if answer != int(answer):
		return False
	answer = int(answer)
	current_operand = operands[-1]
	remaining_operands = operands[:-1]
	if len(remaining_operands) == 1:
		return (remaining_operands[0] * current_operand == answer
			or remaining_operands[0] + current_operand == answer
			or part == 2 and int(f'{remaining_operands[0]}{current_operand}') == answer)
	return (is_possible_equation(answer / current_operand, remaining_operands, part)
			or is_possible_equation(answer - current_operand, remaining_operands, part)
			or part == 2
				and answer != current_operand
				and str(answer).endswith(str(current_operand))
				and is_possible_equation(int(str(answer)[:-len(str(current_operand))]), remaining_operands, part))


def solve(equations, part):
	return sum(answer for answer, operands in equations if is_possible_equation(answer, operands, part))


def main():
	with open('input.txt') as f:
		lines = f.readlines()
	equations = []
	for line in lines:
		answer, operands = line.split(':')
		equations.append((int(answer), [int(operand) for operand in operands.strip().split()]))

	print(solve(equations, 1))
	print(solve(equations, 2))


if __name__ == '__main__':
	main()