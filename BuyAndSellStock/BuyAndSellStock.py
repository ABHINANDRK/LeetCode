class Stock:
    def __init__(self, stocks):
        self.stocks = stocks

   
    def maxProfit(self):
        tempStocks = self.stocks

        if len(tempStocks) <= 1:
            return 0
        
        left = 0
        right = 1
        maxProfit = 0

        while(right < len(tempStocks)):
            profit = tempStocks[right] - tempStocks[left]
            if profit > maxProfit:
                maxProfit = profit
            
            if tempStocks[left] < tempStocks[right]:
                right = right + 1
            else:
                left = right
                right = right + 1
                
        return maxProfit
            




stock = Stock([1,2])
print(stock.maxProfit())
