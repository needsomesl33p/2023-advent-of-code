def load_input() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as file:
        return file.read().splitlines()


def expand_universe(galaxies: list[str]) -> None:
    ctr = 0
    empty_space = '.' * len(galaxies[0])
    empty_row_idxs: list[int] = []
    for idx, row in enumerate(galaxies):
        if '#' not in row:
            empty_row_idxs.append(idx+ctr)
            ctr += 1

    for idx in empty_row_idxs:
        galaxies.insert(idx, empty_space)


def flip_matrix(galaxies: list[str]) -> list[str]:
    columns: dict[int, str] = {
        column_idx: '' for column_idx in range(len(galaxies[0]))}

    for row in galaxies:
        for idx, char in enumerate(row):
            columns[idx] = columns[idx] + char

    return list(columns.values())


def locate_galaxies(galaxies: list[str]) -> list[tuple[int, int]]:
    coordinates = []
    for idx, row in enumerate(galaxies):
        for idy, char in enumerate(row):
            if char == '#':
                coordinates.append((idx, idy))

    return coordinates


def calc_shortest_path(coordinates: list) -> int:
    counter = 0
    while len(coordinates) != 0:
        galaxy = coordinates.pop(0)
        for x, y in coordinates:
            counter += abs(x-galaxy[0]) + abs(y-galaxy[1])
    return counter


def print_universe(galaxies: list[str]) -> None:
    for idx, galaxy in enumerate(galaxies):
        print(idx, galaxy)


def main():
    galaxies = load_input()
    expand_universe(galaxies)
    flipped = flip_matrix(galaxies)
    expand_universe(flipped)
    galaxies = flip_matrix(flipped)
    coordinates = locate_galaxies(galaxies)
    print_universe(galaxies)
    print(calc_shortest_path(coordinates))


main()
