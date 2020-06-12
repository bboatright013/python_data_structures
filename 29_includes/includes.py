def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True
        >>> includes([1, 2, 3], 1, 2)
        False
        >>> includes("hello", "o")
        True
        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True
        >>> includes({1, 2, 3}, 1)
        True
        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True
        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    search_length = len(collection)
    if isinstance(collection, list):
        if start != None:
            for x in range(start, search_length):
                if collection[x] == sought:
                    print("list,isnt none")
                    return True
            return False

        else:
            for x in range(0, search_length):
                if collection[x] == sought:
                    print("list is none")
                    return True
            return False

    elif isinstance(collection, str):
        if start != None:
            for x in range(start, search_length):
                if collection[x] ==sought:
                    print("str, not none")
                    return True
                return False

        else:
            for x in range(0, search_length):
                if collection[x] == sought:
                    print("str none")
                    return True
            return False

    elif isinstance(collection, tuple):
        if start != None:
            for x in range(start, search_length):
                if collection[x] == sought:
                    print("tuple, not none")
                    return True
            return False

        else:
            for x in range(0, search_length):
                if collection[x] ==sought:
                    print("tuple, none")
                    return True
            return False

    elif isinstance(collection, set):
        if collection & {sought}:
            print("set")
            return True
        return False
    elif isinstance(collection, dict):
        col_list = collection.values()
        for item in col_list:
            if sought == item:
                return True
        return False
    else:
        return False
    
    