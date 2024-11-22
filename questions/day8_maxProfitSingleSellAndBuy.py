# prices = [7,1,5,3,6,4]
prices = [1,3]

arrLen = len(prices)

totalProfit: int = 0
if arrLen > 1:
    minSoFar = prices[0]

    for i in range(1,arrLen):
        minSoFar = min(minSoFar, prices[i])

        totalProfit = max(totalProfit, prices[i]-minSoFar)

print(totalProfit)