#cli_utils/separators.py


def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)


def print_char_separator(char):    
    char = f"{char}"
    print(char[0] * 30)


def print_custom_separator(char, length):
    char = f"{char}"
    if length > 0:
        print(char[0] * length)
    else:
        print("the length should be a number big than zero(0)")


def print_labeled_separator(label, char="*", width=30):
    char = f"{char}"
    if width > 0:
        print(label.center(width, char))
        #width = int(width/2) 
        #print((char * width) + label + (char * width))
    else:
        print("width should be a number bigger than 0")
    
    
def print_box(message, char="*"):
    length = len(message) + 2
    print_custom_separator(char, length)
    print(f"* {message} *")
    print_custom_separator(char, length)
