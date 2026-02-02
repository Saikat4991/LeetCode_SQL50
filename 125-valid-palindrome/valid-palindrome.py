class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch for ch in s if ch.isalnum())
        return cleaned_s.lower() == cleaned_s[::-1].lower()

        