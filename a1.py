# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

import os
from pathlib import Path

## =========================================================== ##
##            CATCH IT FUNCTION                                ##
## =========================================================== ##

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
                subfolder, file = make_sense(path, 'r') # new struct
                print(file)
                if 'f' in c_flags:
                    '''only files'''
                    # output only files recursively
                    print_list(file)
                    return

                if 's' in c_flags:
                    '''specific file name'''
                    # output files that match recursively
                    named_file = search_by_name(file, 'r', choice)
                    print_list(named_file)
                    return      

                if 'e' in c_flags:
                    '''extension'''
                    # output files that match extension recur
                    ext_file = search_by_ext(file, 'r', choice)
                    print_list(ext_file)
                    return

                else:
                    # output everything recursively
                    print_list(subfolder)
                    print_list(file)
            
            elif 'r' not in c_flags:
                fly = make_sense(path, '') #fly is the file but singular
                if 'f' in c_flags:
                    # output only files in given dir
                    print_list(fly)
                    return
                    
                elif 's' in c_flags:
                    # output files that match in given dir
                    named_fly = search_by_name(fly, '', choice)
                    print_list(named_fly)
                    return

                elif 'e' in c_flags:
                    # output files that match extension in dir
                    ext_fly = search_by_ext(fly, '', choice)
                    print_list(ext_fly)
                    return
                    
            else:
                print("try again")

        case "D":
            # Delete
            if 'r' in c_flags:
                # unlink recursively
                unlink_it(path, 'r', choice)
                file = make_sense(path, 'r')
                print("Remaining: ")
                print_list(file)
            
            elif '' == c_flags:
                # unlink not recursively
                unlink_it(path, '', choice)
                fly = make_sense(path, '')
                print("Remaining: ")
                print_list(fly)


        case "R":
            read_it(path, choice)

        case "C":
            create_it(path, choice)
## =========================================================== ##
##            CATCH IT FUNCTION                                ##
## =========================================================== ##


def understand_flags(flags: str) -> str:
    c_flags = ''
    for i in flags:
        if i.isalnum():
            c_flags += flags[i]
    return c_flags


## =========================================================== ##
##            MAKE SENSE FUNCTION                              ##
## =========================================================== ##
def make_sense(path: Path, flag: str) -> list:
    if flag == 'r':
        #-------------------------------------------------------#
        def search_directories_recursively(dir):
            '''
            R: makes a recursive search for files
            '''
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
        #-------------------------------------------------------#
        file = search_directories_recursively(path)
        return file

    elif flag == '':
        #-------------------------------------------------------#
        def search_directory(dir): 
            '''
            D: makes a single sweep in a path for files
            '''
            file = []

            for f in os.scandir(dir):

                if f.is_file():
                    file.append(f.path)

            return file
        #-------------------------------------------------------#
        file = search_directory(path)
        return file
## =========================================================== ##
##            MAKE SENSE FUNCTION                              ##
## =========================================================== ##

def search_by_name(file: list[str], flag: str, name_choice: str):
    named_f = []
    for f in file:
        path = Path(f)
        if path.name == name_choice:
            named_f.append(f)

    return named_f


def search_by_ext(file: list[str], flag: str, ext_choice: str):
    ext_f = []

    ext_choice = ext_choice.lstrip(".")

    for f in file:
        path = Path(f)
        if ext_choice == f.name:
            ext_f.append(f)

    return ext_f

def create_it(path: Path, choice: str):
    if path.isdir():
        create_this = path + choice
        create_this.touch()


def unlink_it(file: list[str], flag: str, choice: str):
    if flag == 'r':
        # recursive unlink
        pass
    else:
        pass

def read_it(path: Path):
    # read the file
    f = path.open('r')
    f_contents = f.readlines()
    print_list(f_contents)
    f.close()

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