def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    return_list = []
    if isinstance(num, int):
        if num >= 0:
            for each in range(0, num):
                return_list.append(phrase)
            return ''.join(return_list)
    return None

