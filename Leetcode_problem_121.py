class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        l1=[]
        for i in prices:
            l1.append(i)
        l1.sort(reverse=True)
        if prices==l1:
            return 0
        else:
            x,y=min(prices[0:2]),0
            for i in range(l-1):
                x=min(x,prices[i])
                y=max(y,prices[i+1]-x)
                print(x,y)
            return y