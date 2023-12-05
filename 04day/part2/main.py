def read_inputfile() -> list[str]:
    with open('../input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def separate_scratchcards(card: str) -> tuple[str, str]:
    card = card.split(':')[1:][0]
    card = card.strip().replace('  ', ' ')
    winning_num, num_pool = card.split('|')
    return winning_num.split(), num_pool.split()


def get_scores(winning_nums: list[str], num_pool: list[str]) -> int:
    win_num: int = 0
    for winner in winning_nums:
        if winner in num_pool:
            win_num += 1
    return win_num


def count_scores(scartchcards: list[str]) -> dict:
    table: dict = gen_copy_table(len(scartchcards))
    for card_no, card in enumerate(scartchcards, 1):
        winning_nums, num_pool = separate_scratchcards(card)
        win_num = get_scores(winning_nums, num_pool)
        copies: list = [idx for idx in range(card_no+1, card_no+win_num+1)]
        for copy in copies:
            table[str(copy)] = table[str(copy)] + table[str(card_no)]
    return table


def gen_copy_table(length) -> dict:
    table: dict = {}
    for idx in range(1, length+1):
        table[f'{idx}'] = 1
    return table


def main():
    scratchcards: list[str] = read_inputfile()
    table: dict = count_scores(scratchcards)
    print(sum(table.values()))


if __name__ == '__main__':
    main()
