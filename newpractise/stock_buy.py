

class MaxProfit:
    def find_max_profit(self, price):
        max_profit = -99999999999
        min_so_far = price[0]

        for i in range(len(price)):
            profit = price[i]-min_so_far
            max_profit = max(profit, max_profit)
            min_so_far = min(min_so_far, price[i])
        
        return max_profit






stock = [7, 9, 8, 8, 8, 7, 9, 10, 11, 10, 9, 9, 8, 8, 7, 7, 6 , 7, 9, 8, 10, 11, 9, 8, 8, 7, 3, 6, 7, 8, 9]
print(MaxProfit().find_max_profit(stock))