def draw_field(field):
    for row in range(5):
        if row % 2 == 0:
            practical_row = int(row/2)
            for column in range(5):
                if column % 2 == 0:
                    practical_column = int(column/2)
                    if column != 4:
                        print(field[practical_column][practical_row], end="")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|", end="")
        else:
            print("-----")


player = 1
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
draw_field(current_field)
while True:
    print("Players turn:", player)
    move_row = int(input("Please enter the row:\n"))
    move_colum = int(input("Please enter the column:\n"))
    if player == 1:
        if current_field[move_colum][move_row] == " ":
            current_field[move_colum][move_row] = "X"
            player = 2
    else:
        if current_field[move_colum][move_row] == " ":
            current_field[move_colum][move_row] = "O"
            player = 1
    draw_field(current_field)
