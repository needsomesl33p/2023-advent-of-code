def load_input() -> list[str]:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        return input_file.read().split('\n\n')


def transpose_matrix(mirror: list[str]) -> list[str]:
    transposed = []
    for idx in range(len(mirror[0])):
        column = ''
        for row in mirror:
            column += row[idx]
        transposed.append(column)
    return transposed


def find_reflection(mirror: list[str], is_vertical: bool = False) -> int:
    mult = 1 if is_vertical else 100
    for idx, row in enumerate(mirror):
        if idx <= len(mirror)-2:
            if is_neighbour_same(row, mirror[idx+1]) and is_true_twin(mirror, idx):
                return (idx + 1) * mult
    return 0


def is_neighbour_same(row: str, next_row: str) -> bool:
    return row == next_row


def is_true_twin(mirror: list[str], idx: int):
    # Actually all mirrors are odd, therefore real paritiy does not possible.
    real_side = mirror[idx+1:]
    imag_side = mirror[:idx+1]
    imag_side.reverse()
    stop = min(len(real_side), len(imag_side))
    for j in range(stop):
        if real_side[j] != imag_side[j]:
            return False
    return True


def main():
    all_notes = 0
    mirrors = load_input()
    for mirror in mirrors:
        mirror = mirror.splitlines()
        result = find_reflection(mirror)
        if not result:
            result = find_reflection(transpose_matrix(mirror), True)
        all_notes += result
    print(all_notes)


main()
