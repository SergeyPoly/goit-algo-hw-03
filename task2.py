import turtle

def koch_snowflake(t, length, level):
    """
    Рекурсивно зображує одну сторону сніжинки Коха.
    :param t: Об'єкт turtle.
    :param length: Довжина сторони.
    :param level: Рівень рекурсії.
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)


def draw_snowflake(level):
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set the turtle's speed. 1 is slow, 10 is fast; 0 is fastest.
    t.color("blue")
    t.penup() # Do not let the turtle draw while moving to position (-200, 100).
    t.goto(-200, 100)
    t.pendown() # Enable the turtle to draw.

    # Зображуємо три сторони трикутника
    for _ in range(3):
        koch_snowflake(t, 400, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
        if level < 0:
            raise ValueError("Рівень рекурсії повинен бути цілим додатнім числом.")
        
        draw_snowflake(level)

    except ValueError as e:
        print(f"Помилка вводу: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")