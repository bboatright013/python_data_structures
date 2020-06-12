def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    num1_set = set(num1_str)
    num2_set = set(num2_str)
    num1_obj = {}
    num2_obj = {}
    for num in num1_set:
        num1_obj[str(num)] = num1_str.count(str(num))
    for num in num2_set:
        num2_obj[str(num)] = num2_str.count(str(num))
    check_keys = num1_obj.keys()
    for key in check_keys:
        if num1_obj[key] != num2_obj[key]:
            return False
        else:
            print(f"{key} : {num1_obj[key]}, {num2_obj[key]}")
    return True
        