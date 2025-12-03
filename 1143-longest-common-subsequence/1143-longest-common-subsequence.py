class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Use simple variables for clarity
        m, n = len(text1), len(text2)

        # Create a 2D grid initialized with 0
        # Dimensions are (m+1) x (n+1) to handle empty string base case (row/col 0)
        # dp[i][j] represents LCS of text1[:i] and text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Iterate through the grid
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, add 1 to the result from the previous diagonal
                # Note: text1[i-1] accesses the current char because dp is 1-indexed
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # If no match, take the max of skipping a char from text1 OR text2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right cell contains the answer for the full strings
        return dp[m][n]