class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s 
        return string
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            res.append(s[j+1:j+1+count])
            i= j+1+count

        return res