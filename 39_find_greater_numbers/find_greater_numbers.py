def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    total = 0
    length = len(nums)
    spot = 0
    for y in range(0,length):
        # print(spot)
        # print(y)
        for z in range(spot,length):
            print(nums[z], nums[y])
            if nums[z] > nums[y]:
                total = total + 1
        spot = spot + 1
    return total