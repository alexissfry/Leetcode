class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}
        result = []

        for n in nums1:
            counter[n] = 1 

        for n in nums2:
            if n in counter and counter[n] == 1:
                result.append(n)
                counter[n] -= 1 

        return result

        