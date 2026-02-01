class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key:sortedSTR, values: correspoinding str
        hashMap = {}

        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in hashMap:
                hashMap[sorted_s].append(s)

            else:
                hashMap[sorted_s] = [s]

        return list(hashMap.values())
