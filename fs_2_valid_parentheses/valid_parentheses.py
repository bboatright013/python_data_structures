def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left = 0
    right = 0
    _open = False

    for char in parens:
        if left == 0 and char ==')':
            return False
        elif char == '(':
            left = left + 1
            right = right - 1
            if left != right:
                _open = True
        elif char ==')':
            right = right + 1
            left = left - 1
            if left == right:
                _open = False



    print(left, right)

    return not _open


            
