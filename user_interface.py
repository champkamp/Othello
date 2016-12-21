# Nicholas Imkamp 62086284

import game_logic

def ask_user():


    while True:
        result = []

        try:
            rows = int(input("Enter number of rows?"))
            result.append(rows)
            columns = int(input("Enter number of columns?"))
            result.append(columns)
            turn = input("Which of the players will move first: black or white?").strip()
            if turn != "black" and turn != "white":
                raise
            result.append(turn)
            top_left = input("which color disc will be in the top-left position of these four center cells: white (the traditional default) or black?.").strip()
            if turn != "black" and turn != "white":
                raise
            result.append(top_left)
            
            end = input("How would you like to win the game. Most or fewest discs?").strip()
            if end != "most" and end != "fewest":
                raise
            result.append(end)
            
        except:
            print("Entered invalid response.")
        else:
            gl = game_logic.Othello(result[0], result[1], result[2], result[3], result[4]) 
            print("oranges")
        #if game_logic.Othello._still_in_board(self, column_index, row_index):
        #    print("apples")

                
            

if __name__ == "__main__":
    ask_user()
    

               # if _still_in_board(self, column_index, row_index):
                    #_create_board(self, top_left)
            #else:
                #x = int(input("Invalid input. Please enter valid input.")

##            if turn == "black":
##                    display_board(self)
##                    elif turn == "white":
            

#check to see all valid moves around any space.                     
#check to see if the move is valid. Check to see if the piece is next to an opposite color piece.                            
#check to see if you can flip the pieces.
#check to see if you are on edge of the board.
#check to see if there are other pieces that are of the opposite color that are directly next to the current move
#check to see if
#if there BWWW- this is invalid
#check to see if there is valid move for the oppsite and player on the board for every single dash.
#if __name__ == '__main__':
                             

##user_input = ask_user()

##gl.create_board()
##gl.display_board()
##gl.still_on_board(column, row)
##
##while True:
##                             
##Where would you like to drop your piece?
