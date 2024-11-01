import heapq

# Клас для представлення графа за допомогою списків суміжності
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Кількість вершин у графі
        self.graph = {i: [] for i in range(vertices)}  # Ініціалізація графа

    # Додавання ребра у граф
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))  # Додаємо напрямлене ребро (u -> v)
        self.graph[v].append((u, weight))  # Додаємо напрямлене ребро (v -> u) для неорієнтованого графа

    # Функція для виконання алгоритму Дейкстри
    def dijkstra(self, start):
        # Ініціалізація відстаней до всіх вершин як нескінченність
        distances = {i: float('inf') for i in range(self.V)}
        distances[start] = 0  # Відстань до стартової вершини = 0

        # Мін-heap для зберігання вершин, починаємо з початкової вершини
        min_heap = [(0, start)]  # (відстань, вершина)

        # Виконуємо поки в купі є елементи
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            # Якщо поточна відстань більше відомої, пропускаємо її
            if current_distance > distances[current_vertex]:
                continue

            # Оновлюємо відстані до суміжних вершин
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо нова відстань коротша, оновлюємо її
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances


# Створення графа
graph = Graph(5)  # Приклад з 5 вершинами
graph.add_edge(0, 1, 10)
graph.add_edge(0, 4, 5)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 3, 4)
graph.add_edge(3, 4, 7)
graph.add_edge(4, 1, 3)
graph.add_edge(4, 2, 9)

# Виклик алгоритму Дейкстри
start_vertex = 0
distances = graph.dijkstra(start_vertex)

# Виведення найкоротших шляхів
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in distances.items():
    print(f"Відстань до вершини {vertex}: {distance}")
