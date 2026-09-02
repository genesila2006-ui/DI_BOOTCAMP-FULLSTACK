import math

class Pagination:
    # Step 2: __init__ Method
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0
        
        # Calculate total number of pages
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.items else 1

    # Step 3: get_visible_items Method
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Navigation Methods
    def go_to_page(self, page_num):
        page_num = int(page_num)
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} out of range (1 to {self.total_pages}).")
        self.current_idx = page_num - 1
        return self  # Return self for method chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = max(0, self.total_pages - 1)
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Step 5 (Bonus): Custom __str__ Method
    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())

    # CamelCase method aliases for method chaining support (e.g., p.nextPage())
    def nextPage(self):
        return self.next_page()

    def prevPage(self):
        return self.previous_page()

    def firstPage(self):
        return self.first_page()

    def lastPage(self):
        return self.last_page()

    def goToPage(self, page_num):
        return self.go_to_page(page_num)

    def getVisibleItems(self):
        return self.get_visible_items()


# --- Step 6: Testing the Code ---

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# Initial visible items (Page 1)
print(p.get_visible_items())
# Output: ['a', 'b', 'c', 'd']

# Move to next page (Page 2)
p.next_page()
print(p.get_visible_items())
# Output: ['e', 'f', 'g', 'h']

# Jump to last page (Page 7)
p.last_page()
print(p.get_visible_items())
# Output: ['y', 'z']

# Test __str__() method
p.first_page()
print("\n--- Printed Page 1 ---")
print(str(p))
# Output:
# a
# b
# c
# d

# Method Chaining Test (Bonus)
p.first_page()
chained_result = p.nextPage().nextPage().nextPage().getVisibleItems()
print("\nChained Result:", chained_result)
# Output: ['m', 'n', 'o', 'p']

# Error Handling Test
try:
    p.go_to_page(10)
except ValueError as e:
    print("\nError caught:", e)

try:
    p.go_to_page(0)
except ValueError as e:
    print("Error caught:", e)