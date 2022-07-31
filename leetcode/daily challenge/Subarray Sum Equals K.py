class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        o = 0

        sum_ = 0
        l,r = 0,-1
        while r < n:
            while sum_ < k:
                r += 1
                if r < n:
                    sum_ += nums[r]
            if sum_ == k:
                o += 1
                r += 1
                if r < n:
                    sum_ += nums[r]
            while sum_ > k and l <= r:
                if l < r:
                    sum_ -= nums[l]
                    l += 1
                if l == r:
                    if sum_ == k:
                        o += 1
                    sum_ -= nums[l]
                    l += 1
                    r +=1
                    if r < n:
                        sum_ += nums[r]
        return o

