import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("You must specify either a radius or a diameter.")

    @property
    def diameter(self):
        """Returns the diameter of the circle."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Sets the radius based on a new diameter value."""
        self.radius = value / 2

    @property
    def area(self):
        """Computes and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """Adds two circles together and returns a new circle with the combined radius."""
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        """Checks if two circles are equal based on radius."""
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        """Compares if this circle is smaller than another circle (enables sorting)."""
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other):
        """Compares if this circle is larger than another circle."""
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented


# ==========================================
# TESTING THE IMPLEMENTATION
# ==========================================

# Creating circles using radius and diameter
c1 = Circle(radius=5)
c2 = Circle(diameter=20)  # Radius = 10
c3 = Circle(radius=3)

# 1. Query Radius & Diameter
print(f"c1 Radius: {c1.radius}, Diameter: {c1.diameter}")  # 5, 10
print(f"c2 Radius: {c2.radius}, Diameter: {c2.diameter}")  # 10, 20

# 2. Area
print(f"c1 Area: {c1.area:.2f}")

# 3. String representations
print(str(c1))  # Circle(radius=5, diameter=10)

# 4. Addition
c4 = c1 + c3
print(f"c1 + c3 = {c4}")  # Circle with radius 8

# 5. Comparisons
print(f"Is c2 > c1? {c2 > c1}")      # True
print(f"Is c1 == c3? {c1 == c3}")    # False

# 6. Sorting a list of circles
circles = [c1, c2, c3, c4]
circles.sort()
print(f"Sorted Circles: {circles}")

# Bonus Challenge: Draw Sorted Circles with Turtle

import turtle

def draw_sorted_circles(circle_list):
    # Ensure circles are sorted by size before drawing
    circle_list.sort()

    screen = turtle.Screen()
    screen.title("Visualizing Sorted Circles")
    
    t = turtle.Turtle()
    t.speed(3)
    
    for circle in circle_list:
        # Scale up radius slightly for better visual distinction on screen
        draw_radius = circle.radius * 10
        
        t.penup()
        t.sety(-draw_radius)  # Center the circle at origin
        t.pendown()
        t.circle(draw_radius)

    turtle.done()

# Example usage:
# draw_sorted_circles([c1, c2, c3, c4])