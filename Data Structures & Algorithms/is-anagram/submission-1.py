class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {}
        lettersT = {}

        for c in s:
            if c in lettersS:
                lettersS[c] += 1
            else:
                lettersS[c] = 0
        
        for char in t:
            if char in lettersT:
                lettersT[char] += 1
            else:
                lettersT[char] = 0
        
        if lettersS == lettersT:
            return True
        else:
            return False
            
        
        