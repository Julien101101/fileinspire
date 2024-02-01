# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

from pathlib import Path


class InputError:
    pass

def catch_it(pass_it: str):
    if first_command == None or path == None \
        or flags == None or choice == None:
        raise InputError
    else:
        catch = pass_it.split()
        first_command = catch[0]
        path = catch[1]
        flags = catch[2:-1]
        choice = catch[-1]    


    match first_command:
        case "L":
            # list
            try:
                path = Path(path)
                for
                pass
            finally:
                pass
            
        case "D":
            # delete
            pass
        case "R":
            # read
            pass
        case _:
            # action-default
            return



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