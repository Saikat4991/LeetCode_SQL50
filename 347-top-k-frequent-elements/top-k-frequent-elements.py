class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num : corresponding freq
        num_freq = {}
        for i in nums:
            num_freq[i] = 1 + num_freq.get(i,0)
        
        topK_keys = [key for key, _ in sorted(num_freq.items(), key = lambda x: x[1], reverse = True)[:k]]

        return topK_keys