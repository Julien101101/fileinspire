# JULIEN SAVARY
# 22982687
# Project 1: File Escavator

from sys import exit


def quit_():
    exit(0)


def inspector(user_input):

    command = user_input[0]
    if command == 'Q':
        quit_()
    elif command == 'L':
        # 9
        pass

    else:
        pass


def main():
    try:
        user_input = input("Enter command: ")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass


if __name__ == "__main__":
    main()
