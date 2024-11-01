import turtle
import math

def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    # Малюємо "стовбур"
    t.forward(branch_length)

    # Копіюємо початкову позицію для правої гілки
    position = t.position()
    heading = t.heading()

    # Рекурсивно малюємо ліву гілку
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося до початкової позиції для правої гілки
    t.setposition(position)
    t.setheading(heading)

    # Рекурсивно малюємо праву гілку
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, angle, depth - 1)

    # Повертаємося назад по стовбуру
    t.setposition(position)
    t.setheading(heading)

def main():
    # Параметри для дерева
    recursion_depth = int(input("Введіть рівень рекурсії: "))
    branch_length = 100  # Довжина початкової гілки
    angle = 45  # Кут розгалуження

    # Ініціалізуємо екран
    screen = turtle.Screen()
    screen.title("Фрактал 'Дерево Піфагора'")
    screen.bgcolor("white")

    # Ініціалізуємо черепаху
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)  # Повертаємо вгору для старту
    t.color("green")

    # Малюємо дерево Піфагора
    draw_pythagoras_tree(t, branch_length, angle, recursion_depth)

    # Завершуємо малювання
    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
