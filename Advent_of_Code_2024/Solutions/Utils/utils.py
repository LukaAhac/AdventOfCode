from pathlib import Path
import os

def readThisPuzzlesInput(file):
    current_file_path = Path(file)
    current_file_directory = current_file_path.parent
    parent_directory = current_file_directory.parent

    current_file_name = os.path.basename(file)
    input_file_name = current_file_name[:-3] + ".txt"

    file_path = parent_directory / "Inputs" / input_file_name

    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line.rstrip("\n") for line in lines]

    return lines
