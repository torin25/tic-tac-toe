# game = [[1,0,2],
#         [1,2,0],
#         [1,2,1]]

def win(current_game):
    # horizontal
    for row in current_game:
        # print(row)
        if row.count(row[0])==len(row) and row[0]!=0:
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical
    for i in range(len(current_game)):
        col=[]
        for row in current_game:
            col.append(row[i])
        if col.count(col[0]) == len(col) and col[0]!=0:
            print(f"Player {col[0]} is the winner vertically!")
            return True
        

    # diagonal
    diags=[]
    for j in range(len(current_game)):
        diags.append(current_game[j][j])
    if diags.count(diags[0])==len(diags) and diags[0]!=0:
            print(f"Player {diags[0]} is the winner diagonally! (\\)")
            return True
    
    diags=[]
    for row, col in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if diags.count(diags[0])==len(diags) and diags[0]!=0:
            print(f"Player {diags[0]} is the winner diagonally! (/)")
            return True
    return False

    
def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column]=player
        for count,row in enumerate(game_map):
            print(count,row)
        return game_map
    
    except IndexError as e:
        print("Error: make sure your input for row/column is 0 or 1 or 2",e)
    except Exception as e:
        print("Something went very wrong!",e)

# game_board(game,just_display=True)
# game_board(game_board,player=1,row=3,column=1)

play = True
players = [1,2]
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    game_won = False
    game_board(game,just_display=True)
    current_player=1
    moves=0
    while not game_won:
        print(f"Player {current_player}'s turn.")

        # get input and ensure it is a valid move
        while True:
            try:
                column_choice = int(input("What column do you want to play? (0,1,2): "))
                row_choice = int(input("What row do you want to play? (0,1,2): "))

                if game[row_choice][column_choice] == 0:
                    break
                else:
                    print("\nThat position is already taken! try again.\n")
            except(IndexError, ValueError):
                print("Invalid input! Please enter the numbers between 0 and 2.")
        game = game_board(game,current_player,row_choice,column_choice)
        moves+=1        
        game_won = win(game)

        if game_won:
            print(f"Player {current_player} wins! Game Over.")
            break
        if moves==9:
            print("It's a draw! No more moves left.")
            break

        
        # switching the player
        current_player = 2 if current_player==1 else 1

    play_again = input("Do you want to play again? (Yes/No): ").lower()
    if play_again!="yes":
        play=False
        print("Thanks for playing!!!")
        

    
