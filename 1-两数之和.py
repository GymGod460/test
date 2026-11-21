#  哈希表 
# 进入循环
# key为对应得之 vlaue为下标
# 条件判断 找到就返回
# 没找到就存入
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash1={}
        for index,val in enumerate (nums):
            x=target-val
            if x in hash:
                return [hash1[x],index]
            else:
                hash1[val]=index


            
