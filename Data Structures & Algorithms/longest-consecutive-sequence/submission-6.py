class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_hash_set = set()
        for n in nums:
            nums_hash_set.add(n)
        longest_consecutive_sequence = set()

        for n in nums:
            if n in longest_consecutive_sequence:
                continue

            possible_consecutive_sequence = set([nums[0]])

            incremented_n = n + 1
            while incremented_n in nums_hash_set:
                possible_consecutive_sequence.add(incremented_n)
                incremented_n += 1

            decremented_n = n - 1
            while decremented_n in nums_hash_set:
                possible_consecutive_sequence.add(decremented_n)
                decremented_n -= 1

            if len(possible_consecutive_sequence) > len(longest_consecutive_sequence):
                longest_consecutive_sequence = possible_consecutive_sequence.copy()

            print("-----")
            print(n)

        return len(longest_consecutive_sequence)
            
        


        