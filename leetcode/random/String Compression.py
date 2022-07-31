class Solution:
    def compress(self, chars: List[str]) -> int:
        t = chars[0]
        c = 0
        o = t
        for i in chars:
            if t == i:
                c += 1
            else:
                if c > 1:
                    o = o + str(c)
                o = o + i
                c = 1
                t = i
        else:
            if c > 1:
                o = o + str(c)
        chars.clear()
        print(chars)
        return len(chars)
