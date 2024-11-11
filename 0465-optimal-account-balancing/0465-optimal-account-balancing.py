from collections import defaultdict
from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for lender, receiver, amount in transactions:
            balance[lender] -= amount
            balance[receiver] += amount
        debts = [amount for amount in balance.values() if amount != 0]
        def backtrack(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            min_trans = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    min_trans = min(min_trans, 1 + backtrack(start + 1))
                    debts[i] -= debts[start]
            return min_trans
        return backtrack(0)