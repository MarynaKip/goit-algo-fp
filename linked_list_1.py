class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev  # Змінюємо напрямок посилання
            prev = current  # Рухаємо prev на поточний вузол
            current = next_node  # Переходимо до наступного вузла
        self.head = prev  # Новою головою стає останній вузол
    
    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

def merge_sorted_lists(list1, list2):
    dummy = Node()  # Тимчасовий вузол для початку нового списку
    tail = dummy

    # Об'єднуємо списки
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Додаємо залишок списку, якщо він є
    tail.next = list1 if list1 else list2

    # Створюємо новий список для зручності повернення
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list



# # Створення двох відсортованих списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

# Об'єднання списків
merged_list = merge_sorted_lists(list1.head, list2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()

# Реверсування списку
print("\nРеверсований список:")
merged_list.reverse()
merged_list.print_list()

# Сортування реверсованого списку
print("\nСписок після сортування:")
merged_list.insertion_sort()
merged_list.print_list()
