def read_inputfile() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def separate_scratchcards(card: str) -> tuple[str, str]:
    card = card.split(':')[1:][0]
    card = card.strip().replace('  ', ' ')
    print(card, end=' - ')
    winning_num, num_pool = card.split('|')
    return winning_num.split(), num_pool.split()


def get_scores(winning_nums: list[str], num_pool: list[str]) -> int:
    doubles = 0
    for winner in winning_nums:
        if winner in num_pool:
            doubles += 1
    print(doubles)
    if doubles == 0:
        return 0
    if doubles == 1:
        return 1
    return pow(2, doubles-1)


def count_scores(scartchcards: list[str]) -> list[int]:
    sum_: list[int] = []
    for card in scartchcards:
        winning_nums, num_pool = separate_scratchcards(card)
        sum_.append(get_scores(winning_nums, num_pool))
    return sum_


def main():
    scratchcards: list[str] = read_inputfile()
    sum_: list = count_scores(scratchcards)
    print(sum(sum_))


if __name__ == '__main__':
    main()
