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
    path = Path(path)

    flags = catch[2:-1]

    # figure out what the flags are
    c_flags = understand_flags(flags)

    choice = catch[-1]


    match first_command:
        case "L":
            # list
            if 'r' in c_flags:
                if 'f' in c_flags:
                    '''only files'''
                    # output only files recursively
                    pass

                if 's' in c_flags:
                    '''specific file name'''
                    # output files that match recursively
                    pass      

                if 'e' in c_flags:
                    '''extension'''
                    # output files that match extension recur
                    pass

                else:
                    # output everything recursively
                    pass

            elif 'f' in c_flags:
                # output only files in given dir
                pass

            elif 's' in c_flags:
                # output files that match in given dir
                pass

            elif 'e' in c_flags:
                # output files that match extension in dir
                pass
                    
            else:
                # output everything
                pass

        case "D":
            # unlink
            if 'r' in c_flags:
                unlink_it(path, 'r', choice)
                print('deleted that')
            
            else:
                unlink_it(path, '', choice)
                print('deleted that')


        case "R":
            # open and read a file given the exact path
            read_it(path, choice)

        case "C":
            # create
            create_it(path, choice)


def search_by_name(user_choice, file, interesting_file):
    '''
    Searches files in a list by their name recursively
    '''

    for f in file:
        path = Path(f)
        if path.name == user_choice:
            interesting_file.append(f)

    return interesting_file

    
def print_list(print_it: list):
    for i in print_it:
        print(i)


def make_sense(path: Path, c_flags: str, choice: str):
    file = []

    for f in os.scandir(path):

        if f.is_file():
            file.append(f.path)

    return file


def create_it(path: Path, choice: str):
    if path.isdir():
        create_this = path + choice
        create_this.touch()



def unlink_it_recursively(path: Path, choice: str):
    pass

def unlink_it(path: Path, choice: str):
    pass

def read_it(path: Path):
    pass


def main():
    pass_it = 'H'
    while pass_it != 'Q':
        pass_it = input()
        catch_it(pass_it)


if __name__ == "__main__":
    main()