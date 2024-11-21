# code here
prices: list[int] = [100, 180, 260, 310, 40, 535, 690]
arrLen = len(prices)
if arrLen<2:
    totalProfit = 0
else:    
    totalProfit = 0
    for i in range(1,arrLen):
        if prices[i-1] < prices[i]:
            totalProfit = totalProfit + prices[i] - prices[i-1]
        
print(totalProfit)