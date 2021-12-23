"""
Problem:
 Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another day.
"""

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Approach 1 - Brute Force 
# Two loops and calculate he difference between them and take the larges one
def stock_brute_force(A):
    max_profit = 0
    for i in range(0, len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit

print(stock_brute_force(A))


# Approach 2 - Linear complexity 
def stock(A):
     max_profit = 0
     min_price = A[0]

     for price in A:
         min_price = min(min_price, price)
         compare_profit = price - min_price

         max_profit = max(max_profit, compare_profit)

     return max_profit

print(stock(A))


          
             
