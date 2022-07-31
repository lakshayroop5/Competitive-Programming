from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]


# CODE
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        p = root
        output = []

        def out(a, o: list):
            al = a.left
            ar = a.right
            print(al.val, ar.val)
            if al is None and ar is None:
                o.append(a.val)
            elif al is None:
                out(ar, o)
            elif ar is None:
                out(al, o)
            else:
                out(al, o)
                out(ar, o)
        out(p, output)
        output.reverse()

        print(output)
        return sum(output)
