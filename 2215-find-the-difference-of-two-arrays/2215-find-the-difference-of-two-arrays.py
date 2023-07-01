class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        count1 = []
        count2 = []
        
        for i in dict1:
            if i in dict2:
                continue 
            else: 
                count1.append(i)
                
        for i in dict2:
            if i in dict1:
                continue 
            else: 
                count2.append(i)
                
        answer.append(count1)
        answer.append(count2)   
        return answer