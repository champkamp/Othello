from tkinter import *
from tkinter import ttk
import logic
from tkinter import messagebox

class Othello_GUI:
    
    def __init__(self, rows, columns, turn, top_left, game_type):
        self.processor = logic.Logic(rows, columns, turn, top_left, game_type)
        self.game_type = game_type
        self.processor.initialize_board()
        self.processor.update_move_chart()
        self.root = Tk()
        self.move = [0, 0] #Protocol for move (the location of a prospective move): move[index1] where index1 = location (0=row, 1=column)
        self.rows = rows
        self.columns = columns
        self.root.title("Othello")
        self.width=800
        self.height=800
        self.canvas = Canvas(self.root, width=(self.width), height=(self.height))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.canvas.bind("<Configure>", self.resize)
        self.canvas.grid(row=0, column=0, sticky=(N + W + E + S))
        self.build_canvas()
        
    def build_canvas(self):
        self.canvas.config(background='blue')
        self.y_frac = self.height / self.rows
        self.x_frac = self.width / self.columns
        for row in range(self.rows):
            self.canvas.create_line(0, row*self.y_frac, self.columns*self.x_frac, row*self.y_frac)
        for column in range(self.columns):
            self.canvas.create_line(column*self.x_frac, 0, column*self.x_frac, self.rows*self.y_frac)
        for row_number in range(self.rows):
            for column_number in range(self.columns):
                if self.processor.board[row_number][column_number] == "-":
                    self.canvas.create_rectangle((column_number*self.x_frac, row_number*self.y_frac, (column_number+1)*self.x_frac, (row_number+1)*self.y_frac), fill="blue", tags="E")
                elif self.processor.board[row_number][column_number] == "W":
                    self.canvas.create_oval((column_number*self.x_frac, row_number*self.y_frac, (column_number+1)*self.x_frac, (row_number+1)*self.y_frac), fill="white", tags="P")
                elif self.processor.board[row_number][column_number] == "B":
                    self.canvas.create_oval((column_number*self.x_frac, row_number*self.y_frac, (column_number+1)*self.x_frac, (row_number+1)*self.y_frac), fill="black", tags="P")
        self.canvas.tag_bind("E", "<ButtonPress-1>", self.process)
        self.score = Label(self.root, text="White: " + str(self.processor.score[0]) + " --- Black: " + str(self.processor.score[1]) + " ")
        self.show_turn = Label(self.root, text="Turn: " + self.processor.turn)
        self.score.grid(column=0, row=1)
        self.show_turn.grid(column=0, row=2)
        
    def check_game_ending(self):
        return 
            
        
    def resize(self, event):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.rebuild_canvas()
        
    def rebuild_canvas(self):
        self.canvas.delete(ALL)
        self.score.destroy()
        self.show_turn.destroy()
        self.score = Label(self.root, text="White: " + str(self.processor.score[0]) + " --- Black: " + str(self.processor.score[1]) + " ")
        self.show_turn = Label(self.root, text="Turn: " + self.processor.turn)
        self.build_canvas()
    
    def process(self, event):
        for row in range(self.rows):
            if event.y > row*self.y_frac and event.y < (row+1)*self.y_frac:
                self.move[0] = row
        for column in range(self.columns):
            if event.x > column*self.x_frac and event.x < (column+1)*self.x_frac:
                self.move[1] = column
        if self.processor.check_move_possibility(self.move[0], self.move[1]):
            self.processor.make_move(self.move[0], self.move[1])
            if self.processor.remaining_moves():
                self.rebuild_canvas()
                self.end_game()
            else:
                if not self.processor.remaining_moves_color():
                    if self.processor.turn == "W":
                        messagebox.showinfo("Error", "No available moves for White, switching turns")
                    else:
                        messagebox.showinfo("Error", "No available moves for Black, switching turns")
                    self.processor.switch_turn()
            self.rebuild_canvas()
            self.processor.print_board()
                    
                
    def end_game(self):
        message = "Game Over \n"
        score = self.processor.score
        if self.game_type == "1":
            message = message + "Player with most chips wins \n"
            if score[0] > score[1]:
                message = message + "White wins with score of {} \n".format(score[0])
                message = message + "Black loses with score of {}".format(score[1])
            elif score[0] < score[1]:
                message = message + "Black wins with score of {} \n".format(score[1])
                message = message + "White loses with score of {}".format(score[0])
            else:
                message = message + "Draw! Both players ended with as score of {}".format(score[0])
        else:
            message = message + "Player with least chips wins \n"
            if score[0] > score[1]:
                message = message + "Black wins with score of {} \n".format(score[1])
                message = message + "White loses with score of {}".format(score[0])
            elif score[0] < score[1]:
                message = message + "White wins with score of {} \n".format(score[0])
                message = message + "Black loses with score of {}".format(score[1])
            else:
                message = message + "Draw! Both players ended with as score of {}".format(score[0])
        messagebox.showinfo("Game Over", message)
        self.root.destroy()
        
    def game_over(self):
        if self.processor.remaining_moves():
            return True
        return False
    
    def mainloop(self):
        self.root.mainloop()    
