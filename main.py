class Player:
    def __init__(self, player_number):
        self.name = ""
        self.symbol = ""
        self.player_number = player_number

    def choose_name(self):
        self.name = input(f"Player {self.player_number} Enter your name: ")

    def choose_symbol(self, used_symbols):
        while True:
            symbol = input(f"{self.name}, choose your symbol (X/O): ").upper()
            if symbol in ['X', 'O'] and symbol not in used_symbols:
                self.symbol = symbol
                used_symbols.add(symbol)
                break
            else:
                print("Invalid or already taken symbol, choose X or O.")


class Menu:
    def display_main_menu(self):
        print("Welcome to Tic-Tac-Toe!")
        print("1. Start Game")
        print("2. Quit")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid input. Please enter '1' to start the game or '2' to quit.")

    def display_end_menu(self):
        print("Game over!")
        print("1. Play Again")
        print("2. Quit")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                return choice
            else:
                print("Invalid input. Please enter '1' to play again or '2' to quit.")


class Board:
    def __init__(self):
        self.board = [str(i+1) for i in range(9)]  # Initialize board with numbers

    def display_board(self):
        print("\n")
        for i in range(3):
            print(f"{self.board[3*i]} | {self.board[3*i+1]} | {self.board[3*i+2]}")
            if i < 2:
                print("--+---+--")
        print("\n")

    def update_board(self, position, symbol):
        self.board[position] = symbol

    def is_valid_move(self, position):
        return self.board[position].isdigit()  # Check if the position is still a number

    def reset_board(self):
        self.board = [str(i+1) for i in range(9)]  # Reset board with numbers


class Game:
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        elif choice == "2":
            self.quit_game()

    def setup_players(self):
        used_symbols = set()
        for player in self.players:
            player.choose_name()
            player.choose_symbol(used_symbols)

    def play_game(self):
        self.board.reset_board()
        while True:
            self.play_turn()
            if self.check_win():
                self.board.display_board()
                print(f"{self.players[self.current_player_index].name} wins!")
                self.restart_game()
                break
            if self.check_draw():
                self.board.display_board()
                print("It's a draw!")
                self.restart_game()
                break
            self.switch_player()

    def restart_game(self):
        choice = self.menu.display_end_menu()
        if choice == "1":
            self.play_game()
        elif choice == "2":
            self.quit_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not pos.isdigit() for pos in self.board.board)  # Draw if no digits left

    def play_turn(self):
        self.board.display_board()
        player = self.players[self.current_player_index]
        while True:
            try:
                position = int(input(f"{player.name} ({player.symbol}), choose your position (1-9): ")) - 1
                if 0 <= position < 9 and self.board.is_valid_move(position):
                    self.board.update_board(position, player.symbol)
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for playing! Goodbye!")
        exit()


if __name__ == "__main__":
    game = Game()
    game.start_game()
