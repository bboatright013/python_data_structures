def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return_list = []
    for thing in lst:
        print(thing)
        if bool(thing):
            print(thing)
            return_list.append(thing)
    return return_list

