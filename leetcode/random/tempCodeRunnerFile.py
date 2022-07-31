# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = input("enter value of a:")
#         b = input("enter value of b:")
#         alen = len(a)
#         blen = len(b)
#         a = int(a)
#         b = int(b)
#         a_num = Solution.convert(a, alen)
#         b_num = Solution.convert(b, blen)
#         s = a_num+b_num
#         slen = len(s)
#         for i in range(slen):
#             x = str()
#             x = str(s % 2) + x
#             s = s//2
#         return x
#
#
#     def convert(self, a: int, alen: int):
#         for i in range(alen):
#             sum = sum + (a % 10)*(2**i)
#             a = a//10
#         return sum

for i in range(0, 100, 2):
    print(i)