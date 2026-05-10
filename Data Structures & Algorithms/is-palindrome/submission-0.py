class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_str = "".join([c for c in s if c.isalnum()]).lower()
        reversed_str = "".join([alphanumeric_str[i] for i in range(len(alphanumeric_str) - 1, -1, -1)]).lower()
        if alphanumeric_str ==  reversed_str:
            return True
        return False

        