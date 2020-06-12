def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters = []
    letter_dict = {}
    for char in phrase:
        letters.append(char)
    letter_set = set(letters)
    for lett in letter_set:
        letter_dict[lett] = letters.count(lett)
    return letter_dict
    