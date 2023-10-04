class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        result = []

        for n in nums1:
            set1.add(n)

        set2 = set()
        for n in nums2:
            if n not in set2 and n in set1:
                result.append(n)
                set2.add(n)

        return result 