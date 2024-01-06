# This script cosumes all the memory. Kernel will SIGKILL it.

from string import ascii_lowercase


def read_inputfile() -> list[str]:
    with open('input.txt', 'r', encoding='utf8') as inputfile:
        return inputfile.readlines()


def convert_input(input_file: list[str]):
    garden_maps: dict[str, list] = {}
    mapping_name: str = ''
    removed_newlines: list[str] = [string.strip() for string in input_file]
    removed_empty_lines: list[str] = [row for row in removed_newlines if row]
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
    print('generate lookup tables')
    source_m, destination_m = generate_lookup_tables(mappings)
    for seed in seeds:
        if seed not in source_m:
            new_seeds.append(seed)
        else:
            idx: int = source_m.index(seed)
            new_seed: int = destination_m[idx]
            new_seeds.append(new_seed)
    return new_seeds


def generate_lookup_tables(mappings: list[list[int]]):
    source_table, destionation_table = [], []
    for mapping in mappings:
        destination = mapping[0]
        source = mapping[1]
        map_range = mapping[2]
        source_subpart: list = [
            num for num in range(source, source + map_range)]
        dest_subpart: list = [num for num in range(
            destination, destination + map_range)]
        source_table.extend(source_subpart)
        destionation_table.extend(dest_subpart)
    return source_table, destionation_table


def main():
    input_file = read_inputfile()
    seeds, garden_maps = convert_input(input_file)
    locations = get_locations(garden_maps, seeds)
    print(min(locations))


if __name__ == '__main__':
    main()
