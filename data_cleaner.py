# data_cleaner.py

def clean_data(values):
    """
    Remove negative values from a list.
    """
    cleaned = [x for x in values if x >= 0]
    return cleaned
