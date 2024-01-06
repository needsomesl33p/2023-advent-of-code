from typing import List
Games = List[List[str]]

RED_CUBE: int = 12
GREEN_CUBE: int = 13
BLUE_CUBE: int = 14


def read_inputfile() -> List:
    with open('../input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def convert_dataset(inputfile: List) -> Games:
    games: Games = []
    for line in inputfile:
        temp: List = line.split(':')
        game: List = temp[1][1:].replace(';', ',').split(',')
        games.append(game)
    return games


def sum_biggest_cubes(games: Games) -> int:
    sum_: int = 0
    for pairs in games:
        sum_ += get_power_of_set(pairs)
    return sum_


def get_power_of_set(pairs: List) -> int:
    red, green, blue = 0, 0, 0
    for item in pairs:
        pair = item.strip().split(' ')
        tmp_color: int = int(pair[0])
        if pair[1] == 'red' and tmp_color > red:
            red = tmp_color
        elif pair[1] == 'green' and tmp_color > green:
            green = tmp_color
        elif pair[1] == 'blue' and tmp_color > blue:
            blue = tmp_color
    return red * green * blue


def main():
    input_data: List = read_inputfile()
    games: Games = convert_dataset(input_data)
    sum_ = sum_biggest_cubes(games)
    print(sum_)


if __name__ == '__main__':
    main()
