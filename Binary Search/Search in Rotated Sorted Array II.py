# /**
#  * Follow up for "Search in Rotated Sorted Array": What if duplicates are
#  * allowed?
#  *
#  * Would this affect the run-time complexity? How and why?
#  *
#  * Write a function to determine if a given target is in the array.
#  */
#
# /*
#  * Only compare nums[mid] with nums[high]: 3 cases: >, <, or ==
#  *
#  * if use the same way as dealing with array with unique elements, we can not
#  * guarantee that if A[I]<=A[m] than I~m is a ascending sub-array (ex: 1,1,3,1)
#  *
#  * there will be error:
#  *
#  * for example:A=[1,3,1,1,1], target=3
#  *
#  * cannot implement binary search and just use linearly scan the whole array A
#  * (cost O(N))? -> wrong. The worst case time is O(N), but still we can apply
#  * binary search. Just need to handle the cases A[mid]==A[low] (or
#  * A[mid]==A[high], equivalent)
#  */
