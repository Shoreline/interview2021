class Solution:
    def is_ipv4(self, IP: str) -> str:
        segs = IP.split('.')
        for x in segs:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def is_ipv6(self, IP: str) -> str:
        segs = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in segs:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.is_ipv4(IP)
        elif IP.count(':') == 7:
            return self.is_ipv6(IP)
        else:
            return "Neither"