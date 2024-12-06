# https://adventofcode.com/2024/day/5


def get_anteriors(orders):
	anteriors = dict()
	for before, after in orders:
		if after in anteriors:
			anteriors[after].add(before)
		else:
			anteriors[after] = {before}
	return anteriors


def get_middle_if_in_order(update, anteriors):
	for i in range(len(update)):
		if update[i] in anteriors:
			numbers_after = set(update[i:])
			for anterior in anteriors[update[i]]:
				if anterior in numbers_after:
					return 0
	return update[len(update)//2]


def reorder_update(update, anteriors):
	keep_going = True
	while keep_going:
		keep_going = False
		for i in range(len(update)):
			if update[i] in anteriors:
				for j in range(len(update)-1, i, -1):
					if update[j] in anteriors[update[i]]:
						to_insert = update.pop(i)
						update.insert(j, to_insert)
						keep_going = True
						break
	return update


def part1(anteriors, updates):
	return sum(get_middle_if_in_order(update, anteriors) for update in updates)


def part2(anteriors, updates):
	incorrect_updates = [update for update in updates if get_middle_if_in_order(update, anteriors) == 0]
	reordered_updates = [reorder_update(update, anteriors) for update in incorrect_updates]
	return sum(update[len(update)//2] for update in reordered_updates)


def main():
	with open('input.txt') as f:
		raw = f.read()
	raw_orders, raw_updates = raw.strip().split('\n\n')
	orders = [[int(j) for j in i.split('|')] for i in raw_orders.split('\n')]
	updates = [[int(j) for j in i.split(',')] for i in raw_updates.split('\n')]
	anteriors = get_anteriors(orders)
	print(part1(anteriors, updates))
	print(part2(anteriors, updates))


if __name__ == '__main__':
	main()