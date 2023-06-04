# Condition: |i-j| is at most k and nums[i] = nums[j].
# nums = [1,2,3,1], k = 3
# true
# nums = [1,0,1,1], k = 1
# true
# nums = [1,2,3,1,2,3], k = 2
# false
#
# Followup
# Condition: |i-j| is at most k and |nums[i] - nums[j]| is at most t.
# nums = [1,2,3,1], k = 3, t = 0
# true
# nums = [1,0,1,1], k = 1, t = 2
# true
# nums = [1,5,9,1,5,9], k = 2, t = 3
# false


import collections


def haha(nums, k):
    window = collections.defaultdict(int)
    for i, num in enumerate(nums):
        if i - k - 1 >= 0:
            window[nums[i - k - 1]] -= 1
        window[num] += 1

        # print(window)
        if window[num] > 1:
            return True

    return False


# print(haha([1, 2, 3, 1], 3))
# print(haha([1, 0, 1, 1], 1))
# print(haha([1, 2, 3, 1, 2, 3], 2))

# followup
# https://grantjenks.com/docs/sortedcontainers/sortedlist.html
from sortedcontainers import SortedList


def haha2(nums, k, t):
    sorted_window = SortedList()

    for i, num in enumerate(nums):
        if i - k - 1 >= 0:
            sorted_window.remove(nums[i - k - 1])
        sorted_window.add(num)
        index = sorted_window.index(num)

        if index - 1 >= 0 and sorted_window[index] - sorted_window[index - 1] <= t:
            return True
        if index + 1 < len(sorted_window) and sorted_window[index + 1] - sorted_window[index] <= t:
            return True

    return False


#
#
print(haha2([1, 2, 3, 1], 3, 0))
print(haha2([1, 0, 1, 1], 1, 2))
print(haha2([1, 5, 9, 1, 5, 9], 2, 3))
# s = SortedList()
# s.add(10)
# s.add(9)
# s.add(11)
# s.add(5)
# print(s)
# s.remove(10)
# print(s)
# print(s.index(9))
