# Assignment 5
# David Cardona Londoño
# 10/22/2024

def print_hello(n):
    # Print "Hello World" n times
    for i in range(n):
        print("Hello World")


def print_hello_alt(n):
    # Extra credit: Alternative solution without a loop (using just print)
    print("Hello World\n" * n)


def print_hello_recursion(n):
    # Extra credit: Recursion solution
    if n > 0:
        print("Hello World")
        print_hello_recursion(n - 1)


def power_list(arr):
    # a. Write a loop that prints each of the numbers on a new line.
    for number in arr:
        print(number)

    # b. Write a loop that prints each number and its square on a new line.
    for number in arr:
        print(f"{number} squared is {number**2}")


def power_list_recursion(arr):
    # Extra credit: Recursion solution for Problem 2
    if len(arr) == 0:
        return
    print(f"{arr[0]} squared is {arr[0] ** 2}")
    power_list_recursion(arr[1:])


def draw_polygon(sides, length, line_color, fill_color):
    """
    Draws a regular polygon with the given parameters.
    
    Parameters:
    sides (int): The number of sides of the polygon.
    length (int): The length of each side of the polygon.
    line_color (str): The color of the polygon's outline (as a string, e.g., 'blue').
    fill_color (str): The color to fill the inside of the polygon (as a string, e.g., 'red').
    """
    import turtle
    t = turtle.Turtle()
    t.color(line_color)
    t.fillcolor(fill_color)

    # Start filling the shape
    t.begin_fill()

    # Draw the polygon
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)

    # End filling
    t.end_fill()

    # Finish drawing
    turtle.done()


def problem_4():
    # Iterate through integers 1 to 50, checking divisibility by 3, 5, or both
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("Divisible by both")
        elif i % 3 == 0:
            print("Divisible by three")
        elif i % 5 == 0:
            print("Divisible by five")
        else:
            print(i)


def problem_5():
    # A simple creative picture using turtle graphics (e.g., a flower pattern)
    import turtle
    t = turtle.Turtle()

    for _ in range(36):
        t.circle(50)
        t.right(10)

    turtle.done()


def main():
    # Call your functions here

    # Problem 1: Print hello world 100 times
    n = 100
    print_hello(n)

    # Problem 2: Print numbers and their squares
    numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    power_list(numbers)

    # Problem 3: Draw polygon
    draw_polygon(6, 100, 'blue', 'yellow')

    # Problem 4: Iterate numbers from 1 to 50
    problem_4()

    # Problem 5: Draw a creative picture
    problem_5()


main()
