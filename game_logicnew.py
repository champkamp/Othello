# Nicholas Imkamp 62086284

class Othello:
    
    def __init__(self, rows: int, columns: int, turn: str, top_left: int, end: str):

        self._rows = rows
        self._columns = columns
        self._top_left = top_left[0].upper()
        self._board = self._create_board()
        self._turn = turn[0].upper()
        self._start = self._start_point()
        
    def _create_board(self) -> list: 

        result = [ ]
        
        for col in range(self._columns):
            temp = [ ]
            for row in range(self._rows):
                temp.append('')
            result.append(temp)
                   
        return result

    def _start_point(self):
        
        self._board[self._columns//2 - 1][self._rows//2 - 1] = self._top_left
        self._board[self._columns//2][self._rows//2 - 1] = self._get_opposite_turn(self._top_left)
        self._board[self._columns//2 - 1][self._rows//2] = self._get_opposite_turn(self._top_left)
        self._board[self._columns//2][self._rows//2] = self._top_left
              
    def display_board(self) -> None:

        for row in range(self._rows):
            for col in range(self._columns):
                if self._board[col][row] == '':
                    print('.', end = ' ')
                else:
                    print(self._board[col][row], end = ' ')
            print()
            
    def _get_opposite_turn(self, player: str) -> str:

        if player == 'B':
            return 'W'
        else:
            return 'B'
    
    def _in_board(self, column_index: int, row_index: int) -> bool:

        return 0 <= column_index < self._columns and 0 <= row_index < self._rows
            
    def _one_direction(self,row_add,col_add,row,col) -> list:
        result=[]
        r=row+row_add
        c=col+col_add
        self._in_board(c,r)
        
        if False == self._in_board(c,r):
            return result 
            
        elif self._board[r][c]==self._turn or self._board[r][c]=='':
            return result
        elif self._board[r][c]==self._get_opposite_turn(self):
            for i in range(row, max(self._rows, self._columns)):
                r += row_add
                c += col_add

                if False == self._in_board(c,r):
                    return []
                elif self._board[r][c]=='':
                    return []
                elif self._board[r][c]==self._turn:
                    return result
                else:
                    result.append((r,c))
                            
                
        
        
    def _list_to_flip(self, col: int, row: int) -> list:
        result = self._one_direction(0,1,row,col) + self._one_direction(0,-1,row,col) + self._one_direction(-1,0,row,col) + self._one_direction(1,0,row,col) + self._one_direction(-1,1,row,col) + self._one_direction(-1,-1,row,col) + self._one_direction(1,1,row,col) + self._one_direction(1,-1,row,col)
        return result
        
        


#not tested
    
    def _most_pieces():
        
        if  count("B") > count("W"):

            print("Black wins.")

        elif count("W") > count("B"):

            print("White wins.")

        else:

            print("Tie game.")

#not tested
            
    def _fewest_pieces():

        if  count("B") < count("W"):

            print("Black wins.")

        elif count("W") < count("B"):

            print("White wins.")

        else:

            print("Tie game.")
#not tested

    def _score():

        display_white = self._board.count("W")
        display_black = self._board.count("B")
        display_score = (display_white, display_black)
        print(display_score)

        if display_white > display_black:
            print("White wins")

        elif display_black > display_white:
                print("Black wins")

        elif display_white == display_black:
                    print("Tie game")
        else:
            print("Invalid")
        

    

    def player_move(self, color: str, col: int, row: int):

        self._board[col][row] = color

        for piece in self._list_to_flip(col, row):


            if self._board[piece[0]][piece[1]] == "B":
                self._board[piece[0]][piece[1]] = "W"

            elif self._board[piece[0]][piece[1]] == "W":
                self._board[piece[0]][piece[1]] = "B"

            else:
                return
                

       
        
            
# not tested
##        flip_list = self._list_to_flip(col, row)
##        for flip in flip_list:
##            self._board[flip[0]][flip[1]] = color 
##            

                 

               

        
            

        
        
            
        # look inside the board at position x pos[0] and y pos[1]

        
if __name__ == "__main__":
    def assert_piece(color, col: int, row: int):
        actual = othello._board[col][row]
        assert(actual == color), "expected "+str(col)+","+str(row)+" to have a "+color+" piece, but it was "+actual

    othello = Othello(4, 4, 'w', 'w', 'most',)
    othello.display_board()

    #before moves were made
    assert_piece("W",1,1)
    assert_piece("B",1,2)
    assert_piece("B",2,1)
    assert_piece("W",2,2)
    assert_piece("",0,0)

    #invalid path
    #othello.player_move("B", 1, 1)
    #othello.display_board()


    assert_piece("W", 1,1)
    assert_piece("",1,3)
    assert_piece("B",1,2)

    #valid path
    #othello.player_move("B", 2,3)
    #othello.display_board()
    #othello.display_board()
    #othello.player_move("W", 2,0)
    #othello.display_board()
    
    #assert_piece("B", 2,3)
    #assert_piece("B", 2,2)
    #assert_piece("W", 2,0)
    #assert_piece("W", 2,1)
    
    

#game logic
#create board
#make move place piece. list of pieces to flip. and flipping actual pieces.
#function to check if move is valid.
#function to check winner or game is over.






# UI
#Crete game state
# While no winner
# display board
# make move
# switch turn
# any valid move?
# if no, switch turn
# any valid moves  if no, break
# print winner
    

            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    
