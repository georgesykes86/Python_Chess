class Piece:
  def __init__(self, type, colour):
    self.type = type
    self.colour = colour

class Pawn(Piece):
  def __init__(self, colour):
    self.moves = [1,0]
    Piece.__init__(self,"pawn", colour)

class Queen(Piece):
  def __init__(self, colour):
    self.moves = [[1,0], [2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-1,0], [-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
    Piece.__init__(self, "queen", colour)

class King(Piece):
  def __init__(self, colour):
    self.moves = [[1,0], [0,1],[1,1],[-1,1],[-1,0],[0,-1],[-1,-1],[1,-1]]
    Piece.__init__(self, "king", colour)

class Castle(Piece):
  def __init__(self, colour):
    self.moves = [[1,0], [2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[-1,0], [-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7]]
    Piece.__init__(self, "castle", colour)

class Knight(Piece):
  def __init__(self, colour):
    self.moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    Piece.__init__(self, "knight", colour)

class Bishop(Piece):
  def __init__(self, colour):
    self.moves = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7]]
    Piece.__init__(self, "bishop", colour)

