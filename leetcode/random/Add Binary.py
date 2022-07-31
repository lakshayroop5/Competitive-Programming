# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         alen = len(a)
#         blen = len(b)
#         a = int(a)
#         b = int(b)
#         a_num = Solution.convert(a, alen)
#         b_num = Solution.convert(b, blen)
#         s = a_num+b_num
#         if s == 0: return "0"
#         x = str()
#         while s>0:
#             x = str(s%2) + x
#             s = s//2
#         return x
#
#
#     @staticmethod
#     def convert(a: int, alen: int) -> int:
#         sum = 0
#         for i in range(alen):
#             sum = sum + (a % 10)*(2**i)
#             a = a//10
#         return sum

o = str()
o = o + 'a'
o = o + 'b'
c = list(o)
print(c)
