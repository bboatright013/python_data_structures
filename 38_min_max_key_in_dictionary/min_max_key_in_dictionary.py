def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    keys = d.keys()
    min_ = None
    max_ = None
    print(keys)
    for key in keys:
        if max_ == None:
            max_ = key
        elif max_ != None and min_ == None:
            if key > max_:
                min_ = max_
                max_ = key
            else: 
                min_ = key
        elif max_ != None and min_ != None:
            if key > max_:
                max_ = key
            if key < min_:
                min_= key
    return (min_, max_)
