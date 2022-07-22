# 1、当移动 right 扩⼤窗⼝，即加⼊字符时，应该更新哪些数据？ 
# 2、什么条件下，窗⼝应该暂停扩⼤，开始移动 left 缩⼩窗⼝？
# 3、当移动 left 缩⼩窗⼝，即移出字符时，应该更新哪些数据？
# 4、我们要的结果应该在扩⼤窗⼝时还是缩⼩窗⼝时进⾏更新？


# 76 minimum window substring

def minWindow(self, s: str, t: str) -> str:
    if not t or not s: return ''
    l , r = 0,0
    start = 0
    minlen = float('inf')

    needs = Counter(t)
    window ={}
    match = 0
    
    while r < len(s):
        c1 = s[r]
        if c1 in needs:
            window[c1] = window.get(c1,0) + 1
            if window[c1] == needs[c1]:
                match += 1
        
        r += 1
        
        while( match == len(needs) ):
            if r - l < minlen:
                start = l
                minlen = r - l
                
            c2 = s[l]
            if c2 in needs:
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            l += 1
    if minlen == float('inf'): return ''
    return s[start:start+minlen]
            
# 567 Permutation in String
# https://leetcode.com/problems/permutation-in-string/


def checkInclusion(self, s1: str, s2: str) -> bool:
    if not s1 or not s2:return
    
    l, r = 0,0
    needs = Counter(s1)
    window = {}
    
    valid = 0
    
    while r<len(s2):
        c = s2[r]
        r+=1
        
        if c in needs:
            window[c] = window.get(c,0)+1
            if window[c]==needs[c]:
                valid+=1
        while r-l>=len(s1):
            if valid == len(needs):
                return True
            d = s2[l]
            l+=1
            if d in needs:
                if window[d]==needs[d]:
                    valid -=1
                window[d]-=1
    return False


# 438
def findAnagrams(self, s: str, p: str) -> List[int]:
    if not s or not p: return
    
    l,r = 0,0
    output =[]
    
    needs = Counter(p)
    window = {}
    
    valid = 0
    
    while r<len(s):
        
        c1 = s[r]
        r += 1
        
        if c1 in needs:
            window[c1] = window.get(c1,0)+1
            if window[c1]==needs[c1]:
                valid +=1
        
        while r-l >= len(p):
            if valid == len(needs):
                output.append(l)
                
            c2 = s[l]
            l +=1
            
            if c2 in needs:
                if window[c2]==needs[c2]:
                    valid -= 1
                window[c2] -= 1
            
    return output


# 3
def lengthOfLongestSubstring(self, s: str) -> int:
    if not s: return 0
    
    l,r = 0,0
    window ={}
    res = 0
    
    while r<len(s):
        c1 = s[r]
        r+=1
        
        window[c1]=window.get(c1,0)+1
        while window[c1] > 1:
            c2 = s[l]
            l+=1
            window[c2] -= 1
        res = max(res,r-l)
    return res
