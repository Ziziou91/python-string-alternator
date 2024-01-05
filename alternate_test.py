"""testing suite for alternate.py"""
import pytest
from alternate import capitalize_words, capitalize_letters, get_input
from unittest.mock import patch
from unittest import TestCase


def answer():
    ans = get_input()
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'
    
class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('builtins.input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('builtins.input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')

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

def test_capitalise_letter(input_str, expected):
    assert capitalize_letters(input_str)  ==  expected


