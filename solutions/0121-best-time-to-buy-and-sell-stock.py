# 121. Best Time to Buy and Sell Stock / 买卖股票的最佳时机
# 难度：简单    语言：Python3    日期：2026-10-27
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# 思路：一次遍历，维护「到今天为止的最低价」minprice 和「到今天为止的最大利润」maxprofit。
#       对每个价格 price：若它比最低价还低，就更新买入价；否则算今天的卖出利润 price - minprice，
#       比已有的最大利润大就更新。因为只能买卖一次，买入价必须早于卖出价，
#       而 minprice 只统计到当前这一天之前的价格，所以不会出现「先卖后买」。
# 复杂度：时间 O(n)，空间 O(1)


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice = 10010
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit
