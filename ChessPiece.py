

class ChessPiece:

    selected = False
    is_king = False

    def __init__(self, x, y, is_red):
        self.x = x
        self.y = y
        self.is_red = is_red

    def get_move_locs(self, board):
        moves = []
        for x in xrange(9):
            for y in xrange(10):
                if (x,y) in board.pieces and board.pieces[x,y].is_red == self.is_red:
                    continue
                if self.can_move(board, x-self.x, y-self.y):
                    moves.append((x,y))
        return moves

    def move(self, board, dx, dy, is_calc=False):
        nx, ny = self.x + dx, self.y + dy
        if (nx, ny) in board.pieces:
            board.remove(nx, ny)
        board.remove(self.x, self.y)
        if not is_calc:
            print('Move %s from (%d,%d) to (%d,%d)' % (self.name, self.x, self.y, self.x+dx, self.y+dy))
        self.x += dx
        self.y += dy
        board.pieces[self.x, self.y] = self
        return True

    def count_pieces(self, board, x, y, dx, dy):
        sx = dx/abs(dx) if dx!=0 else 0
        sy = dy/abs(dy) if dy!=0 else 0
        nx, ny = x + dx, y + dy
        x, y = x + sx, y + sy
        cnt = 0
        while x != nx or y != ny:
            if (x, y) in board.pieces:
                cnt += 1
            x += sx
            y += sy
        return cnt

    # below added by Fei Li
    def get_moves_slow(self, board):
        moves = []
        for x in xrange(9):
            for y in xrange(10):
                if (x,y) in board.pieces and board.pieces[x,y].is_red == self.is_red:
                    continue
                if self.can_move(board, x-self.x, y-self.y):
                    moves.append((self.x, self.y, x-self.x, y-self.y))
        return moves
