def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than n, make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    if int(n) >= 3:
        length = len(phrase)
        if length >= n:
            new_n = int(n) - 3
            print(isinstance(new_n, int))
            return_string = phrase[0:new_n]
            return_string_long = f"{return_string}..."
            return return_string_long
        else:
            return phrase
    return "Truncation must be at least 3 characters"
