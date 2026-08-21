class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        dict1 = {}
        for x in s:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x]+=1
        for x in t:
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x]+=1
        return dict == dict1