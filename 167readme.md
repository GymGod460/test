# 源代码

```py


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


```

## 注意事项

```py
1.双指针和滑动窗口解决问题不同
2.双指针解决范围查找**相向双指针（两头往中间走）**：多用于**有序数组**，找两数 / 三数之和、反转、比较两端
3.滑动窗口 全部为正数使用 子串使用的概率最大
```
