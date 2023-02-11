# Rotate 180 degrees -> flip num[i] upside down and let it be the new nums[-i]
# So we need to check if the flipped nums[i] (new nums[-i]) equals to the old nums[-i]
# Only a limited digits is meaningful after being flipped:
#   ("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro_dict = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in stro_dict or stro_dict[num[i]] != num[j]:
                return False
            i += 1
            j -= 1

        return True
