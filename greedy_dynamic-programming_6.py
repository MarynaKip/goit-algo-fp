items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за зменшенням калорій на одиницю вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    for item, properties in sorted_items:
        if budget >= properties['cost']:
            selected_items.append(item)
            total_calories += properties['calories']
            budget -= properties['cost']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Отримуємо список вартостей і калорійностей
    costs = [item["cost"] for item in items.values()]
    calories = [item["calories"] for item in items.values()]
    item_names = list(items.keys())
    
    # Ініціалізація таблиці динамічного програмування
    n = len(calories)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо таблицю динамічного програмування
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо вибрані страви
    selected_items = []
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]
    
    return selected_items, total_calories

# Приклад використання
budget = 100

# Жадібний алгоритм
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

# Алгоритм динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_result)
print("Сумарна калорійність:", dp_calories)
