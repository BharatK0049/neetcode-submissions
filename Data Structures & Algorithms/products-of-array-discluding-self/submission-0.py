class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def mult_shit(numbas: List[int]) -> int:
            mult = 1
            for i in range(len(numbas)):
                mult *= numbas[i]
            return mult
        
        list_prod = [1] * len(nums)
        for i in range(len(nums)):
            list_rem = nums.copy()
            list_rem.pop(i)
            list_prod[i] = mult_shit(list_rem)
        
        return list_prod