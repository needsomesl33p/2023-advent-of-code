"""
The input file shows that 1 symbol can argo multiple numbers,
but 1 number can be adjacent to only 1 symbol.

Biggest number: 3 digits

Note: Should not use typing: list, Tuple etc. 
3.9 supports type aliasing by default
"""

import re
from string import digits
EngineSchematic = list[str]
GearLocationMatrix = list(tuple[int, int])
NON_GEARS: str = digits + '.'
MAX_DEC: int = 4


def read_inputfile() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def search_gears(engine_schematic: EngineSchematic) -> GearLocationMatrix:
    gear_matrix: list[tuple] = []
    for index, row in enumerate(engine_schematic):
        row = row.strip()
        for j, symbol in enumerate(row):
            if symbol not in NON_GEARS:
                gear_matrix.append((index, j))

    return gear_matrix


def collect_nearby_parts(matrix: GearLocationMatrix, engine_schematic: EngineSchematic) -> int:
    v_num = 0
    sum_ = 0
    for i, j in matrix:
        row: str = engine_schematic[i].strip()
        up_row: str = engine_schematic[i-1].strip()
        low_row: str = engine_schematic[i+1].strip()
        v_num: int = search_horizontally(row, j)
        h_num = search_vertically(j, up_row, low_row)
        sum_ += (v_num + h_num)
    return sum_


def search_horizontally(row: str, index: int) -> int:
    left_adj_num, right_adj_num = 0, 0
    length: int = len(row) - 1
    if index - 1 >= 0 and row[index-1] in digits:
        left_adj_num: int = walkthrough(row, index, 'left')
    if index <= length and row[index+1] in digits:
        right_adj_num: int = walkthrough(row, index, 'right')
    return left_adj_num + right_adj_num


def search_vertically(index: int, up_row: str, low_row='') -> tuple[int, int]:
    upper, lower, diag_u, diag_l = 0, 0, 0, 0
    up_center: str = up_row[index-1:index+2]
    low_center: str = low_row[index-1:index+2]
    is_up_vertical: bool = up_row[index] != '.'
    is_low_vertical: bool = low_row[index] != '.'
    is_up_diag: bool = any(
        symbol in digits for symbol in up_center) and not is_up_vertical
    is_low_diag: bool = any(
        symbol in digits for symbol in low_center) and not is_low_vertical
    if up_row and is_up_vertical:
        upper = continue_vertical_search(up_row, index)
    if low_row and is_low_vertical:
        lower = continue_vertical_search(low_row, index)
    if is_up_diag:
        diag_u = search_diagonally(up_row, index)
    if is_low_diag:
        diag_l = search_diagonally(low_row, index)
    return upper + lower + diag_u + diag_l


def continue_vertical_search(row: str, index: int) -> int:
    center: str = row[index-1:index+2]
    is_all_num = all(item in digits for item in list(center))
    if is_all_num:
        return int(center)
    direction: str = determine_direction(row, index)
    num: int = walkthrough(row, index, direction)
    return num


def search_diagonally(row: str, index: int) -> int:
    result: int = 0
    direction: str = determine_diag_direction(row, index)
    if direction == 'both':
        result += walkthrough(row, index, 'left')
        result += walkthrough(row, index, 'right')
    else:
        result = walkthrough(row, index, direction)
    return result


def determine_direction(row: str, index: int) -> str:
    return 'left' if row[index+1] == '.' else 'right'


def determine_diag_direction(row: str, index: int):
    if row[index+1] != '.' and row[index-1] != '.':
        return 'both'
    return determine_direction(row, index)


def walkthrough(row: str, index: int, direction: str) -> int:
    numb: str = ''
    step: int = -1 if direction == 'left' else 1
    stop: int = index - MAX_DEC if direction == 'left' else index + MAX_DEC
    for idx in range(index, stop, step):
        numb += row[idx]
    numb = numb.split('.')
    numb = list(filter(None, numb))
    numb = (re.search('\d+', numb[0]).group())
    return int(numb[::-1]) if direction == 'left' else int(numb)


def main():
    engine_schematic: EngineSchematic = read_inputfile()
    gear_matrix: GearLocationMatrix = search_gears(engine_schematic)
    sum_: int = collect_nearby_parts(gear_matrix, engine_schematic)
    print(sum_)


if __name__ == '__main__':
    main()
