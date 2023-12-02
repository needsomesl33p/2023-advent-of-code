from typing import List
Games = List[List[str]]
RED_CUBE: int = 12
GREEN_CUBE: int = 13
BLUE_CUBE: int = 14


def read_inputfile() -> List:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def convert_dataset(inputfile: List) -> Games:
    games: Games = []
    for line in inputfile:
        temp: List = line.strip().split(':')
        game: List = temp[1][1:].replace(';', ',').split(',')
        games.append(game)
    return games


def count_possible_cases(games: Games) -> int:
    sum_: int = 0
    for game_id, game, in enumerate(games, 1):
        if is_possible(game):
            sum_ += game_id

    return sum_


def is_possible(game: List[str]) -> bool:
    red, green, blue = get_cubes(game)
    return red <= RED_CUBE and green <= GREEN_CUBE and blue <= BLUE_CUBE


def get_cubes(game: List[str]) -> tuple[int, int, int]:
    red, green, blue = 0, 0, 0
    for pair in game:
        pair = pair.strip().split(' ')
        tmp_color: int = int(pair[0])
        if pair[1] == 'red' and tmp_color > red:
            red = tmp_color
        elif pair[1] == 'green' and tmp_color > green:
            green = tmp_color
        elif pair[1] == 'blue' and tmp_color > blue:
            blue = tmp_color
    return red, green, blue


def main():
    input_data: List = read_inputfile()
    games: Games = convert_dataset(input_data)
    sum_ = count_possible_cases(games)
    print(sum_)


if __name__ == '__main__':
    main()
