class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # More Space Complexity but O(N)
        prefix = [1] * len(nums)
        prefix_num = 1
        for i in range(len(nums)):
            prefix[i] = prefix_num
            prefix_num *= nums[i]
        print(prefix)

        postfix = [1] * len(nums)
        postfix_num = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix_num
            postfix_num *= nums[i]
        print(postfix)

        final_array = [1] * len(nums)
        for i in range(len(nums)):
            final_array[i] =  prefix[i] * postfix[i]

        return final_array