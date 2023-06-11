def can_get_target(nums, target):
    if len(nums) == 1 and nums[0] == target:
        return True

    def compute(x, y):
        res = {x + y, x - y, y - x, x * y}
        if y != 0:
            res.add(x / y)
        if x != 0:
            res.add(y / x)
        return res

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            for val in compute(nums[i], nums[j]):
                new_nums = nums[:i] + [val] + nums[j + 1:]
                if can_get_target(new_nums, target):
                    return True

    return False

print(can_get_target([], 5))
print(can_get_target([1, 2], 5))
print(can_get_target([1, 2, 3, 4], 24))
print(can_get_target([3, 43, 44, 9], 24))
print(can_get_target([1, 5, 5, 5], 24))
