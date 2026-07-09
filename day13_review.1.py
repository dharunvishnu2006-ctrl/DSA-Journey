def min_cost_stairs_variant(cost, start):
    n = len(cost)

    dp = [float('inf')] * (n + 1)
    dp[start] = 0

    for i in range(start, n):
        if dp[i] != float('inf'):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            if i + 2 <= n:
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])

    return dp[n]