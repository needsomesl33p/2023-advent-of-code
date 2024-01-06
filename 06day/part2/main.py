# Solve it with binary search


def read_inputfile() -> tuple[int, int]:
    with open('../input.txt', 'r', encoding='utf8') as inputfile:
        lines = inputfile.read().splitlines()
        time = int(lines[0].split(':')[1].replace(' ', ''))
        distance = int(lines[1].split(':')[1].replace(' ', ''))
        return time, distance


def calculate_winner_races(time: int, distance: int) -> int:
    total: int = 0
    for milsec in range(0, time):
        current_dist: int = milsec * (time-milsec)
        if current_dist > distance:
            total += 1
    return total


def main():
    times, distances = read_inputfile()
    print(times, distances)
    print(calculate_winner_races(times, distances))


if __name__ == '__main__':
    main()
