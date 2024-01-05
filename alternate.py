"""A simple function to test Python string methods.

Function takes a string, and depending on the users input it will:
 1) Upper and lower-case alternating characters
 1) Upper and lower-case alternating words
"""

def get_input():
    """Simple function to return user input."""
    return input("please enter a string: ")

def app() -> None:
    print("initial app function")
    user_str = get_input()
    capitalize_letters(user_str)
    print(capitalize_words(user_str))


def capitalize_words(user_str: str) -> str:
    """Takes a string provided by user and fully capitalises every other word before returning."""
    user_list = user_str.split()
    return " ".join([word.upper() if i % 2 else word.lower() for i, word in enumerate(user_list)])
   

def capitalize_letters(user_str: str) -> str:
    """Takes a string provided by user and capitalises every other letter before returning."""
    
    return "".join([word.upper() if i % 2 else word.lower() for i, word in enumerate(user_str)])

print(f"{"="*10}alternate.py{"="*10}\n")

# app()

print(f"\n{"="*10}alternate.py END{"="*10}")
