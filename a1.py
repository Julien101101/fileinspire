# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

from sys import exit
from pathlib import Path


def catch_it(pass_it: str):
    catch = pass_it.split()
    first_command = catch[0]
    path = catch[1]
    options = catch[2:-1]
    search = catch[-1]

    print(options)

def quit_():
    exit(0)


def main():
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