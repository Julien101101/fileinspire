# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

from pathlib import Path
from sys import exit

def list_contents(directory, recursive=False, only_files=False, search_name=None, search_extension=None):
    # Implement the listing functionality here
    pass

def create_file(directory, file_name):
    # Implement the file creation functionality here
    pass

def delete_file(file_path):
    # Implement the file deletion functionality here
    pass

def read_file(file_path):
    # Implement the file reading functionality here
    pass

def inspector(user_input):
    command = user_input[0]

    if command == 'Q':
        exit()
    elif command == 'L':
        # Extract options and call list_contents function
        pass
    elif command == 'C':
        # Extract options and call create_file function
        pass
    elif command == 'D':
        # Extract file path and call delete_file function
        pass
    elif command == 'R':
        # Extract file path and call read_file function
        pass
    else:
        print("ERROR: Unknown command")

def main():
    try:
        while True:
            user_input = input("Enter command: ")
            inspector(user_input.split())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
