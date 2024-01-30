# The next pipe can be determined by the current pipe tile and the direction
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

# 11,32

# X, Y coordinates
# CURRENT_DIRECTION = { current_pipe: ((next_x, next_y), next_direction) }

PIPE_MODES = {
    'NORTH': {'|': ((0, -1), 'NORTH'),
              '7': ((-1, 0), 'WEST'),
              'F': ((1, 0), 'EAST')},

    'SOUTH': {'|': ((0, 1), 'SOUTH'),
              'L': ((1, 0), 'EAST'),
              'J': ((-1, 0), 'WEST')},

    'WEST': {'-': ((-1, 0), 'WEST'),
             'L': ((0, -1), 'NORTH'),
             'F': ((0, 1), 'SOUTH')},

    'EAST': {'-': ((1, 0), 'EAST'),
             'J': ((0, -1), 'NORTH'),
             '7': ((0, 1), 'SOUTH')},
}


def load_input() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as file:
        return file.read().splitlines()


def get_start_position(pipline_map: list[str]) -> tuple[int, int]:
    for idy, line in enumerate(pipline_map):
        for idx, letter in enumerate(line):
            if letter == 'S':
                return idx, idy
    return (0, 0)


def walk_thru_pipes(coordinates: tuple[int, int], pipeline_map: list[str]):
    corner = 'SOUTH'
    current_pipe, counter = '|', 0
    while current_pipe != 'S':
        next_dataset = PIPE_MODES[corner][current_pipe]
        coordinates = get_next_coordinates(coordinates, next_dataset[0])
        x, y = coordinates
        current_pipe = pipeline_map[y][x]
        corner = next_dataset[1]
        print(next_dataset, end=' ')
        print(x, y, current_pipe, corner)
        counter += 1
    return counter


def get_next_coordinates(current_coordinates: tuple[int, int], modification: tuple[int, int]) -> tuple[int, int]:
    return current_coordinates[0] + modification[0], current_coordinates[1] + modification[1]


def main():
    pipeline_map = load_input()
    start_coordinates = get_start_position(pipeline_map)
    steps = walk_thru_pipes(start_coordinates, pipeline_map)
    print(steps//2)


main()
