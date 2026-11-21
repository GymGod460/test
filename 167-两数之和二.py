# 注意区别原地哈希
# 这题要用双指针

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            add=numbers[l]+numbers[r]
            if add==target:
                return [l+1,r+1]
            elif add<target:
                l+=1
            else:
                r-=1

