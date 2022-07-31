# t = int(input())

# for i in range(t):
#     a = list(map(int, input().split()))
#     d1 = a[1] - a[0]
#     d2 = a[2] - a[1]

#     if d1 == d2:
#         print("YES")

#     else:
#         if ((a[0]+a[2])/(2*a[1])).is_integer() and ((a[0]+a[2])/(2*a[1])) > 0:
#             print("YES")
#         elif ((d1+a[1])/a[2]).is_integer() and ((d1+a[1])/a[2]) > 0:
#             print("YES")
#         elif ((a[1]-d2)/a[0]).is_integer() and ((a[1]-d2)/a[0]) > 0:
#             print("YES")
#         else:
#             print("NO")

s = set()
s.add(1)
s.add(4)
s.add(3)
s.add(2)
s.pop()
print(s)