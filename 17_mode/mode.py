def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # num_dict = {}
    num_list = []
    most = 0
    number = None
    for num in nums:
        num_list.append(num)
    for num in num_list:
        # num_dict[num] = num.count(num)
        if nums.count(num) > most:
            most = nums.count(num)
            number = num
    print(most)
    return number
    