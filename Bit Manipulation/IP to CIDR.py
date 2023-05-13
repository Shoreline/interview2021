class Solution:
    def ipToCIDR(self, ip, n):
        num = self.ip2num(ip)
        # print(ip, num)
        end = num + n - 1

        covered = 0 # already covered numbers. When covered == n we are done.
        cur = num   # current number
        ans = []

        while covered < n:
            zeroes = self.trailing_zeroes(cur)
            while 2 ** zeroes + covered > n:  # not allowed to cover outside of n
                zeroes -= 1

            ans.append(self.num2ip(cur) + "/" + str(32 - zeroes))
            covered += 2 ** zeroes
            cur = cur + 2 ** zeroes
        return ans

    # count trailing zeros of the binary form of the input number
    def trailing_zeroes(self, num):
        if num == 0:
            return 32
        ans = 0
        while num and num % 2 == 0:
            ans += 1
            num = num >> 1
        return ans

    # Convert ip (a string) into an integer
    def ip2num(self, ip):
        ans = 0
        ip_list = ip.split(".")
        for i, digit in enumerate(ip_list[::-1]):
            # print(i, digit, " | ", (int(digit)) << (8 * i))
            # ans += (int(digit)) << (8 * i)
            ans += int(digit) * (256 ** i)
        return ans

    def num2ip(self, num):
        ans = []
        for i in range(4):
            tmp = num & (255)
            ans.append(str(tmp))
            num = num >> 8
        return ".".join(ans[::-1])
