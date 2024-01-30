def load_input() -> list[str]:
    with open('11day/input.txt', 'r', encoding='utf8') as file:
        return file.read().splitlines()


def expand_universe(galaxies: list[str], dead_rows: list[int], dead_columns: list[int]):
    space_expansion = 1_000_000-1
    coordinates: list[tuple[int, int]] = locate_galaxies(galaxies)
    max_size = normalize_dead_spaces(
        dead_rows, dead_columns, len(galaxies[0]), len(galaxies))
    new_coordinates = coordinates.copy()
    for deads_idx in range(max_size):
        for co_idx, coor in enumerate(coordinates):
            x, y = coor
            a, b = new_coordinates[co_idx]
            if dead_rows[deads_idx] < x and dead_columns[deads_idx] < y:
                new_coordinates[co_idx] = a+space_expansion, b+space_expansion
            elif dead_rows[deads_idx] < x:
                new_coordinates[co_idx] = a+space_expansion, b
            elif dead_columns[deads_idx] < y:
                new_coordinates[co_idx] = a, b+space_expansion

    return new_coordinates


def normalize_dead_spaces(dead_rows: list[int], dead_columns: list[int], max_r: int, max_c) -> int:
    num_r, num_c = len(dead_rows), len(dead_columns)
    if num_r > num_c:
        for _ in range(num_r-num_c):
            dead_columns.append(max_c)
        return num_r
    if num_r < num_c:
        for _ in range(num_c-num_r):
            dead_rows.append(max_r)
        return num_c
    return num_r


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


def collect_dead_spaces(galaxies: list[str]) -> list[int]:
    dead_spaces = []
    for idx, row in enumerate(galaxies):
        if '#' not in row:
            dead_spaces.append(idx)
    return dead_spaces


def main():
    galaxies = load_input()
    dead_rows = collect_dead_spaces(galaxies)
    rev = flip_matrix(galaxies)
    dead_columns = collect_dead_spaces(rev)
    new_coo = expand_universe(galaxies, dead_rows, dead_columns)
    print(calc_shortest_path(new_coo))


main()
