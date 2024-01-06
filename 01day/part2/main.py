from typing import List
from string import digits

CalibrationDoc = List[str]
CalibrationValues = List[int]

TRANSLATION_TABLE: dict[str, str] = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def read_inputfile() -> CalibrationDoc:
    with open('../input.txt', 'r') as inputfile:
        return inputfile.readlines()


def find_digit(line: str, start: int, step: int = 1, stop_mod: int = 0) -> str:
    line_len: int = len(line)
    stop: int = line_len + \
        stop_mod if stop_mod >= 0 else (line_len * -1) + stop_mod
    for index in range(start, stop, step):
        if line[index] in digits:
            return line[index]


def find_words(line: str) -> tuple:
    words: list[tuple] = get_words_from_line(line)
    if len(words) == 1:
        return words[0][1], words[0][1]
    if len(words) > 1:
        sorted_list = sorted(words, key=lambda tuple_: tuple_[0])
        return sorted_list[0][1], sorted_list[-1][1]
    return None, None


def get_words_from_line(line: str) -> list[tuple]:
    table: set = set()
    for word in TRANSLATION_TABLE.keys():
        if word in line:
            table.add((line.find(word), word))
            table.add((line.rfind(word), word))

    return list(table)


def is_string_contains_digit(string: str) -> bool:
    return any(letter.isdigit() for letter in string)


def select_cal_values(calibration_doc: CalibrationDoc) -> CalibrationValues:
    calibration_values: CalibrationValues = []
    for line in calibration_doc:
        word1, word2 = find_words(line)
        if word1:
            part1: str = line.split(word1)[0]
            part2: str = line.split(word2)[-1]

            digit1: str = find_digit(line, 0) if is_string_contains_digit(
                part1) else TRANSLATION_TABLE[word1]
            digit2: str = find_digit(line, -1, -1, -1) if is_string_contains_digit(
                part2) else TRANSLATION_TABLE[word2]
        else:
            digit1: str = find_digit(line, 0)
            digit2: str = find_digit(line, -1, -1, -1)

        calibration_values.append(int(f'{digit1}{digit2}'))
    return calibration_values


def main():
    cal_doc: CalibrationDoc = read_inputfile()
    calibration_values: CalibrationValues = select_cal_values(cal_doc)
    sum_: int = sum(calibration_values)
    print(f'Sum of calculation values: {sum_}')


if __name__ == '__main__':
    main()
