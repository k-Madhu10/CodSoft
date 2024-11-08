import random

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = PLAYER_X

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_winner(self, player):
        
        for row in self.board:
            if all(s == player for s in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != EMPTY for row in self.board for cell in row)

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == EMPTY]

    def make_move(self, row, col, player):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player
            return True
        return False

    def minimax(self, depth, is_maximizing):
        if self.is_winner(PLAYER_O):
            return 1 
        if self.is_winner(PLAYER_X):
            return -1  
        if self.is_draw():
            return 0  

        if is_maximizing:
            best_score = float('-inf')
            for row, col in self.available_moves():
                self.make_move(row, col, PLAYER_O)
                score = self.minimax(depth + 1, False)
                self.board[row][col] = EMPTY  
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row, col in self.available_moves():
                self.make_move(row, col, PLAYER_X)
                score = self.minimax(depth + 1, True)
                self.board[row][col] = EMPTY  
                best_score = min(best_score, score)
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = None
        for row, col in self.available_moves():
            self.make_move(row, col, PLAYER_O)
            score = self.minimax(0, False)
            self.board[row][col] = EMPTY  
            if score > best_score:
                best_score = score
                move = (row, col)
        return move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == PLAYER_X:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if not self.make_move(row, col, PLAYER_X):
                    print("Invalid move. Try again.")
                    continue
            else:
                print("AI is making a move...")
                row, col = self.best_move()
                self.make_move(row, col, PLAYER_O)

            if self.is_winner(self.current_player):
                self.print_board()
                if self.current_player == PLAYER_X:
                    print("You win!")
                else:
                    print("AI wins!")
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = PLAYER_X if self.current_player == PLAYER_O else PLAYER_O


if __name__ == "__main__":
    game = TicTacToe()
    game.play()