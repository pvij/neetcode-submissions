from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_counter = Counter(nums)

        # finding the number
        for n in nums:
            x = target - n
            if x in nums_counter:
                if x == n:
                    if nums_counter[n] > 1:
                        break
                else:
                    break

        # finding indices
        indices = []
        for idx, val in enumerate(nums):
            if val in (n, target - n):
                indices.append(idx)
            if len(indices) == 2:
                break

        return sorted(indices)

        