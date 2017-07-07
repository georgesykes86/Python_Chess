class Board:
  class Square:
    def __init__(self, grid_pos, colour):
      self.pos_X = grid_pos[0]
      self.pos_Y = grid_pos[1]
      self.colour = colour

  def __init__(self):
    self.grid_letters = ["A","B","C","D","E","F","G","H"]
    self.count = 0
    self.squares = {}
    self.grid_pos =  [None,None]
    self.square_ID = ""

  def createboard(self):
    for i in range(0, 8):
      for j in range(0, 8):
        self.grid_pos[0] = self.grid_letters[i]
        self.grid_pos[1] = (j+1)
        self.square_ID = f"{self.grid_pos[0]}{self.grid_pos[1]}"
        self.count += 1
        if self.count % 2 == 0:
          colour = "black"
        else:
          colour = "white"
        self.squares[self.square_ID] = Board.Square(self.grid_pos, colour)

  def print_board(self):
    for square in self.squares:
      print(square, self.squares[square].pos_X, self.squares[square].pos_Y, self.squares[square].colour)








