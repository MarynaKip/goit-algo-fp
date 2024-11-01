import random
import matplotlib.pyplot as plt

# Налаштування параметрів симуляції
num_simulations = 1000000  # Велика кількість кидків для точності результатів
sum_counts = {i: 0 for i in range(2, 13)}  # Ініціалізація підрахунку для кожної суми

# Симуляція кидків кубиків
for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_sum = dice1 + dice2
    sum_counts[roll_sum] += 1

# Обчислення ймовірностей для кожної суми
sum_probabilities = {s: (count / num_simulations) * 100 for s, count in sum_counts.items()}

# Аналітичні розрахунки для порівняння
analytical_probabilities = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100
}

# Підготовка даних для побудови графіка
sums = list(sum_probabilities.keys())
simulation_probs = [sum_probabilities[s] for s in sums]
analytical_probs = [analytical_probabilities[s] for s in sums]

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(sums, simulation_probs, color="skyblue", width=0.4, label="Monte Carlo Simulation")
plt.bar([s + 0.4 for s in sums], analytical_probs, color="orange", width=0.4, label="Analytical Probability")

plt.xlabel("Сума чисел на двох кубиках")
plt.ylabel("Імовірність (%)")
plt.title("Ймовірності сум при киданні двох кубиків: Монте-Карло vs. Аналітичний розрахунок")
plt.xticks(sums)
plt.legend()
plt.show()

# Повернемо значення для перевірки точності
sum_probabilities, analytical_probabilities
