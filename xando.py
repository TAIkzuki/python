
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
marker = 'X'
def display_board():
    for i in range(0, len(board), 3):
        print('|', board[i], '|', board[i + 1], '|', board[i + 2], '|', "\n____________")


def muve(marker):
    position = int(input("Выберите позицию 1-9 для выставления: "))
    while position!=range(1,9):
        position = int(input("Выберите позицию 1-9 для выставления: "))
        if board[position - 1] == "O" or board[position - 1] == "X":
            print("Ошибка: Dведите свободую клетку 0-9 для выставления ", marker)
        else:board[position - 1] = marker
    else:print('Вы можете ввести только номер позиции от 1-9')
# def example():
#     position = int(input("Выберите позицию 1-9 для выставления: "))
#     while (1 <= board[position] <= 9) or board[position - 1] == "O" or board[position - 1] == "X":
#         print("Ошибка: Введите свободную позицию 1-9 для выставления: ")
#         position = int(input("Выберите позицию 1-9 для выставления: "))
#     return position
def check_winner():
        '''Проверить, есть ли победитель'''
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if all(board[i] == board[line[0]] for i in line):
                print(f"Игрок {board[line[0]]} выиграл!")
                exit()


def move_marker(marker):
    if marker == 'X':
        return 'O'
    elif marker == 'O':
        return 'X'
    else:
        return marker


print("Вы играете за Х \n")


def start_game():
    i = 1
    marker = 'X'
    while i <= 9 :
        check_winner()
        print("Ход игрока", marker)
        display_board()
        # example()
        muve(marker)
        marker= move_marker(marker)
        i+=1
    else:
        display_board()
        print("Ничья!")
start_game()
