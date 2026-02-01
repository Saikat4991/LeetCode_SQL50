class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key:sortedSTR, values: correspoinding str
        hashMap = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            hashMap[sorted_s].append(s)

        return list(hashMap.values())
