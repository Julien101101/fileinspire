# JULIEN SAVARY
# 22982687
# project 1

# file path recursion system inspector
# [COMMAND] [INPUT] [[-]OPTION] [INPUT]

class SomeException(Exception):
    def __init__(self, message):
        self.message = message



def inspector(informat: str):

    command = informat[0]

    if command.upper == 'Q':
        exit()


    elif command.lower == 'l':
        user_input = informat[2::]


    else:
       pass
    



def main():
    try:
        ics = input()
        inspector(ics)
    except:
        pass
    finally:
        pass



if __name__ == "__main__":
    main()