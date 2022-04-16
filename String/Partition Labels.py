# We only need to keep tracking the last appearance of each letter.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        seg_start, seg_end = 0, 0  # inclusive
        res = []
        for i, c in enumerate(s):
            seg_end = max(seg_end, last[c])
            if i == seg_end:
                res.append(seg_end - seg_start + 1)
                seg_start = i + 1

        return res

# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         last = [0] * 26 # a map to save the last index of each letter
#         for i in range(len(s)):
#             last[ord(s[i]) - ord('a')] = i

#         seg_start, seg_end = 0,0
#         ans = []
#         for i in range(len(s)):
#             # each char in s can extend the end of a segment to last(c)
#             seg_end = max(seg_end, last[ord(s[i]) - ord('a')])
#             # we can only do partiton when i is already the end of current segment
#             if i == seg_end:
#                 ans.append(seg_end - seg_start + 1)
#                 seg_start = i + 1
#         return ans


# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         ranges = [[ float('inf'), -float('inf')] for _ in range(26)]
#         for i in range(len(s)):
#             idx = ord(s[i]) - ord('a')
#             ranges[idx][0] = min(ranges[idx][0], i)
#             ranges[idx][1] = max(ranges[idx][1], i)

#         # sort intervals by start

#         # merge intervals

#         # every element within the merged intervals is invalid to partition

#         return None