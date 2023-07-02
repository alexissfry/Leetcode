class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = []
        
        for s in set1:
            if s in set2:
                result.append(s)
        
        return result