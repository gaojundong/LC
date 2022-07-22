# • 1. 数组中两个数的和为给定值(1)
# 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dic={}
        for i in range(n):
            if target-nums[i] in dic :
                return [i,dic[target-nums[i]]]
            dic[nums[i]]=i 
        return None
# 二分法
# 双指针

# • 2. 判断数组是否含有重复元素(217,easy)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        dic={}
        for i in range(n):
            if nums[i] in dic:
                return True
            dic[nums[i]]=1
        return False

# • 3. 最长和谐序列(594，easy)
# 两次遍历
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        res=0
        for k in dic:
            if int(k+1) in dic:
                res=max(res,int(dic[k])+int(dic[k+1]))
        return res

# 一次遍历
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        res=0
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
            if nums[i]+1 in dic:
                res=max(res,int(dic[nums[i]])+int(dic[nums[i]+1]))
            if nums[i]-1 in dic:
                res=max(res,int(dic[nums[i]])+int(dic[nums[i]-1]))
        return res

# • 4. 最长连续序列(128，hard)
# • 哈希表:用哈希表储存数组，每次从最前边的节点开始判断
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        dic=set(nums)
        for num in dic:
            if num-1 not in dic :#如果num-1存在则表示num不是最前面的节点，就不用遍历了
                curr=num
                lenth=1
                while curr+1 in dic:
                    curr+=1
                    lenth+=1
                res=max(lenth,res)
        return res

# 并查集