# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

import os
from pathlib import Path


class InputError:
    pass

def catch_it(pass_it: str):
    catch = pass_it.split()
    first_command = catch[0]
    path = catch[1]
    flags = catch[2:-1]
    choice = catch[-1]  
    
    match first_command:
        case "L":
            try:
                pathy = get_path()
                stringy = understand_flags(flags)
                triceratop = [choice]

                triceratops = triceratops(pathy, stringy, triceratop)

                for i in triceratops:
                    print(i)

            finally:
                pass

        case "D":
            pass

        case "Q":
            return
        case "R":
            pass
        case "C":
            pass
     
    def get_path():
        luna = Path(path)
        if luna.is_dir():
            return luna
        raise FileNotFoundError
    
    def understand_flags():
        pass

def triceratops(pathy: Path, stringy: str, search_str: str) -> list:

    if "r" in stringy:
        if "f" in stringy:
            def search_by_name(user_choice, file):
                '''
                Searches files in a list by their name recursively
                '''

                named_file = []

                for f in file:
                    path = Path(f)
                    if path.name == user_choice:
                        named_file.append(f)

                return file
            file = search_by_name(pathy, search_str)

        if "stringy:
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
    
    elif "s" in stringy:
        file = []

        for f in os.scandir(dir):

            if f.is_file():
                file.append(f.path)

        return file
    
    elif "e" in stringy:
        
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
        
        file = search_by_extension(pathy, pathy)

        return file
        





def main():
    while pass_it != 'Q':
        try:
            pass_it = input()
            catch_it(pass_it)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            pass


if __name__ == "__main__":
    main()