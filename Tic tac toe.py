winning_combinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],  # Vertical
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  # Horizontal
    [1, 5, 9],
    [3, 5, 7],  # Diagonal
]

box_elements = [None] * 9
click = 0
x_attempts = []
o_attempts = []
is_won = False

def handle_click(position):
    global click, is_won

    if box_elements[position] is None and not is_won:
        if click % 2 == 0:
            box_elements[position] = "X"
            x_attempts.append(position + 1)
            result(x_attempts, "X")

        else:
            box_elements[position] = "O"
            o_attempts.append(position + 1)
            result(o_attempts, "O")

        click += 1

        if click == 9 and not is_won:
            print("It's a tie 🤝")
            exit()

def result(players_array, player):
    global is_won

    for combination in winning_combinations:
        if all(pos in players_array for pos in combination):
            is_won = True
            print(f"{player}'s has won..!! 🥳")
            exit()

def display_board():
    for i in range(0, 9, 3):
        print(f"{box_elements[i] or ' '} | {box_elements[i + 1] or ' '} | {box_elements[i + 2] or ' '}")
        if i < 6:
            print("-" * 9)

if __name__ == "__main__":
    while True:
        try:
            position = int(input("Enter the position (1-9): ")) - 1
            if 0 <= position < 9:
                handle_click(position)
                display_board()
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number.")




