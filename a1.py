# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

from sys import exit
from pathlib import Path


def catch_it(pass_it: str):
    first_command = pass_it[0]
    path = pass_it[1]
    pass


def quit_():
    exit(0)


def main():
    try:
        pass_it = input("Enter command: ")
        catch_it(pass_it)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass


if __name__ == "__main__":
    main()
