"""A simple app to test Python string methods.

Function takes a string, and depending on the users input it will:
 1) Upper and lower-case alternating characters
 1) Upper and lower-case alternating words
"""
import re

def app() -> None:
    """main function, passes users inputs to the relevant functions"""
    print("""What would you like to do?
        - Capitalise letters - capitalise every other letter
        - Capitalise words - capitalise every other word    
    """)
    method_choice_str = handle_method_input("\nType 'letters' or 'words' to select, or 'cancel' to exit: ")
    final_str = ""
    if method_choice_str == "letters" or method_choice_str == "letter":
        print("\nCapitalise Letters") 
        final_str = capitalize_letters(get_input("\nPlease enter your string: "))
    elif method_choice_str == "words" or method_choice_str == "word":
        print("\n Capitalise Words")
        final_str = capitalize_words(get_input("\nPlease enter your string: "))
    elif method_choice_str == "cancel":
        exit()
    print(f"\n{final_str}")

def get_input(prompt: str) -> str:
    """Simple function to return user input."""
    return input(prompt)

def validate_input(user_str: str) -> str:
    """Checks the passed user_str is valid. If not, recursively ask the user to input again."""
    valid_inputs = ["letters", "letter", "words", "word", "cancel"]
    #sanitise the input
    user_str_no_punc = re.sub(r"[^\w\s]", "", user_str).lower()
    #check input is in valid_inputs
    try:
        if user_str_no_punc.lower() not in valid_inputs:
            raise ValueError(f"\n{"="*10}ERROR! '{user_str}' is not not a valid input! Please try again.{"="*10}\n")
    except ValueError as e:
        print(e)
        user_str_no_punc = handle_method_input("\nType 'letters' or 'words' to select, or 'cancel' to exit: ")
    return user_str_no_punc

def handle_method_input(prompt: str) -> str:
    """Calls get_input before passing to validate_str and then returns."""
    user_str = get_input(prompt)
    validated_str = validate_input(user_str)
    return validated_str

def capitalize_words(user_str: str) -> str:
    """Takes a string provided by user and fully capitalises every other word before returning."""
    user_list = user_str.split()
    return " ".join([word.upper() if i % 2 else word.lower() for i, word in enumerate(user_list)])

def capitalize_letters(user_str: str) -> str:
    """Takes a string provided by user and capitalises every other letter before returning.""" 
    return "".join([word.upper() if i % 2 else word.lower() for i, word in enumerate(user_str)])

# Runs from here. 
print(f"{'*'*60}")
print(f"{'='*24}alternate.py{'='*24}")
print(f"{'*'*60}\n")

if __name__ == "__main__":
    app()

print(f"\n{'*'*60}")
print(f"{'='*22}alternate.py END{'='*22}")
print(f"{'*'*60}")

