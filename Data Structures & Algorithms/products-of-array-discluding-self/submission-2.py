# [1, 2, 3, 0] - 6
# My output: [6, 3, 2, 6]
# Output: [0, 0, 0, 6]
# [0, 1, 2, 0, 5] - multiple zeroes
# [0, 0, 0]

class Solution:
    # # with division
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     productExceptSelfArray = []
    #     product = 1
    #     nonZeroProduct = 1
    #     nZeros = 0
    #     for num in nums:
    #         if num == 0:
    #             nZeros += 1
    #             product *= num
    #             continue    
    #         nonZeroProduct *= num
    #         product *= num
    #     for num in nums:
    #         if num == 0:
    #             if nZeros == 1:
    #                 productExceptSelfArray.append(nonZeroProduct)
    #                 continue
    #             productExceptSelfArray.append(0)
    #             continue
    #         productExceptSelfArray.append(int(product / num))
    #     return productExceptSelfArray


# [-2, 3, 0, 1, 9]
# [-2, -2, -6, 0, 0] - prefix sum, x_i - x_0 * ... * x_(i-1), if i == 0, x_0
# [0, 0, 9, 9, 9] - suffix sum, x_i = x_(i + 1) * ... x_n, if i == (n - 1), x_n
# Output: [0, 0, -54, 0, 0]

# [2, 3, 1, 4, 5]
# prefix product = [2, 2, 6, 6, 24]
# suffix product = [60, 20, 20, 5, 5]


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = 1
        prefixProductArr = [prefixProduct]
        for idx in range(len(nums)):
            if idx == 0:
                continue
            prefixProduct *= nums[idx-1]
            prefixProductArr.append(prefixProduct)

        suffixProduct = 1
        nums_len = len(nums)
        suffixProductArr = [suffixProduct] * nums_len
        for idx in range(nums_len - 1, -1, -1):
            if idx == nums_len - 1:
                continue
            suffixProduct *= nums[idx + 1]
            suffixProductArr[idx] = suffixProduct

        productOfArrayExceptSelf = []
        for idx in range(len(nums)):
            productOfArrayExceptSelf.append(prefixProductArr[idx] * suffixProductArr[idx])

        return productOfArrayExceptSelf



