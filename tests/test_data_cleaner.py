# tests/test_data_cleaner.py
from data_cleaner import clean_data

def test_clean_data_removes_negatives():
    values = [10, -5, 3, -1, 0]
    assert clean_data(values) == [10, 3, 0]  # negative numbers removed
