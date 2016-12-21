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
        self._board[self._columns//2][self._rows//2 - 1] = self._opposite_player(self._top_left)
        self._board[self._columns//2 - 1][self._rows//2] = self._opposite_player(self._top_left)
        self._board[self._columns//2][self._rows//2] = self._top_left
              
    def display_board(self) -> None:

        for row in range(self._rows):
            for col in range(self._columns):
                if self._board[col][row] == '':
                    print('.', end = ' ')
                else:
                    print(self._board[col][row], end = ' ')
            print()
            
    def _opposite_player(self, player: str) -> str:

        if player == 'B':
            return 'W'
        else:
            return 'B'
    
    def _still_in_board(self, column_index: int, row_index: int) -> bool:

        return 0 <= column_index < self._columns and 0 <= row_index < self._rows
            
    def _list_to_flip(self, column: int, row: int) -> list:
        result = []
        for c in range(column - 2, column + 1):
            for r in range(row - 2, row + 1):
                if self._in_board(c, r) and self._board[c][r] == self._get_opposite_turn():
                    col_change = c - (column-1)
                    row_change = r - (row-1)
                    curr_col = c
                    curr_row = r
                    temp = []
                    while self._in_board(curr_col, curr_row):
                        if self._board[curr_col][curr_row] == self._turn:
                            result.extend(temp)
                            break
                        if self._board[curr_col][curr_row] == self._get_opposite_turn():
                            temp.append((curr_col, curr_row))
                        curr_col += col_change
                        curr_row += row_change
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
        
# not tested

##    def _is_valid(self, move: int) -> list:
##
##        result = []
##
##        if move in display_board() and type(move) == int:
##            
##                if move == True:
##                    result.append("T")
##
##                elif move == False:
##                    result.append("F")
##
##                else:
##
##                    invalid = int(input("Invalid response. Please enter your move?"))

#result  = tuple(result)

        #return result
    
    def current_position(self, pos):
        return (pos[0], pos[1])
    
    def right_of(self, pos):
        return (pos[0], pos[1]+1)
    
    def left_of(self, pos):
        return (pos[0], pos[1]-1)

    def above(self, pos):
        return (pos[0]-1, pos[1])

    def below(self, pos):
        return (pos[0]+1, pos[1])

    def above_right(self, pos):
        return (pos[0]-1, pos[1]+1)

    def above_left(self, pos):
        return (pos[0]-1, pos[1]-1)

    def below_right(self, pos):
        return (pos[0]+1, pos[1]+1)
    
    def below_left(self, pos):
        return (pos[0]+1, pos[1]-1)


    def player_move(self, color: str, row: int, col: int):
        current_position = self._board[row][col]

        for piece in self._list_to_flip(col, row):
            if piece == "B":
                piece = "W"
            if piece == "W":
                piece = "B"
            
        

        if current_position == "W" and color == "B":
            return
        elif current_position == "W" and color == "B":
            return 
        elif current_position == "B" and color == "B":
            return
        elif current_position == "W" and color == "W":
            return
        elif current_position == "":
            self._board[row][col] = color
        elif self._right_of(pos) == color and self._left_of(pos) == color:
            current_postion == color

        elif self._above(pos) == color and self.below(pos) == color:
            current_postion == color

        elif self.above_left(pos) == color and self.below_right(pos) == color:
            current_postion == color

        elif self.above_right(pos) == color and self.below_left(pos) == color:
            current_postion == color

        else:
            print("Invalid")
            return current_position
        
            
# not tested
##        flip_list = self._list_to_flip(col, row)
##        for flip in flip_list:
##            self._board[flip[0]][flip[1]] = color 
##            

                 

               

        
            

        
        
            
        # look inside the board at position x pos[0] and y pos[1]
        
if __name__ == "__main__":
    def assert_piece(color, row: int, col: int):
        actual = othello._board[row][col]
        assert(actual == color), "expected "+str(row)+","+str(col)+" to have a "+color+" piece, but it was "+actual

    othello = Othello(4, 4, 'white', 'white', 'most',)

    othello.display_board()

    #before moves were made
    assert_piece("",0,0)
    assert_piece("B",1,2)
    assert_piece("W",2,2)

    #invalid path
    othello.player_move("B", 1, 1)
    othello.display_board()


    assert_piece("W", 1,1)
    assert_piece("",1,3)
    assert_piece("B",1,2)

    #valid path
    othello.player_move("B", 2,3)
    othello.display_board()
    othello.player_move("W", 2,0)
    othello.display_board()
    
    assert_piece("B", 2,3)
    #assert_piece("B", 2,2)
    assert_piece("W", 2,0)
    #assert_piece("W", 2,1)
    
    othello.display_board()

    

            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    
