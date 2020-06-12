def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    words = phrase.split(" ")
    print(words[0])
    words[0] = words[0].capitalize()
    return_string = " ".join(words)
    return return_string