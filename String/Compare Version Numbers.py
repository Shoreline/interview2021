# convert the input strings into lists of integers.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_list = [int(ver) for ver in version1.split(".")]
        ver2_list = [int(ver) for ver in version2.split(".")]

        for i in range(max(len(ver1_list), len(ver2_list))):
            v1 = ver1_list[i] if i < len(ver1_list) else 0
            v2 = ver2_list[i] if i < len(ver2_list) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
