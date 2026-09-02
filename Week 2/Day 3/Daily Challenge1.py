import math
import functools

@functools.total_ordering
class Circle:
    def __init__(self, radius: float = None, diameter: float = None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("Must specify either radius or diameter.")

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: float):
        if value < 0:
            raise ValueError("Diameter cannot be negative.")
        self._radius = float(value) / 2

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @classmethod
    def from_diameter(cls, diameter: float):
        """Alternative constructor using @classmethod decorator."""
        return cls(diameter=diameter)

    # Dunder Methods
    def __repr__(self):
        return f"Circle(radius={self.radius:.2f})"

    def __str__(self):
        return f"Circle -> Radius: {self.radius:.2f}, Diameter: {self.diameter:.2f}, Area: {self.area:.2f}"

    def __add__(self, other: "Circle") -> "Circle":
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other: "Circle") -> bool:
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
# Testing & Verification
# Create instances using radius or diameter
c1 = Circle(radius=5)
c2 = Circle.from_diameter(12)  # Radius: 6
c3 = Circle(radius=3)

# Query properties
print(c1)  # Circle -> Radius: 5.00, Diameter: 10.00, Area: 78.54
print(f"Area of c2: {c2.area:.2f}")

# Addition (__add__)
c4 = c1 + c3  # Radius: 5 + 3 = 8
print(f"Added Circle: {c4}")

# Comparisons (__gt__, __eq__)
print(f"Is c2 > c1? {c2 > c1}")    # True (Radius 6 > 5)
print(f"Is c1 == c3? {c1 == c3}")  # False

# Sorting lists (__lt__)
circles = [c1, c2, c3, c4]
circles.sort()
print("Sorted Circles:", circles)
# Bonus Challenge: Turtle Visualization
# To draw the sorted circles visually on the screen:

import turtle

def draw_sorted_circles(circles_list):
    sorted_circles = sorted(circles_list)
    
    screen = turtle.Screen()
    screen.title("Sorted Circles Visualizer")
    
    pen = turtle.Turtle()
    pen.speed(3)
    
    for c in sorted_circles:
        # Scale up radius for visual clarity on screen
        draw_radius = c.radius * 15
        
        pen.penup()
        pen.sety(-draw_radius)  # Center the circle visually
        pen.pendown()
        pen.circle(draw_radius)
        
        # Label the circle
        pen.penup()
        pen.sety(0)
        pen.write(f" r={c.radius}", align="left", font=("Arial", 10, "normal"))

    turtle.done()

# Uncomment to run visualizer:
# draw_sorted_circles([Circle(radius=2), Circle(radius=6), Circle(radius=4)])