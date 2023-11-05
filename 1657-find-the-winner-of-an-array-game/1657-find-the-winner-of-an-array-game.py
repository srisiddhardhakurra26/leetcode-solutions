class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        
        if k >= len(arr):
            return max(arr)
        
        curr_winner = arr[0]
        consec_wins = 0
        for i in range(1, len(arr)):
            if curr_winner > arr[i]:
                consec_wins += 1
            else:
                curr_winner = arr[i]
                consec_wins = 1
            
            if consec_wins == k:
                return curr_winner
        return curr_winner