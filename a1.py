# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

import os
from pathlib import Path

def catch_it(pass_it: str):
    if pass_it == 'Q':
        return

    catch = pass_it.split()

    first_command = catch[0]

    path = Path(catch[1])

    flags = catch[2:-1]

    c_flags = understand_flags(flags)

    choice = catch[-1]

    match first_command:
        case "L":
            # list
            subfolder, file = make_sense(path, 'r')
            if 'f' in c_flags:
                print_list(file)
                return
            elif 's' in c_flags:
                named_file = search_by_name(file, choice)
                print_list(named_file)
                return
            elif 'e' in c_flags:
                ext_file = search_by_ext(file, choice)
                print_list(ext_file)
                return
            else:
                print_list(subfolder + file)

        case "D":
            # Delete
            if 'r' in c_flags:
                unlink_it(path, 'r', choice)
            else:
                unlink_it(path, '', choice)

        case "R":
            read_it(path, choice)

        case "C":
            create_it(path, choice)

def understand_flags(flags: list) -> str:
    c_flags = ''.join(flag for flag in flags if flag.isalnum())
    return c_flags

def make_sense(path: Path, flag: str) -> list:
    if flag == 'r':
        def search_directories_recursively(dir):
            subfolder, file = [], []
            for f in os.scandir(dir):
                if f.is_dir():
                    subfolder.append(f.path)
                if f.is_file():
                    file.append(f.path)
            for d in list(subfolder):
                sf, f = search_directories_recursively(d)
                subfolder.extend(sf)
                file.extend(f)
            return subfolder, file
        return search_directories_recursively(path)
    elif flag == '':
        def search_directory(dir):
            file = [f.path for f in os.scandir(dir) if f.is_file()]
            return file
        return search_directory(path)

def search_by_name(file: list, name_choice: str):
    return [f for f in file if f.name == name_choice]

def search_by_ext(file: list, ext_choice: str):
    ext_choice = ext_choice.lstrip(".")
    return [f for f in file if ext_choice == f.name]

def create_it(path: Path, choice: str):
    if path.is_dir():
        create_this = path / choice
        create_this.touch()

def unlink_it(path: Path, flag: str, choice: str):
    if flag == 'r':
        # Recursive unlink logic goes here
        pass
    else:
        file_to_unlink = path / choice
        file_to_unlink.unlink()

def read_it(path: Path):
    with path.open('r') as f:
        f_contents = f.readlines()
        print_list(f_contents)

def print_list(print_it: list):
    for i in print_it:
        print(i)

def main():
    pass_it = 'H'
    while pass_it != 'Q':
        pass_it = input()
        catch_it(pass_it)

if __name__ == "__main__":
    main()
