# Find the first occurance of a segment (needle) in a given string (haystack)
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# time: O(N*M). N, M are the lengths of haystack and needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        i = 0
        while i + len(needle) < len(haystack) + 1:
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
        return -1


# Other solution (KMP) can do O(M+N):
# https://leetcode.com/problems/implement-strstr/discuss/13024/O(m%2Bn)-and-O(mn)-solutions
# https://github.com/Shoreline/InterviewProblems/blob/833439ec49dd944e0636598435b2bbd9580eae5d/InterviewProblems/src/string/StrStr.java
class Solution_kmp:
    """ Returns index of 1st occurrence of needle in haystack.
    Returns -1 if pattern is not in the haystack.
    Knuth–Morris–Pratt algorithm.
    Time complexity: O(n + m). Space complexity: O(m).
    """

    def strStr(self, haystack: str, needle: str) -> int:
        # special cases
        if not haystack and not needle:
            return 0
        elif not needle:
            return 0

        # build longest proper suffix array for pattern
        lps_array = self.build_lps(needle)

        n, m = len(haystack), len(needle)
        i, j = 0, 0
        while i < n:
            # current characters match, move to the next characters
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # current characters don't match
            else:
                if j > 0:  # try start with previous longest prefix
                    j = lps_array[j - 1]
                # 1st character of needle doesn't match character in haystack
                # go to the next character in haystack
                else:
                    i += 1

            # whole needle matches haystack, match is found
            if j == m:
                return i - m

        # no match was found
        return -1

    """ Helper function for strStr.
    Returns longest proper suffix array for string needle.
    Each lps_array[i] is the length of the longest proper prefix
    which is equal to suffix for needle ending at character i.
    Proper means that whole string cannot be prefix or suffix.

    Time complexity: O(m). Space complexity: O(1), where
    m is the length of the needle, space used for lps array isn't included.
    """

    def build_lps(self, needle):
        m = len(needle)
        lps_array = [0] * m
        i, j = 1, 0  # start from the 2nd character in needle
        while i < m:
            if needle[i] == needle[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            else:
                if j > 0:
                    j = lps_array[j - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        return lps_array