import os
import time
import random

class Cell:
    def __init__(self, x, y, state=False):
        self.x = x
        self.y = y
        self.is_alive = state

    def __str__(self):
        return "█" if self.is_alive else " "


class GameOfLife:
    def __init__(self, width=20, height=10, expandable=False, max_border=10000):
        self.width = width
        self.height = height
        self.expandable = expandable
        self.max_border = max_border
        
        # Store live cell coordinates set for efficient memory usage: (x, y)
        self.live_cells = set()

    def set_initial_state(self, coordinates):
        """Sets initial live cell coordinates."""
        for x, y in coordinates:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.live_cells.add((x, y))

    def randomize(self, density=0.3):
        """Generates a random initial state."""
        self.live_cells.clear()
        for r in range(self.height):
            for c in range(self.width):
                if random.random() < density:
                    self.live_cells.add((c, r))

    def get_neighbors(self, x, y):
        """Returns the 8 adjacent cell coordinates."""
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbors.append((x + dx, y + dy))
        return neighbors

    def count_live_neighbors(self, x, y):
        """Counts how many adjacent cells are alive."""
        count = 0
        for nx, ny in self.get_neighbors(x, y):
            if (nx, ny) in self.live_cells:
                count += 1
        return count

    def next_generation(self):
        """Computes the next state of the universe according to Conway's rules."""
        # Find all cells to evaluate (all live cells + all their immediate neighbors)
        cells_to_check = set(self.live_cells)
        for x, y in self.live_cells:
            for nx, ny in self.get_neighbors(x, y):
                cells_to_check.add((nx, ny))

        next_live_cells = set()

        for x, y in cells_to_check:
            # Check fixed border bounds if expandable is False
            if not self.expandable:
                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    continue
            else:
                # Bonus: Check against maximum boundary threshold to prevent memory overflows
                if abs(x) > self.max_border or abs(y) > self.max_border:
                    continue

            live_neighbors = self.count_live_neighbors(x, y)
            is_currently_alive = (x, y) in self.live_cells

            # Rule 1 & 3: Underpopulation / Overpopulation (handled implicitly by omitting from next_live_cells)
            # Rule 2: Live cell stays alive with 2 or 3 neighbors
            if is_currently_alive and live_neighbors in (2, 3):
                next_live_cells.add((x, y))
            # Rule 4: Dead cell becomes alive with exactly 3 neighbors
            elif not is_currently_alive and live_neighbors == 3:
                next_live_cells.add((x, y))

        self.live_cells = next_live_cells

    def display(self, generation=0):
        """Renders the grid to the console."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== Conway's Game of Life — Generation {generation} ===")
        print("+" + "-" * self.width + "+")

        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                is_alive = (x, y) in self.live_cells
                line += str(Cell(x, y, is_alive))
            line += "|"
            print(line)

        print("+" + "-" * self.width + "+")
        print(f"Active Live Cells: {len(self.live_cells)}")

    def run(self, max_generations=50, delay=0.2):
        """Runs the game simulation loop."""
        for gen in range(1, max_generations + 1):
            self.display(generation=gen)
            if not self.live_cells:
                print("\nAll cells have died. Game Over!")
                break
            self.next_generation()
            time.sleep(delay)


# --- Example Presets & Test Runs ---
if __name__ == "__main__":
    game = GameOfLife(width=30, height=15, expandable=False)

    # Preset: Glider pattern heading towards bottom-right
    glider = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    
    # Preset: Blinker oscillator
    blinker = [(10, 5), (10, 6), (10, 7)]

    game.set_initial_state(glider + blinker)
    
    # Or randomize grid:
    # game.randomize(density=0.25)

    # Start the simulation loop
    game.run(max_generations=40, delay=0.15)