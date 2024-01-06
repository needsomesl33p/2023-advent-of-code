from string import ascii_lowercase


def read_inputfile() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.read().splitlines()


def convert_input(input_file: list[str]) -> tuple[list, dict]:
    garden_maps: dict[str, list] = {}
    mapping_name: str = ''
    removed_empty_lines: list[str] = [row for row in input_file if row]
    seeds: list[int] = string_to_int(
        input_file[0].split(':')[1].split())
    for line in removed_empty_lines[1:]:
        if line[0] in ascii_lowercase:
            mapping_name = line[:-1]
            garden_maps[mapping_name] = []
        else:
            garden_maps[mapping_name].append(string_to_int(line.split()))
    return seeds, garden_maps


def string_to_int(list_of_strings: list[str]) -> list[int]:
    return [int(string) for string in list_of_strings]


def get_locations(garden_maps: dict[str, list], seeds: list[int]):
    m_name, mappings = next(iter(garden_maps.items()))
    del garden_maps[m_name]
    print(m_name)
    new_seeds = get_new_seeds(mappings, seeds)
    print(new_seeds)
    if len(garden_maps) == 0:
        print('exit recursion...')
        return new_seeds
    return get_locations(garden_maps, new_seeds)


def get_new_seeds(mappings: list[list[int]], seeds: list[int]) -> list[int]:
    new_seeds: list[int] = []
    for seed in seeds:
        new_seeds.append(calculate_seed(seed, mappings))
    return new_seeds


def calculate_seed(seed: int, mappings: list[list[int]]):
    new_seed = seed
    for map_ in mappings:
        destination = map_[0]
        source = map_[1]
        map_range = map_[2]
        if source <= seed < (source + map_range):
            if destination > source:
                return seed + (destination - source)
            return seed - (source - destination)
    return new_seed


def main():
    input_file = read_inputfile()
    seeds, garden_maps = convert_input(input_file)
    locations = get_locations(garden_maps, seeds)
    print(min(locations))


if __name__ == '__main__':
    main()
