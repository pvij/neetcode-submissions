class Solution:

    # Notes
    # 1. delimiter is needed for cases where a word is 5 character long but, say, starts with 6. 
    # We will incorrectly read 56 as the word length, which would be incorrect. E.g., 
    # 3#cat56#fg6#eh....
    # 2. If something starts with a delimiter, there will be two delimiters one after the other.

    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}{self.delimiter}{s}"
        return encoded

    def decode(self, s: str) -> List[str]:

        def find_delimiter_position(encoded_string):
            pos = None
            for char in encoded_string:
                # the first character can never be the delimiter
                if not pos:
                    pos = 1
                    continue
                if char == self.delimiter:
                    break
                pos += 1
            return pos

        decoded = []
        idx = 0
        remaining_string = s
        while idx < len(s):
            remaining_string = s[idx:]
            delimiter_position = find_delimiter_position(remaining_string)
            word_length = int(remaining_string[0:delimiter_position])
            word = remaining_string[(delimiter_position + 1): (delimiter_position + 1 + word_length)]
            decoded.append(word)
            idx += delimiter_position + word_length + 1
        return decoded
            


