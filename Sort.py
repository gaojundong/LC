# • 快速选择
# 用于求解  Kth Element 问题，也就是第 K 个元素的问题。可以使用快速排序的 partition() 进行实现。需要先打乱数组，否则最坏情况下时间复杂度为 O(N2)。
# • 堆
# 用于求解  TopK Elements 问题，也就是 K 个最小元素的问题。可以维护一个大小为 K 的最小堆，最小堆中的元素就是最小元素。最小堆需要使用大顶堆来实现，大顶堆表示堆顶元素是堆中最大元素。这是因为我们要得到 k 个最小的元素，因此当遍历到一个新的元素时，需要知道这个新元素是否比堆中最大的元素更小，更小的话就把堆中最大元素去除，并将新元素添加到堆中。所以我们需要很容易得到最大元素并移除最大元素，大顶堆就能很好满足这个要求。
# 堆也可以用于求解 Kth Element 问题，得到了大小为 k 的最小堆之后，因为使用了大顶堆来实现，因此堆顶元素就是第 k 大的元素。
# 快速选择也可以求解 TopK Elements 问题，因为找到 Kth Element 之后，再遍历一次数组，所有小于等于 Kth Element 的元素都是 TopK Elements。

# ○ 1. Kth Element（215，medium）
# 堆排序（Python内置模块默认小根堆）
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapsort(arr):
            n = len(arr)
            # 新建堆
            for i in range(n , -1, -1):
                sift(arr, i, n)
            # 一个个交换元素
            for i in range(n-1, 0, -1):
                arr[0], arr[i] = arr[i], arr[0]
                sift(arr, 0, i)
        # 重建堆
        def sift(arr, k, n):
            largest = k
            l = 2 * k + 1
            r = 2 * k + 2
            if l < n and arr[k] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != k:
                arr[k], arr[largest] = arr[largest], arr[k]
                sift(arr, largest, n)
        heapsort(nums)
        n=len(nums)
        return nums[n-k]

# • 桶排序
# ○ 1. 出现频率最多的 k 个元素(347,m)
# 堆排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        pq=[]
        for key,value in dic.items():
            if len(pq)<k:
                heapq.heappush(pq,(value,key))
            elif value >pq[0][0]:
                heapq.heapreplace(pq,(value,key))
        
        res=[]
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res
# 桶排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        #桶排序
        bucket=[[] for _ in range(len(nums)+1)]
        for key,value in dic.items():
            #将有value个的元素放入对应下标的桶中
            bucket[value].append(key)
        res=[]
        for i in range(len(nums),-1,-1):
            if bucket[i]:
                res.extend(bucket[i])#将此列表中的所有元素放入res中
            if len(res)>=k:
                break
        return res[:k]

# ○ 2. 按照字符出现次数对字符串排序(451,m)
# 桶排序
class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.Counter(s)
        bucket=[[] for _ in range(len(s)+1)]
        for key,value in dic.items():
            bucket[value].append(key)
        res=""
        for i in range(len(s),-1,-1):
            if bucket[i]:
                for ss in bucket[i]:
                    res=res+ss*i
        return res
# 堆排序
class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.Counter(s)
        pq=[]
        for key,value in dic.items():
            heapq.heappush(pq,(value,key))
        res=''
        while pq:
            temp=heapq.heappop(pq)
            res=temp[1]*temp[0]+res
        return res

# • 荷兰国旗问题
# ○ 1. 按颜色进行排序(75,m)
# ○ 交换排序
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p0,p2=0,n-1
        curr=0
        while curr<=p2:
            if nums[curr]==0:
                nums[p0],nums[curr]=nums[curr],nums[p0]
                p0+=1
                curr+=1
            elif nums[curr]==2:
                nums[p2],nums[curr]=nums[curr],nums[p2]
                p2-=1
            else:
                curr+=1
	
