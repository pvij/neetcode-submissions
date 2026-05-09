# [1, 2, 3, 0] - 6
# My output: [6, 3, 2, 6]
# Output: [0, 0, 0, 6]
# [0, 1, 2, 0, 5] - multiple zeroes
# [0, 0, 0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productExceptSelfArray = []
        product = 1
        nonZeroProduct = 1
        nZeros = 0
        for num in nums:
            if num == 0:
                nZeros += 1
                product *= num
                continue    
            nonZeroProduct *= num
            product *= num
        for num in nums:
            if num == 0:
                if nZeros == 1:
                    productExceptSelfArray.append(nonZeroProduct)
                    continue
                productExceptSelfArray.append(0)
                continue
            productExceptSelfArray.append(int(product / num))
        return productExceptSelfArray
        