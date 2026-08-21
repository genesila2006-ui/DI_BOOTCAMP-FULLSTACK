# Step 1: Representing the Game Board
def create_board():
    """Returns a 3x3 grid filled with empty spaces."""
    return [[' ' for _ in range(3)] for _ in range(3)]


# Step 2: Displaying the Game Board
def display_board(board):
    """Prints the current state of the board in a clean visual grid format."""
    print("\n  0   1   2")
    for idx, row in enumerate(board):
        print(f"{idx} " + " | ".join(row))
        if idx < 2:
            print("  " + "---+" * 2 + "---")
    print()


# Step 3: Getting Player Input
def player_input(board, player):
    """Prompts the player for row and column inputs and validates them."""
    while True:
        try:
            row = int(input(f"Player '{player}', enter row (0-2): "))
            col = int(input(f"Player '{player}', enter column (0-2): "))

            # Range check
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue

            # Cell availability check
            if board[row][col] != ' ':
                print("That cell is already taken! Choose another.")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Step 4: Checking for a Winner
def check_win(board, player):
    """Checks rows, columns, and diagonals for 3 matching symbols."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Step 5: Checking for a Tie
def check_tie(board):
    """Checks if every cell on the board is filled."""
    return all(cell != ' ' for row in board for cell in row)


# Step 6: The Main Game Loop
def play():
    """Manages the full game flow."""
    board = create_board()
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")

    while True:
        display_board(board)

        # Get move and update board
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        # Check win condition
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player '{current_player}' wins!")
            break

        # Check tie condition
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


# Run the game
if __name__ == "__main__":
    play()