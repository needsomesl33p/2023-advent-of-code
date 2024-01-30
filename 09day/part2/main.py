def load_input() -> list[list[int]]:
    history: list[list] = []
    with open('../input.txt', 'r', encoding='utf8') as file:
        tmp: list[str] = file.read().splitlines()
        for line in tmp:
            nums = line.split()
            int_generator = (int(num) for num in nums)
            history.append(list(int_generator))
        return history


def get_oasis(history_map: list[list[int]]) -> int:
    counter = 0
    for history in history_map:
        pyramid = get_seq_pyramid(history)
        counter += extrapolate_backwards(pyramid)

    return counter


def get_seq_pyramid(history: list[int]) -> list[list[int]]:
    pyramid = []
    pyramid.append(history)
    init_value = calc_next_sequence(history)
    while sum(init_value) != 0:
        pyramid.append(init_value)
        init_value = calc_next_sequence(init_value)

    pyramid.append(init_value)
    return pyramid


def calc_next_sequence(init_sequence: list[int]) -> list[int]:
    return [init_sequence[idx+1] - init_sequence[idx] for idx in range(len(init_sequence)-1)]


def extrapolate_backwards(pyramid: list[list[int]]) -> int:
    pyramid.reverse()
    final_history_value = pyramid[1][0] - pyramid[0][1]
    for idx in range(1, len(pyramid)-1):
        final_history_value = pyramid[idx+1][0] - final_history_value
    return final_history_value


def main():
    history_map = load_input()
    result = get_oasis(history_map)
    print(result)


main()
