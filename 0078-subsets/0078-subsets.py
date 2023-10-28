class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []
        def dfs(i): 
            if i >= len(nums): 
                ("hiiiii")
                res.append(subset.copy())
                return 

            # include nums[i]
            print("include: ", subset)
            subset.append(nums[i])
            dfs(i+1)

            # do NOT include nums[i]
            print("do not include: ", subset)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res


            


