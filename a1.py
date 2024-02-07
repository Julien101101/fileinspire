# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

import os
from pathlib import Path


def understand_flags(flags: str) -> str:
    c_flags = ''
    print(flags)
    for i in flags:
        if i.isalnum():
            c_flags += i
    return c_flags


def catch_it(pass_it: str):
    if pass_it == 'Q':
        return
    catch = pass_it.split()
    first_command = catch[0]
    path = catch[1]
    flags = catch[2:-1]
    choice = catch[-1] 
    
    path = Path(path)
    print(path)
    c_flags = understand_flags(flags)
    print(c_flags)
    

    match first_command:
        case "L":
            try:
                columbus = make_sense(path, c_flags, choice)
                print(columbus)
                for i in columbus:
                    print(i)

            finally:
                pass

        case "D":
            # unlink
            pass

        case "R":
            # read
            pass

        case "C":
            # create
            pass


def make_sense(path: Path, c_flags: str, search_str: str) -> list:
    print(f"inside {c_flags}")
    if c_flags != '':
        print("here")
        if "r" in c_flags:
            if "f" in c_flags:
                def search_by_name_recursively(user_choice, file):

                    named_file = []

                    for f in file:
                        path = Path(f)
                        if path.name == user_choice:
                            named_file.append(f)

                    return file
                file = search_by_name_recursively(path, search_str)

            if "e" in c_flags:
                #recursively look for extensions
                pass


            def search_directories_recursively(dir):
                subfolder, file = [], []

                for f in os.scandir(dir):
                    if f.is_dir():
                        subfolder.append(f.path)
                    if f.is_file():
                        file.append(f.path)

                for dir in list(subfolder):
                    sf, f = search_directories_recursively(dir)
                    subfolder.extend(sf)
                    file.extend(f)

                return subfolder, file
            return file

        elif "f" in c_flags:
            file = []
            for f in os.scandir(dir):

                if f.is_file():
                    file.append(f.path)
            return file

        elif "e" in c_flags:
            def search_by_extension(user_choice, file):
                '''
                Searches files in a directory by their extension
                '''
                extension_file = []

                user_choice = user_choice.lstrip(".")

                for f in file:
                    if user_choice == f.name:
                        extension_file.append(f)

                return extension_file
            
            file = search_by_extension(search_str, path)

            return file
    else:
        file = []

        for f in os.scandir(path):

            if f.is_file():
                file.append(f.path)

        return file



def main():
    pass_it = 'H'
    while pass_it != 'Q':
        pass_it = input()
        catch_it(pass_it)


if __name__ == "__main__":
    main()


    # so if i am seeing this right I can create 
    # functions to create functions in order
    # make this more succint, and more resuable.