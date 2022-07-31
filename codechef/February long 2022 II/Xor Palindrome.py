T = int(input())

for K in range(T):
    n = int(input())
    s = input()
    z = 0
    o = 0

    if n <= 3:
        print("YES")

    else:
        if n % 2 != 0:
            print("YES")
        else:
            z = s.count('0')
            o = s.count('1')
            if z % 2 ==0 and o % 2 ==0:
                print("YES")
            else:
                if z == n//2:
                    print("YES")
                else:
                    print("NO")



