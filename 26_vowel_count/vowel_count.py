def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_map = {}
    vowel_set = {"a","e","i","o","u"}
    new_phrase = phrase.lower()
    for vowel in vowel_set:
        if new_phrase.count(vowel) != 0:
            vowel_map[f'{vowel}'] = new_phrase.count(vowel)
    return vowel_map