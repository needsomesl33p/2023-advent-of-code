from functools import reduce


def read_inputfile() -> tuple[list, list]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        lines = inputfile.readlines()
        time: list[str] = lines[0].split(':')[1].split()
        distance: list[str] = lines[1].split(':')[1].split()
        return [int(i) for i in time], [int(i) for i in distance]


def calculate_winner_races(times: list, distances: list) -> int:
    winning_cases: list[int] = []
    for idx, time in enumerate(times):
        total: int = 0
        dist: int = distances[idx]
        for milsec in range(0, time):
            current_dist: int = milsec * (time-milsec)
            if current_dist > dist:
                total += 1
        winning_cases.append(total)
    print(winning_cases)
    return reduce(lambda x, y: x*y, winning_cases)


def main():
    times, distances = read_inputfile()
    print(calculate_winner_races(times, distances))


if __name__ == '__main__':
    main()
