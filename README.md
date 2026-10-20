# Drawing of Night Sky Landscape with Python Turtle
## Description

This project creates a simple night-sky scene using Python's built-in `turtle` graphics library. A moon and a field of randomly placed stars light up a midnight-blue sky above a mountain range with snow-capped peaks and a row of pine trees in the foreground.

The program demonstrates basic concepts in Python graphics, including:

* Drawing shapes (lines, triangles and circles)
* Filling shapes with `begin_fill()` / `end_fill()`
* Using functions to modularize code
* Randomization for natural-looking placement
* Layering: objects drawn later appear in front of earlier ones

## Code Overview

The project is structured around reusable functions:

* `draw_star(starlength)` – Draws a small cross-shaped star of the given size.
* `draw_triangle(p1, p2, p3, color)` – Draws a filled triangle from three points. It is the basic building block for mountains, snow caps and trees.
* `draw_mountain(x, mountain_width, mountain_height, color)` – Draws a mountain standing on the bottom edge of the screen, including a white snow cap on its peak.
* `draw_circle(x, y, radius, color)` – Draws a filled circle around a center point.
* `draw_moon(x, y, radius)` – Draws a moon with crater spots, built from several circles.
* `draw_tree(x, tree_height)` – Draws a tree with a brown trunk and three stacked green triangles.

The scene is drawn back to front: stars, moon, mountains, trees. 100 stars with random positions and sizes and 8 trees with random positions and heights make every run look slightly different.

For speed, the program uses `screen.tracer(0)`, so the picture appears almost instantly instead of being drawn step by step.

## How to Run

1. Clone or download this repository.
2. Open the project file project1_artistic_nightsky_code.py in your Python IDE or text editor.
3. Run the program
4. A window will open showing the night sky with moon, mountains and trees.
5. Click anywhere in the window to close it.
