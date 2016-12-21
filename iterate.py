def assert_piece(color, row: int, col: int):
    actual = othello._board[row][col]
    assert(actual == color), "expected "+str(row)+","+str(col)+" to have a "+color+" piece, but it was "+actual

import game_logic




othello = game_logic.Othello(4, 4, 'white', 'white', 'most',)

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


assert_piece("B", 2,3)
assert_piece("B", 2,2)

othello.display_board()

## does he have a piece there? OK
## is it his ? OK

##can he move there?
##is that legal?
##what changes on the board becuase of it>?
##
##display



print ("Ok i created the Othello instance")
