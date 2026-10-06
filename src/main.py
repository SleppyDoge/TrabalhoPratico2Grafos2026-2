# Imports
import sys

# Modified classes/functions


# Data input - sys filepath safety
def get_filepath() -> str:
    if len(sys.argv) != 2:
        raise FileNotFoundError(
            "The execution of the program requires input of the filepath with the input data"
        )
    return sys.argv[1]


# Data input - read
def data_input() -> list[int]:
    filepath = get_filepath()
    raw_data = None
    with open(filepath, "r") as arquivo:
        raw_data = list(map(lambda x: int(x), arquivo.read().split()))
    return raw_data


def data_parsing(raw_data: list[int]) -> dict:
    return {
        "vertices_size": raw_data[0],
        "costs": raw_data[1 : raw_data[0] + 1],
        "edge_size": raw_data[raw_data[0] + 1],
        "edges": list(
            zip(raw_data[raw_data[0] + 2 :: 2], raw_data[raw_data[0] + 2 + 1 :: 2])
        ),
    }


# Processing


# Main
def main():
    raw_data = data_input()
    raw_data = data_parsing(raw_data)
    print(raw_data)


# Run
if __name__ == "__main__":
    main()
