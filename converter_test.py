import pytest
import re
import converter

def test_add_extension():
    test_filename = 'test'
    test_filename2 = 'test.json'
    test_filename3 = 'test.txt'

    assert converter.add_extension(test_filename, 'json') == 'test.json'
    assert converter.add_extension(test_filename, '') == 'test'
    assert converter.add_extension(test_filename2, 'json') == 'test.json'
    assert converter.add_extension(test_filename3, 'txt') == 'test.txt'

def test_split_camel_case():

    test = "test"
    expected_test = "test"

    test2 = "teStstrInG"
    expected_test2 = "te Ststr In G"

    test3 = ""
    expected_test3 = ""

    assert converter.split_camel_case(test) == expected_test
    assert converter.split_camel_case(test2) == expected_test2
    assert converter.split_camel_case(test3) == expected_test3
