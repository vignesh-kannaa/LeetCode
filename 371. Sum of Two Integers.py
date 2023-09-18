"""Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a & mask if b > 0 else a


"""SOL:
xor a,b
carry a &b
masking since python is orbitory for -ve values
end b>0, b can be 100..(32 zeros) and can exit"""
