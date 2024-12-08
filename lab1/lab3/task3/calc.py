with open("task.in") as f:
    n, k, m = map(int, f.readline().split())
    
    plans = []
    for _ in range(m):
        l, r, c, p = map(int, f.readline().split())
        plans.append((l, r, c, p))

cost_per_day = [float('inf')] * (n + 1)

for day in range(1, n + 1):
    available_plans = [(c, p) for l, r, c, p in plans if l <= day <= r]
    
    available_plans.sort(key=lambda x: x[1])
    
    cores_needed = k
    day_cost = 0
    for cores, price in available_plans:
        if cores_needed <= 0:
            break
        cores_to_rent = min(cores_needed, cores)
        day_cost += cores_to_rent * price
        cores_needed -= cores_to_rent
    
    if cores_needed > 0:
        cost_per_day[day] = float('inf')
    else:
        cost_per_day[day] = day_cost

if any(cost == float('inf') for cost in cost_per_day[1:]):
    print("Невозможно арендовать нужное количество ядер каждый день")
else:
    with open("task.out", "w") as f_out:
        f_out.write(str(sum(cost_per_day[1:])) + "\n")
