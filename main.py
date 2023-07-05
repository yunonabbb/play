import random
def create_board():
    board = [['*' for _ in range(10)] for _ in range(10)]
    return board
def player(board, player_x, player_y):
    board[player_x][player_y] = '@'
def place_enemy(board):
    enemy_x = random.randint(0, 9)
    enemy_y = random.randint(0, 9)
    board[enemy_x][enemy_y] = '+'
def print_board(board):
    for row in board:
        print(' '.join(row))
def is_valid_move(x, y):
    return 0 <= x < 10 and 0 <= y < 10
def play_game():
    player_x = random.randint(0, 9)
    player_y = random.randint(0, 9)
    moves = 5
    level = 1
    enemies = level

    board = create_board()
    player(board, player_x, player_y)

    while enemies > 0:
        print(f"Level: {level}")
        print(f"Moves left: {moves}")
        print_board(board)


        direction = input("Enter direction (w/a/s/d): ")


        new_x, new_y = player_x, player_y
        if direction == 'w':
            new_x -= 1
        elif direction == 'a':
            new_y -= 1
        elif direction == 's':
            new_x += 1
        elif direction == 'd':
            new_y += 1


        if is_valid_move(new_x, new_y):
            moves -= 1
            if board[new_x][new_y] == '+':
                enemies -= 1
                moves += 5
            board[player_x][player_y] = ' '
            player_x, player_y = new_x, new_y
            player(board, player_x, player_y)
            if enemies > 0 and moves <= 0:
                print("Game over! You ran out of moves.")
                break
        else:
            print("Invalid move! Try again.")


        while enemies < level:
            place_enemy(board)
            enemies += 1

        if enemies == 0:
            level += 1
            enemies = level
            moves += 5

    print("Congratulations! You won the game!")

play_game()








