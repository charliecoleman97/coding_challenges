'''

We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.
'''

'''
Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
'''

''' 
source: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
'''

def minCostToMoveChips(position: list[int]) -> int:
    cost_list = []
    for i in range(0, len(position)):
        # print(f'postition = {position[i]}')
        cost = 0
        for j in range(0, len(position)):
            # print(f'sub-position = {position[j]}')
            if (position[j] - position[i])%2 == 0 or (position[j] + position[i])%2 == 0:
                cost = cost
            elif position[j] == position[i]:
                cost = cost
            else:
                cost += 1
            # print(f'cost = {cost}')  
        cost_list.append(cost)
        # print(f'cost list = {cost_list}')
    return min(cost_list)

print(minCostToMoveChips([1, 3, 5, 7, 9]))

'''
It works but it's slow and overly long 
'''

'''
Better answer found online
'''
# """
# count_even is the number of coins in even pos
# count_odd is the number of coins in odd pos
# """
def minCostToMoveChipsImproved(position: list[int]) -> int:
    count_odd = count_even = 0
    for pos in position:
        if(pos%2==0):
            count_even += 1
        else:
            count_odd += 1
    # """
    # Directly Jump to step 4 as cost of step 1- step 3 is 0
    # """
    print(f"count_odd = {count_odd}")
    return min(count_odd,count_even)

print(minCostToMoveChipsImproved([1, 3, 5, 7, 9]))