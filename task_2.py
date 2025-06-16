import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)
        t.right(120)
        koch_snowflake(t, length, level-1)
        t.left(60)
        koch_snowflake(t, length, level-1)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 2 або 3): "))

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # найшвидше малювання
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 300, level)
        t.right(120)

    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()
