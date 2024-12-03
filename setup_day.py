import os


def main():
    directories = [f for f in os.listdir(".") if os.path.isdir(os.path.join(".", f)) and f.startswith("day_")]
    next_day = max([int(i.split("_")[1]) for i in directories]) + 1 if len(directories) else 1
    os.mkdir(os.path.join(".", f"day_{next_day}"))
    for filename in ["solution.py", "example.txt", "input.txt"]:
        with open(os.path.join(".", f"day_{next_day}", filename), "w") as f:
            if filename == "solution.py":
                f.write(f"# https://adventofcode.com/2024/day/{next_day}\n\ndef main():\n\tpass\n\nif __name__ == \"__main__\":\n\tmain()")


if __name__ == "__main__":
    main()