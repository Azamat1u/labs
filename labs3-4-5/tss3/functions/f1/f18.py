def spy_game(nums):
    zero_position = None
    double_zero = False

    for num in nums:
        if num == 0:
            zero_position = nums.index(num)
            if double_zero:
                double_zero = False
        elif num == 7 and zero_position is not None:
            return True
        elif num == 0 and zero_position is not None:
            double_zero = True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
