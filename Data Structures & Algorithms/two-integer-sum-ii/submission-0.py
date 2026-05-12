class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 0
        second_idx = len(numbers) - 1 - idx 
        while idx < second_idx:
            fp = numbers[idx]
            sp = numbers[second_idx]
            if (fp + sp) == target:
                return [idx + 1, second_idx + 1]
            if target - fp > sp:
                idx += 1
                continue
            if target - sp < fp:
                second_idx -= 1
                continue
        