# • 1. 用栈实现队列（232）
# 用两个栈实现队列
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        x=self.stack2.pop()
        self.stack2.append(x)
        return x
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

# • 2. 用队列实现栈（225）
# 用一个队列实现，入栈的时候需要旋转队列顺序
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        x=self.stack2.pop()
        self.stack2.append(x)
        return x
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

# • 3. 最小值栈
# • 维护两个栈，一个正常栈，一个最小值栈，pop和push要同时操作。
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[float("inf")]
    def push(self, x: int) -> None:
        self.stack.append(x)
        k=self.minstack[-1]
        if x<k:
            self.minstack.append(x)
        else:
            self.minstack.append(k)
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]

# • 4. 用栈实现括号匹配（20）
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c=='(' or c =='[' or c=='{':
                stack.append(c)
            else:
                if not stack:#没有右括号只有左括号
                    return False
                d=stack.pop()
                #判断是否有非法匹配
                if c==')' and d!='(': f1=True
                else : f1=False
                if c==']' and d!='[': f2=True
                else : f2=False
                if c=='}' and d!='{': f3=True
                else : f3=False
                #如果有不正确的匹配，返回False
                if f1 or f2 or f3: return False 
        return stack==[]#空栈的情况下返回True，否则False
# • 5. 数组中元素与下一个比它大的元素之间的距离（739，medium）
# • 单调栈
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        n=len(T)
        res=[0]*n
        for i in range(n):
            while stack!=[] and T[stack[-1]]<T[i]:
#判断栈顶元素(i之前的元素)是否小于当前值，如果是则找到了最近的升温时间
                res[stack[-1]]=abs(stack[-1]-i)
                stack.pop()
            stack.append(i)
        return res 

# • 6. 循环数组中比当前元素大的下一个元素（503，medium）
# 单调栈，遍历两次数组
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2*n):#相当于将两个nums数组拼起来进行遍历
            while stack!=[] and nums[stack[-1]%n]<nums[i%n]:
                res[stack[-1]%n]=nums[i%n]
                stack.pop()
            stack.append(i)
        return res

# 下一个更大元素I (496,easy)
# 单调栈解法：
# 先对num2数组使用单调栈求解每个元素的下一个最大值，存进hashmap中，在检索nums1中的结果
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        dic={}
        for i in range(n):
            while stack!=[] and nums2[i]>nums2[stack[-1]]:
                dic[nums2[stack.pop()]]=nums2[i]
            stack.append(i)
        
        m=len(nums1)
        res=[-1]*m
        for j in range(m):
            if nums1[j] in dic: 
                res[j]=dic[nums1[j]]
        return res
