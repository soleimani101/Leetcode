class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        selected = []  # List to store the current non-repeating substring
        max_length = 0  # Variable to keep track of the maximum length

        for i in s:
            if i not in selected:
                selected.append(i)
            else:
                # If a repeating character is found, update the max_length if needed
                max_length = max(max_length, len(selected))
                # Find the index of the repeating character
                idx = selected.index(i)
                # Remove all characters before and including the repeating character
                selected = selected[idx+1:]
                # Add the current character to the selected list
                selected.append(i)

        # Update max_length in case the non-repeating substring extends to the end of the string
        max_length = max(max_length, len(selected))

        return max_length
