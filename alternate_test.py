"""testing suite for alternate.py"""
import pytest
from alternate import capitalize_words, capitalize_letters, validate_input

# --------capitalize_words tests--------
def test_capitalize_words_returns_string():
    """ensures that capitalize_words returns a string"""
    assert isinstance(capitalize_words("test"), str)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("this is a test", "this IS a TEST"),
        ("THIS IS A TEST", "this IS a TEST"),
        ("tHe QuiCk FOX jumpED OVEr the LAzy DoG","the QUICK fox JUMPED over THE lazy DOG"),
    )
)

def test_capitalize_words(input_str, expected):
    "test that capitalize_words returns an expected value"
    assert capitalize_words(input_str)  ==  expected

# --------capitalize_letters tests--------
def test_capitalise_letters_returns_string():
    """ensures that capitalize_letters returns a string"""
    assert isinstance(capitalize_letters("test"), str)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("this is a test", "tHiS Is a tEsT"),
        ("THIS IS A TEST", "tHiS Is a tEsT"),
        ("THe QuiCk FOX jumpED OVEr the LAzy DoG","tHe qUiCk fOx jUmPeD OvEr tHe lAzY DoG"),
    )
)

def test_capitalize_letter(input_str, expected):
    """ensures that capitalize_letters returns an expected value"""
    assert capitalize_letters(input_str)  ==  expected

# --------validate_input tests--------
def test_validate_input_returns_string():
    """ensures that validate_input returns a string"""
    assert isinstance(validate_input("letters"), str)

@pytest.mark.parametrize(
    ("input_str", "expected"),
    (
        ("letters", "letters"),
        ("!?letters.", "letters"),
        ("words!?,.", "words"),
        ("[]cancel'%$^*():;./", "cancel"),
        ("word", "word"),
        ('letter', "letter"),
        ("LETTER", "letter"),
        ("WORDS", "words"),
        ("CANCEL", "cancel")
    )
)

def test_validate_input_handles_variants(input_str, expected):
    """ensures that validate_input removes punctuation and handles singular, as well as plural"""
    assert validate_input(input_str)  ==  expected
