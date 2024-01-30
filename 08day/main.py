def load_input() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as file:
        return file.read().splitlines()


def transform_input(input_file: list[str]) -> dict[str, list]:
    network = {}
    for line in input_file:
        line = line.replace(' ', '')
        data = line.split('=')
        node = data[0].strip()
        elements = data[1][1:-1].split(',')
        network[node] = elements
    return network


def count_steps(instructions: str, network: dict[str, list]) -> int:
    counter, pointer = 0, 0
    node: str = 'AAA'
    while node != 'ZZZ':
        instruction = instructions[pointer]
        elements = network[node]
        print(node, elements, instruction)
        node = elements[0] if instruction == 'L' else elements[1]
        pointer = 0 if len(instructions)-1 == pointer else pointer+1
        counter += 1
    return counter


def main():
    inp: list[str] = load_input()
    instructions = inp[0]
    network = transform_input(inp[2:])
    steps = count_steps(instructions, network)
    print(steps)


main()
