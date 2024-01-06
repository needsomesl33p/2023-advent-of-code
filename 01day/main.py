from typing import List
from string import digits

CalibrationDoc = List[str]
CalibrationValues = List[int]


def read_input() -> CalibrationDoc:
    with open('input.txt', 'r') as input:
        return input.readlines()


def find_digit(line: str, start: int, step: int = 1, stop_mod: int = 0) -> str:
    line_len: int = len(line)
    stop: int = line_len + \
        stop_mod if stop_mod >= 0 else (line_len * -1) + stop_mod
    for index in range(start, stop, step):
        if line[index] in digits:
            return line[index]


def select_cal_values(calibration_doc: CalibrationDoc) -> CalibrationValues:
    calibration_values: CalibrationValues = []
    for line in calibration_doc:
        digit1: str = find_digit(line, 0)
        digit2: str = find_digit(line, -1, -1, -1)
        calibration_values.append(int(f'{digit1}{digit2}'))
    return calibration_values


def main():
    cal_doc: CalibrationDoc = read_input()
    calibration_values: CalibrationValues = select_cal_values(cal_doc)
    sum_: int = sum(calibration_values)
    print(f'Sum of calculation values: {sum_}')


if __name__ == '__main__':
    main()
