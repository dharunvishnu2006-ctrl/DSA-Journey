def stock_span(prices):
    stack = []  
    span = [0] * len(prices)

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]
        stack.append(i)
    return span

prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))