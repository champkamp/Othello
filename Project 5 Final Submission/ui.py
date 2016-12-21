#Nicholas Imkamp 62086284

from tkinter import *
from tkinter import ttk
import ui_board

#UI Main

def run_gui():
    
    #Mainframe
    mainframe = ttk.Frame(root, padding="10 10")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
    #Callable Functions
    def start_game():
        '''Reads the values of the initial GUI and loads them into the logic processor, acts as mainframe function'''
        start_color = str(STARTING_COLOR.get())
        top_left = str(TOP_LEFT_COLOR.get())
        game_type = str(GAME_TYPE.get())
        if start_color == "White":
            color = "W"
        else:
            color = "B"
        if top_left == 'White':
            tl = 'W'
        else:
            tl = 'B'
        if game_type == 'More Pieces Wins':
            gt = '1'
        else:
            gt = '2'
        gui = ui_board.Othello_GUI(int(ROWS.get()), int(COLUMNS.get()), color, tl, gt)
        gui.mainloop()
            
    
    #Variable Definitions
    ROWS = StringVar()
    COLUMNS = StringVar()
    STARTING_COLOR = StringVar()
    TOP_LEFT_COLOR = StringVar()
    GAME_TYPE = StringVar()
    
    #Input Widgets
    
    #Dropdown Widgets
    ttk.OptionMenu(mainframe, ROWS, '4','4','6','8','10','12','14','16').grid(column=2, row=2, sticky=W)
    ttk.OptionMenu(mainframe, COLUMNS, '4','4','6','8','10','12','14','16').grid(column=4, row=2, sticky=W)
    ttk.OptionMenu(mainframe, STARTING_COLOR, 'White', 'White', 'Black').grid(column=2, row=3, sticky=W)
    ttk.OptionMenu(mainframe, TOP_LEFT_COLOR, 'White', 'White', 'Black').grid(column=4, row=3, sticky=W)
    ttk.OptionMenu(mainframe, GAME_TYPE, 'More Pieces Wins', 'More Pieces Wins', 'Less Pieces Wins').grid(column=3, row=4, sticky=W)
    
    #Label Widgets
    ttk.Label(mainframe, text="Initial Values:").grid(column=1, columnspan=4, row=1, sticky=W)
    ttk.Label(mainframe, text="Rows:").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="Columns:").grid(column=3, row=2, sticky=W)
    ttk.Label(mainframe, text="Starting Color:").grid(column=1, row=3, sticky=W)
    ttk.Label(mainframe, text="Top Left Color:").grid(column=3, row=3, sticky=W)
    ttk.Label(mainframe, text="How will the game be played?").grid(column=1, row=4, columnspan=2, sticky=W)
    
    #Buttons
    ttk.Button(mainframe, text="New Game", command=start_game).grid(column=4, row=5, sticky=E)

if __name__ == "__main__":
    root = Tk()
    root.title("Othello")
    run_gui()
    root.mainloop()
