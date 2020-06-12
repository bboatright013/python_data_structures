def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    rev = []
    for char in phrase:
        rev.append(char)
    print(rev)
    rev.reverse()
    print(rev)
    reverse = ''.join(rev)
    print(reverse)
    return reverse
    