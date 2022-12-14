# Задача 3:
#Создайте программу для игры в ""Крестики-нолики""

from ast import Break


board = list(range(1, 10)) # Создаем список от 1 до 9(в индексы будем ставить "Х" или "O")

wins_coord = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

def creation_board(board): # Создаем метод рисования поля для игры
    print("-" * 13) # Рисуем верхнию границу
    for i in range(3): # В цикле рисуем вертикальные и горизонтальные границы
        print("|", board[0 + i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|") 
        print("-" * 13)
# creation_board(board)  

def take_input(player_token): # Создаем метод проверки правильности введенных пользователем данных
    while True:
        value = input("Куда ставим " + player_token + ' ?: ') # Спрашиваем куда поставить Х или O
        if not (value in '123456789'): # Если юзер ввел что то не из списка от 1 до 9
            print('Ошибка ввода. Повторите, пожалуйста') # То просим его повторить ввод
            continue # Возвращаемся в начало цикла для повторного ввода
        value = int(value) # Преобразуем значение вэлью в целочисленный тип
        if str(board[value - 1]) in'XO': # Если юзер выбирает индекс где уже стоит X или O
            print('Эта клетка уже занята') # То печатаем сообщение
            continue # Возвращаемся в начало цикла для повторного ввода
        board[value - 1] = player_token # Если индекс не занят то записываем туда X или O
        break # Выходим из цикла

def check_win(): # Метод проверки на выигрыш
    for each in wins_coord: # Проверяем в цикле каждый из выгрышных кортежей
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]): 
        # И если значения индексов совпадают(например ХХХ или ООО(условие истино))
            return board[each[1] - 1] # то возвращаем выигрышную позицию
    else:
        return False   # Иначе False    

def main(): # Создаем главную функцию(обЪеденяет все функции)
    counter = 0 # Создаем переменную отвечающию за номерацию хода
    while True: # Создаум цикл
        creation_board(board) # Пока истина рисуем доску
        if counter % 2 == 0: # Если ход четный
            take_input('Х') # Ставим Х
        else: # Каждый нечетный ход
            take_input('О') # Ходят О
        if counter > 3: # Если сделано больше 3х ходов
            winner = check_win() # То проверяем выигрышные комбинации
            if winner: # Если получаем истину
                creation_board(board) # То перерисрвываем доску
                print(f'Поздравляем победителя!: {winner}') # И печатаем победа!(Х или О)
                break # Выходим из цикла
        counter += 1 # Если количество ходов не достигло 3х то переменную увеличиваем на 1
        if counter > 8: # Если юзеры заполнили все поля
            creation_board(board) # Последний раз отрисовываем доску
            print('У нас ничья!') # И пишем Ничья!
            break # Выходим из цикла

main()            
                