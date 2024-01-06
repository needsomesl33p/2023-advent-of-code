from operator import itemgetter


STRENGHT_OF_CARDS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                     '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
POINTS = {2: 1, 3: 3, 4: 5, 5: 6}


def read_inputfile() -> list[tuple]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return [tuple(camal_cards.split()) for camal_cards in inputfile.readlines()]


def get_strength(hand: str, value=0) -> int:
    card1 = hand[0]
    num_of_cards = hand.count(card1)
    value += POINTS[num_of_cards] if num_of_cards in POINTS else 0
    hand = hand.replace(card1, '')
    if len(hand) <= 1:
        return value
    return get_strength(hand, value)


def organize_cards(camal_cards: list) -> dict:
    organised_cards = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for camal_card, value in camal_cards:
        organised_cards[value].append(camal_card)
    return organised_cards


def sort_cards(organized_cards: dict) -> None:
    for _, camal_cards in organized_cards.items():
        camal_cards.sort(key=lambda camal_card:
                         [STRENGHT_OF_CARDS.get(char) for char in camal_card[0]], reverse=True)


def merge_lists(cards: list[list]) -> list:
    merged_list = []
    for _, camal_cards in cards:
        merged_list.extend(camal_cards)
    return merged_list


def calc_grand_total(lst: list) -> int:
    sum_ = 0
    idx = 0
    for rank in range(len(lst), 0, -1):
        sum_ += int(lst[idx][1]) * rank
        idx += 1

    return sum_


def main():
    camal_cards: list = read_inputfile()
    camals_with_value = [(card, get_strength(card[0]))for card in camal_cards]
    organized_cards: dict = organize_cards(camals_with_value)
    sort_cards(organized_cards)
    reversed_cards: list = sorted(
        organized_cards.items(), key=itemgetter(0), reverse=True)
    sum_: int = calc_grand_total(merge_lists(reversed_cards))
    print(sum_)


main()
