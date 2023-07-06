# A defanged IP address replaces every period "." with "[.]".
class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace('.', '[.]')
        return '[.]'.join(address.split('.'))