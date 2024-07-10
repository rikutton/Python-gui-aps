import random

# ボードの初期化
board = [' ' for _ in range(9)]

# ボードの表示
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# プレイヤーの入力を受け取り、ボードを更新
def player_move(board):
    move = int(input("Choose your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("This spot is already taken.")
        player_move(board)

# CPUのランダムムーブ
def cpu_move(board):
    available_moves = [i for i, x in enumerate(board) if x == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'

# 勝者のチェック
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# 引き分けのチェック
def check_draw(board):
    return ' ' not in board

# ゲームループ
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        cpu_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("CPU wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
