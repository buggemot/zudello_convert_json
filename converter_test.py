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
