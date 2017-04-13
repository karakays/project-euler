def find_total_change_ways(coins, coin_index, amount):
    # we made a change! amount reached 0.
    if not amount:
        return 1
     
    # Amount reached less than 0, so return
    if amount < 0:
        return 0
 
    # If there are no coins and n is greater than 0, then no solution exist
    if coin_index < 0 and amount >= 1:
        return 0
 
    # count is sum of solutions including S[m-1] excluding S[m-1]
    return find_total_change_ways(coins, coin_index- 1, amount) + find_total_change_ways(coins, coin_index, amount - coins[coin_index] )


def find_total_change_ways_memo(coins, total_amount):
    def init_memo():
        change_memo = [None] * (len(coins) + 1)
        for i in range(len(change_memo)):
            change_memo[i] = [None for a in range(0, total_amount + 1)]
        for i in range(total_amount + 1):
            change_memo[0][i] = 0
        for i in range(len(coins) + 1):
            change_memo[i][0] = 1 
        return change_memo
	
    change_memo = init_memo()
    for coin_ind in range(1, len(change_memo)):
        for amount in range(1, len(change_memo[coin_ind])):
	        if coins[coin_ind - 1] <= amount:
                change_memo[coin_ind][amount] = change_memo[coin_ind - 1][amount] + change_memo[coin_ind][amount - coins[coin_ind - 1]]
			else:
                change_memo[coin_ind][amount] = change_memo[coin_ind - 1][amount] 

    return change_memo[len(coins)][total_amount]


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print find_total_change_ways(coins, len(coins) - 1, 200)
    print find_total_change_ways_memo(coins, 200)


if '__main__' == __name__:
    main()

