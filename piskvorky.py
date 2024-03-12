def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(board, player):
    win_combinations = [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],

        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player,player,player] in win_combinations



board = [[" " for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
turn = 0

while 1==1:
        print_board(board)
        player = players[turn % 2]
        print(f"Hráč {player}:")

        row = int(input("Zadej řádek (1, 2, 3): "))
        col = int(input("Zadej sloupec (1, 2, 3): "))

        if board[row-1][col-1] != " ":
            print("Toto pole je již zabrané!")
            continue

        board[row-1][col-1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Hráč {player} vyhrál!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("Remiza!")
            break

        turn += 1