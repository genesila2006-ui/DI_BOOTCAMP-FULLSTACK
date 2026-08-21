import re

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Convert matrix_string to a 2D list (matrix)
rows = [line for line in MATRIX_STR.strip('\n').split('\n')]
matrix = [list(row) for row in rows]

num_rows = len(matrix)
num_cols = max(len(row) for row in matrix)

# Step 2 & 3: Iterate column-by-column and concatenate all characters
column_text = ""
for col in range(num_cols):
    for row in range(num_rows):
        if col < len(matrix[row]):
            column_text += matrix[row][col]

# Step 4: Replace group of non-alpha characters between two alpha characters with a space
# (?<=[a-zA-Z]) checks for a letter before, [^a-zA-Z]+ matches non-letters, (?=[a-zA-Z]) checks for a letter after
decoded_message = re.sub(r'(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])', ' ', column_text)

# Step 5: Print the decoded message
print(decoded_message)