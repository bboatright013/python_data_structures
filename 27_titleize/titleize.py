def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    tmp_list = []
    words = phrase.split()
    for word in words:
        new_word = word.capitalize()
        tmp_list.append(new_word)
    return_list = ' '.join(tmp_list)
    return return_list