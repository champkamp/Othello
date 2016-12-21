class Logic:
    
    def __init__(self, rows, columns, start_color, top_left_color, game_type):
        self.rows = rows
        self.columns = columns
        self.start_color = start_color
        self.top_left = top_left_color
        self.game_type = game_type
        self.move_types = [self.left, self.up_left, self.up, self.up_right, self.right, self.down_right, self.down, self.down_left]
        self.score = [2, 2] #Protocol for score (logs amount of white and black pieces on board): score[index1] where index1 = color (0=White, 1=Black)
        self.board = [ [ "-" for x in range(self.columns) ] for y in range(self.rows) ] #Protocol for board (where the different pieces currently reside on the board): board[index1][index2] where index1 = row location of piece and index2 = column location of piece. A "W" marker represents a white piece, a "B" marker represents a black piece and a "-" marker represents an empty space
        self.move_possibilities = [ [ (False, False) for x in range(self.columns) ] for y in range(self.rows) ] #Protocol for move_possibilities (shows whether a color can move in the specified row/column): move_possibilies[index1][index2][index3] where index1 = row, index2 = column, index3 = color (0=White, 1=Black)
        self.move_chart = [ [ [ [False for a in range(8)] for b in range(2) ] for x in range(self.columns) ] for y in range(self.rows) ] #Protocol for move_chart (shows which directions a color can move in specified row/column): move_chart[index1][index2][index3][index4] where index1 = row, index2 = column, index3 = color (0=White, 1=Black), index4 = move_direction (0=left, 1=up_left, 2=up, 3=up_right, 4=right, 5=down_right, 6=down, 7=down_left)
        self.turn = start_color
        if self.turn == "W":
            self.turn_index = 0 #Turn index is used to locate the move data for at each space for either color
        else:
            self.turn_index = 1
        
        
    def initialize_board(self):
        if self.top_left == "W":
            self.board[self.rows//2-1][self.columns//2-1] = "W"
            self.board[self.rows//2-1][self.columns//2] = "B"
            self.board[self.rows//2][self.columns//2-1] = "B"
            self.board[self.rows//2][self.columns//2] = "W"
        else:
            self.board[self.rows//2-1][self.columns//2-1] = "B"
            self.board[self.rows//2-1][self.columns//2] = "W"
            self.board[self.rows//2][self.columns//2-1] = "W"
            self.board[self.rows//2][self.columns//2] = "B"
            
    def make_move(self, row, column):
        moves = self.move_chart[row][column][self.turn_index]
        for move_number in range(len(moves)):
            if moves[move_number]:
                self.move_types[move_number](row, column, self.turn, True)
        self.switch_turn()
        self.update_score()
        self.update_move_chart()
    
    def switch_turn(self):
        if self.turn == "W":
            self.turn = "B"
            self.turn_index=1
        else:
            self.turn = "W"
            self.turn_index=0
            
    def update_score(self):
        print("updating score...")
        white_count = 0
        black_count = 0
        for row in self.board:
            for space in row:
                if space == "W":
                    white_count += 1
                elif space == "B":
                    black_count += 1
        self.score = [white_count, black_count]
                
            
    def update_move_chart(self):
        for y in range(self.rows):
            for x in range(self.columns):
                white_moves = self.check_all(y, x, "W")
                black_moves = self.check_all(y, x, "B")
                self.move_chart[y][x][0] = white_moves
                self.move_chart[y][x][1] = black_moves
                if True in white_moves:
                    if True in black_moves:
                        self.move_possibilities[y][x] = (True, True)
                    else:
                        self.move_possibilities[y][x] = (True, False)
                else:
                    if True in black_moves:
                        self.move_possibilities[y][x] = (False, True)
                    else:
                        self.move_possibilities[y][x] = (False, False)
    
    def check_all(self, row, column, color):
        if self.board[row][column] == "-":
            return [ x(row, column, color, False) for x in self.move_types]
        else:
            return [ False for x in range(len(self.move_types)) ]
    
    def left(self, row, column, move_color, move):
        if column != 0 and column != 1:
            if self.board[row][column-1] != "-" and self.board[row][column-1] != move_color:
                if move:
                    self.board[row][column-1] = move_color
                    self.board[row][column] = move_color
                for x in range(2, column+1):
                    if self.board[row][column-x] == move_color:
                        return True
                    elif self.board[row][column-x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row][column-x] = move_color
        return False
                
    
    def up_left(self, row, column, move_color, move):
        if column != 0 and column != 1 and row != 0 and row != 1:
            if self.board[row-1][column-1] != "-" and self.board[row-1][column-1] != move_color:
                if move:
                    self.board[row-1][column-1] = move_color
                    self.board[row][column] = move_color
                for x, y in zip(range(2, column+1), range(2, row+1)):
                    if self.board[row-y][column-x] == move_color:
                        return True
                    elif self.board[row-y][column-x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row-y][column-x] = move_color
        return False
    
    def up(self, row, column, move_color, move):
        if row != 0 and row != 1:
            if self.board[row-1][column] != "-" and self.board[row-1][column] != move_color:
                if move:
                    self.board[row-1][column] = move_color
                    self.board[row][column] = move_color
                for y in range(2, row+1):
                    if self.board[row-y][column] == move_color:
                        return True
                    elif self.board[row-y][column] == "-":
                        return False
                    else:
                        if move:
                            self.board[row-y][column] = move_color
        return False
    
    def up_right(self, row, column, move_color, move):
        if row != 0 and row != 1 and column != self.columns-1 and column != self.columns-2:
            if self.board[row-1][column+1] != "-" and self.board[row-1][column+1] != move_color:
                if move:
                    self.board[row-1][column+1] = move_color
                    self.board[row][column] = move_color
                for x, y in zip(range(2, self.columns-column), range(2, row+1)):
                    if self.board[row-y][column+x] == move_color:
                        return True
                    elif self.board[row-y][column+x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row-y][column+x] = move_color
        return False
    
    def right(self, row, column, move_color, move):
        if column != self.columns-1 and column != self.columns-2:
            if self.board[row][column+1] != "-" and self.board[row][column+1] != move_color:
                if move:
                    self.board[row][column+1] = move_color
                    self.board[row][column] = move_color
                for x in range(2, self.columns-column):
                    if self.board[row][column+x] == move_color:
                        return True
                    elif self.board[row][column+x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row][column+x] = move_color
        return False
    
    def down_right(self, row, column, move_color, move):
        if row != self.rows-1 and row != self.rows-2 and column != self.columns-1 and column != self.columns-2:
            if self.board[row+1][column+1] != "-" and self.board[row+1][column+1] != move_color:
                if move:
                    self.board[row+1][column+1] = move_color
                    self.board[row][column] = move_color
                for x, y in zip(range(2, self.columns-column), range(2, self.rows-row)):
                    if self.board[row+y][column+x] == move_color:
                        return True
                    elif self.board[row+y][column+x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row+y][column+x] = move_color
        return False
    
    def down(self, row, column, move_color, move):
        if row != self.rows-1 and row != self.rows-2:
            if self.board[row+1][column] != "-" and self.board[row+1][column] != move_color:
                if move:
                    self.board[row+1][column] = move_color
                    self.board[row][column] = move_color
                for y in range(2, self.rows-row):
                    if self.board[row+y][column] == move_color:
                        return True
                    elif self.board[row+y][column] == "-":
                        return False
                    else:
                        if move:
                            self.board[row+y][column] = move_color
        return False
    
    def down_left(self, row, column, move_color, move):
        if row != self.rows-1 and row != self.rows-2 and column != 0 and column != 1:
            if self.board[row+1][column-1] != "-" and self.board[row+1][column-1] != move_color:
                if move:
                    self.board[row+1][column-1] = move_color
                    self.board[row][column] = move_color
                for x, y in zip(range(2, column+1), range(2, self.rows-row)):
                    if self.board[row+y][column-x] == move_color:
                        return True
                    elif self.board[row+y][column-x] == "-":
                        return False
                    else:
                        if move:
                            self.board[row+y][column-x] = move_color
        return False
        
    
    def remaining_moves(self):
        for row in self.move_possibilities:
            for possibility in row:
                if True in possibility:
                    return False
        return True
    
    def remaining_moves_color(self):
        for row in self.move_possibilities:
            for possibility in row:
                if possibility[self.turn_index] == True:
                    return True
        return False
    
    def check_move_possibility(self, row, column):
        return self.move_possibilities[row][column][self.turn_index]
            
        
    def print_board(self):
        for x in range(self.rows):
            print(self.move_possibilities[x])
        print("-----")
