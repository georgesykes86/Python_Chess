from Board import *
from Piece import *

class Game_manager:
  def __init__(self):
    self.board = Board()
    self.board.createboard()
    self.board_manager = {}
    self.move_counter = 0

  def populate_board(self):
    for key in self.board.squares:
      if self.board.squares[key].pos_Y ==1 :
        if self.board.squares[key].pos_X == "A" or self.board.squares[key].pos_X == "H":
          self.board_manager[key] = Castle("black")
        if self.board.squares[key].pos_X == "B" or self.board.squares[key].pos_X == "G":
          self.board_manager[key] = Knight("black")
        if self.board.squares[key].pos_X == "C" or self.board.squares[key].pos_X == "F":
          self.board_manager[key] = Bishop("black")
        if self.board.squares[key].pos_X == "D" :
          self.board_manager[key] = Queen("black")
        if self.board.squares[key].pos_X == "E" :
          self.board_manager[key] = King("black")
      elif self.board.squares[key].pos_Y ==8 :
        if self.board.squares[key].pos_X == "A" or self.board.squares[key].pos_X == "H":
          self.board_manager[key] = Castle("white")
        if self.board.squares[key].pos_X == "B" or self.board.squares[key].pos_X == "F":
          self.board_manager[key] = Knight("white")
        if self.board.squares[key].pos_X == "C" or self.board.squares[key].pos_X == "E":
          self.board_manager[key] = Bishop("white")
        if self.board.squares[key].pos_X == "D" :
          self.board_manager[key] = Queen("white")
        if self.board.squares[key].pos_X == "E" :
          self.board_manager[key] = King("white")
      elif self.board.squares[key].pos_Y ==2 :
        self.board_manager[key] = Pawn("black")
      elif self.board.squares[key].pos_Y ==7 :
        self.board_manager[key] = Pawn("white")
      else:
        pass
  def print_game_board(self):
    for key in self.board_manager:
      print(key, self.board_manager[key].type,self.board_manager[key].colour)

newgame = Game_manager()
newgame.populate_board()
newgame.print_game_board()

