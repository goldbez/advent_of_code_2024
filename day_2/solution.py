# https://adventofcode.com/2024/day/2

def is_safe(report):
    if len(report) <= 1:
        return True
    first_diff = report[1] - report[0]
    if first_diff == 0:
        return False
    direction = first_diff / abs(first_diff)
    last_level = None
    for level in report:
        if last_level is not None and level == last_level:
            return False
        if last_level is not None and abs(level - last_level) > 3:
            return False
        if last_level is not None and (level - last_level) / abs(level - last_level) != direction:
            return False
        last_level = level
    return True


def is_safe_2(report):
    if len(report) <= 2:
        return is_safe(report)
    versions_with_one_element_removed = [report[:i] + report[i + 1:] for i in range(len(report))]
    return any(is_safe(report) for report in versions_with_one_element_removed)


def part1(reports):
    return len([report for report in reports if is_safe(report)])


def part2(reports):
    return len([report for report in reports if is_safe_2(report)])


def main():
    with open("input.txt") as f:
        raw = f.read()
    reports = [[int(i) for i in line.split()] for line in raw.splitlines()]
    print(part1(reports))
    print(part2(reports))


if __name__ == "__main__":
    main()