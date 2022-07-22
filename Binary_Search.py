
def binary_search(self, nums: List[int], target: int) -> int:
    l=len(nums)
    i,j=0,l-1
    if target<nums[0] or target>nums[-1]:
        return -1
    while i<=j:
        d=int((i+j)/2)
        if target<nums[d]:
            j=d-1
        if target>nums[d]:
            i=d+1
        if target==nums[d]:
            return d
    return -1

# 35 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
def searchInsert(self, nums: List[int], target: int) -> int:
    n=len(nums)
    i,j=0,n-1
    while i<=j:
        m=int((i+j)/2)
        if nums[m]==target:
            return m
        elif nums[m]<target:
            i=m+1
        else:
            j=m-1
    return i



#求开方（69）需要使用右中位数，左中位数容易陷入死循环。
def mySqrt(self, x: int) -> int:
    m=int(x/2)
    l,r=0,m+1
    while l<r:
        ind=l+int((r-l+1)/2)
        if ind**2==x:
            return ind
        if ind**2<x and (ind+1)**2>x:
            return ind
        if ind**2>x:
            r=ind-1
        if ind**2<x:
            l=ind+1
    return l

# 2. 大于给定元素的最小元素
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    n=len(letters)
    l,r=0,n-1
    while l<=r:
        m=int((l+r)/2)
        if letters[m]>target:
            r=m-1
        if letters[m]<=target:
            l=m+1
    if l>n-1:
        return letters[0]
    else:
        return letters[l]

# 3. 有序数组的 Single Element（540）
# 题目描述：一个有序数组只有一个数不出现两次，找出这个数。
# 要求以 O(logN) 时间复杂度进行求解，因此不能遍历数组并进行异或操作来求解，这么做的时间复杂度为 O(N)。
# 令 index 为 Single Element 在数组中的位置。在 index 之后，数组中原来存在的成对状态被改变。如果 m 为偶数，并且 m + 1 < index，那么 nums[m] == nums[m + 1]；m + 1 >= index，那么 nums[m] != nums[m + 1]。
# 从上面的规律可以知道，如果 nums[m] == nums[m + 1]，那么 index 所在的数组位置为 [m + 2, h]，此时令 l = m + 2；如果 nums[m] != nums[m + 1]，那么 index 所在的数组位置为 [l, m]，此时令 h = m。
# 因为 h 的赋值表达式为 h = m，那么循环条件也就只能使用 l < h 这种形式。
def singleNonDuplicate(self, nums: List[int]) -> int:
    n=len(nums)
    l,r=0,n-1
    while l<r:
        m=int((l+r)/2) 
        #确保l,r,m都在偶数位，则每次比较只需要与其后面的数比
        #如果与后面的数相同，则m+1之前的所有数都有两个l=m+2
        #如果与后面的数不同，则单个的数在m之前，r=m
        if m%2==1:
            m-=1
        if nums[m]==nums[m+1]:
            l=m+2
        elif nums[m]!=nums[m+1]:
            r=m
    return nums[l]

# 4. 第一个错误的版本(278)
# 题目描述：给定一个元素 n 代表有 [1, 2, ..., n] 版本，在第 x 位置开始出现错误版本，导致后面的版本都错误。可以调用 isBadVersion(int x) 知道某个版本是否错误，要求找到第一个错误的版本。
# 如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，令 r = m；否则第一个错误的版本在 [m + 1, h] 之间，令 l = m + 1。
# 因为 r 的赋值表达式为 r = m，因此循环条件为 l < h。
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l,r=1,n
    while l<r:
        m=int((l+r)/2)
        temp=isBadVersion(m)
        if temp:
            r=m
        else:
            l=m+1
    return l
    #如果r=m+1的话，循环条件需要改成l<=r

# 5. 旋转数组的最小数字(153)

def findMin(self, nums: List[int]) -> int:
    l,r=0,len(nums)-1
    while l<r:
        m=int((l+r)/2)
        if nums[m]<nums[r]:
            #如果中位数小于右边的数，则右半个数组是递增的，最小值在左半个数组中
            r=m
        else:
            #如果中位数大于右边的数，则右半个数组中存在旋转过来的最小数
            l=m+1
    return nums[l]

# 6. 查找区间
# 题目描述：给定一个有序数组 nums 和一个目标 target，要求找到 target 在 nums 中的第一个位置和最后一个位置。
# 可以用二分查找找出第一个位置和最后一个位置，但是寻找的方法有所不同，需要实现两个二分查找。我们将寻找 target 最后一个位置，转换成寻找 target+1 第一个位置，再往前移动一个位置。这样我们只需要实现一个二分查找代码即可。
# 在寻找第一个位置的二分查找代码中，需要注意 h 的取值为 nums.length，而不是 nums.length - 1。先看以下示例：
# nums = [2,2], target = 2
# 如果 h 的取值为 nums.length - 1，那么 last = findFirst(nums, target + 1) - 1 = 1 - 1 = 0。这是因为 findLeft 只会返回 [0, nums.length - 1] 范围的值，对于 findFirst([2,2], 3) ，我们希望返回 3 插入 nums 中的位置，也就是数组最后一个位置再往后一个位置，即 nums.length。所以我们需要将 h 取值为 nums.length，从而使得 findFirst返回的区间更大，能够覆盖 target 大于 nums 最后一个元素的情况。
def searchRange(self, nums: List[int], target: int) -> List[int]:
    l,r=0,len(nums)
    while l<r:
        m=int((l+r)/2)
        if nums[m]>=target:
            r=m
        else:
            l=m+1
    if l==len(nums) or nums[l]!=target:
        #l的判断必须在nums[l]的判断之前，否则会有数组越界错误
        return [-1,-1]
    start=l
    l,r=0,len(nums)
    while l<r:
        m=int((l+r)/2)
        if nums[m]>=target+1:
            r=m
        else:
            l=m+1
    end=l-1
    return [start,end]


