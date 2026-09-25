"""
HMW07trees.py
====================================
This is an example file with trees.

| Author: Kyriacos Savva
| Date: 2026 25 September
"""
import turtle
import random

def draw_tree_1(branch_len, pen_size, t):
    """
    Tree 1:
    - 4 branches per intersection at equal angles (e.g., 90, 30, -30, -90 relative to current heading)
    - Starts thick and gets thinner at each intersection
    - End branches are wide and green (leaves)
    """
    if branch_len < 15:
        # Base case: draw leaves
        t.color("green")
        t.pensize(8)
        t.forward(branch_len)
        t.backward(branch_len)
        return

    # Draw current branch
    t.color("saddlebrown")
    t.pensize(pen_size)
    t.forward(branch_len)

    # 4 branches split equally across 180 degrees (-90, -30, 30, 90)
    angles = [-90, -30, 30, 90]
    
    for angle in angles:
        t.left(angle)
        draw_tree_1(branch_len - 15, max(1, pen_size - 2), t)
        t.right(angle)  # Restore original heading

    # Return to previous position
    t.penup()
    t.backward(branch_len)
    t.pendown()


def draw_tree_2(branch_len, pen_size, t):
    """
    Tree 2:
    - Random branching angle between 15 and 45 degrees
    - Random length reduction at each step
    - Random number of branches (2 to 4 branches per intersection)
    - Dynamic thickness and leaf coloration
    """
    if branch_len < 10:
        # Base case: leaves
        t.color("forestgreen")
        t.pensize(6)
        t.forward(branch_len)
        t.backward(branch_len)
        return

    # Draw main branch
    t.color("sienna")
    t.pensize(pen_size)
    t.forward(branch_len)

    # Random number of split branches at this intersection
    num_branches = random.randint(2, 4)

    for _ in range(num_branches):
        # Random angle between -45 and 45 degrees
        angle = random.uniform(15, 45) * random.choice([-1, 1])
        # Random reduction in length
        len_subtraction = random.uniform(10, 20)
        
        t.left(angle)
        draw_tree_2(branch_len - len_subtraction, max(1, pen_size - 1.5), t)
        t.right(angle)

    # Return to previous position
    t.penup()
    t.backward(branch_len)
    t.pendown()


def main():
    screen = turtle.Screen()
    screen.setup(width=1000, height=700)
    screen.bgcolor("white")
    screen.tracer(0)  # Speed up rendering

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # --- Draw Tree 1 ---
    t.penup()
    t.goto(-250, -250)
    t.setheading(90)
    t.pendown()
    draw_tree_1(branch_len=60, pen_size=10, t=t)

    # --- Draw Tree 2 ---
    t.penup()
    t.goto(250, -250)
    t.setheading(90)
    t.pendown()
    draw_tree_2(branch_len=75, pen_size=8, t=t)

    screen.update()
    
    # Save screen image (optional depending on system setups, or screenshot manually for README)
    ts = t.getscreen()
    ts.getcanvas().postscript(file="trees.eps")

    screen.exitonclick()

if __name__ == "__main__":
    main()