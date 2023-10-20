class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0]
        if amount == 0:
            return 0
    

        for i in range(1,amount+1):
            min_i = []
            # print('this is i', i,arr)

            for j in range(len(coins)):
                if i-coins[j] < 0:
                    # print('no value', i, coins[j])
                    continue
                elif i-coins[j] >= 0:
                    # print('fit to the value', i,coins[j])
                    if arr[i-coins[j]] == -1:
                        continue
                    else:
                        min_i.append(arr[i-coins[j]]+1)
            
            # print('end of one cycle', min_i)
            if len(min_i)<1:
                arr.append(-1)
            else:
                # print('cannot find?',min(min_i))
                if min(min_i) == -1:
                    arr.append(-1)
                else:
                    arr.append(min(min_i))
        # print('finam arryal',arr)
        return arr[-1]