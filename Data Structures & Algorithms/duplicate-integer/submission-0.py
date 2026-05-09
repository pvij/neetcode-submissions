class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()
        for n in nums:
            if n in numbers_seen:
                return True
            numbers_seen.add(n)
        return False

         