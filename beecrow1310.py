# by filipe dev
def calculate_max_profit(days, per_day_cost, revenues):
    max_profit = 0
    current_profit = 0
    
    for revenue in revenues:
        current_profit += revenue - per_day_cost
        max_profit = max(max_profit, current_profit)
        current_profit = max(0, current_profit)  # Reset to 0 if profit becomes negative
    
    return max_profit

while True:
    try:
        N = int(input())
        perDayCost = int(input())
        
        revenues = []
        for _ in range(N):
            revenue = int(input())
            revenues.append(revenue)
        
        max_profit = calculate_max_profit(N, perDayCost, revenues)
        print(max_profit)
    
    except EOFError:
        break
