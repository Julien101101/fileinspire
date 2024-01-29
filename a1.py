from pathlib import Path
from sys import exit

def list_contents(directory, recursive=False, only_files=False, search_name=None, search_extension=None):
    path = Path(directory)

    if not path.is_dir():
        print(f"ERROR: {directory} is not a valid directory.")
        return

    for item in path.iterdir():
        if only_files and not item.is_file():
            continue

        if search_name and search_name not in item.name:
            continue

        if search_extension and not item.name.endswith(search_extension):
            continue

        print(item)

        if recursive and item.is_dir():
            list_contents(item, recursive, only_files, search_name, search_extension)

def create_file(directory, file_name):
    path = Path(directory) / (file_name + ".dsu")

    if path.exists():
        print(f"ERROR: File {path} already exists.")
        return

    try:
        path.touch()
        print(path)
    except Exception as e:
        print(f"ERROR: Failed to create file {path}. {e}")

def delete_file(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"ERROR: File {path} not found.")
        return

    try:
        path.unlink()
        print(f"{path} DELETED")
    except Exception as e:
        print(f"ERROR: Failed to delete file {path}. {e}")

def read_file(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"ERROR: File {path} not found.")
        return

    try:
        with open(path, 'r') as file:
            content = file.read()
            if not content:
                print("EMPTY")
            else:
                print(content)
    except Exception as e:
        print(f"ERROR: Failed to read file {path}. {e}")

def inspector(user_input):
    command = user_input[0]

    if command == 'Q':
        exit()
    elif command == 'L':
        options = user_input[1:]
        list_contents(*options)
    elif command == 'C':
        options = user_input[1:]
        create_file(*options)
    elif command == 'D':
        file_path = user_input[1]
        delete_file(file_path)
    elif command == 'R':
        file_path = user_input[1]
        read_file(file_path)
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
