import time


def logo():
    """Prints tic-tac-toe logo."""
    print(r"""

     ______   __     ______        ______   ______     ______        ______   ______     ______
    /\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\
    \/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\
       \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\
        \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/

                                __  __           ______           __  __
                               /\_\_\_\         /\  __ \         /\_\_\_\
                               \/_/\_\/_        \ \ \/\ \        \/_/\_\/_
                                 /\_\/\_\        \ \_____\         /\_\/\_\
                                 \/_/\/_/         \/_____/         \/_/\/_/

                                      ______           __  __           ______
                                     /\  __ \         /\_\_\_\         /\  __ \
                                     \ \ \/\ \        \/_/\_\/_        \ \ \/\ \
                                      \ \_____\         /\_\/\_\        \ \_____\
                                       \/_____/         \/_/\/_/         \/_____/

                                            __  __           ______           __  __
                                           /\_\_\_\         /\  __ \         /\_\_\_\
                                           \/_/\_\/_        \ \ \/\ \        \/_/\_\/_
                                             /\_\/\_\        \ \_____\         /\_\/\_\
                                             \/_/\/_/         \/_____/         \/_/\/_/

    """)


class GameBoard:
    """Models tic tac toe game board."""

    def __init__(self):

        # List of all fields in the tic-tac-toe board.
        # The numbers are replaced with markers as game progresses.
        self.grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Dictionary of all possible winning combinations.
        # Key is winning grid pattern as string,
        # if the filed number chosen by player is present in key add 1 to key value.
        self.x_score = {'123': 0, '456': 0, '789': 0, '147': 0, '258': 0, '369': 0, '159': 0, '357': 0}
        self.o_score = {'123': 0, '456': 0, '789': 0, '147': 0, '258': 0, '369': 0, '159': 0, '357': 0}

        # Update grid function assigns win if a marker has a winning combination
        self.x_win = False
        self.o_win = False

    def show_grid(self):
        """Print tic-tac-toe board with values from grid list above."""
        print(f"""
             {self.grid[0]} | {self.grid[1]} | {self.grid[2]}  
             {self.grid[3]} | {self.grid[4]} | {self.grid[5]} 
             {self.grid[6]} | {self.grid[7]} | {self.grid[8]} 
            """)

    def update_grid(self, mark, player_choice):
        """Use player's choice of field number and their marker to update score and game board."""
        # Error handing incase player types a non-integer value.
        try:
            grid_index = int(player_choice) - 1
        except ValueError:
            print('Invalid entry, try again!')
            time.sleep(2)
        else:
            # Check if player's choice is not in grid list.
            if player_choice not in self.grid:
                print('Invalid entry, try again!')
                time.sleep(2)
            else:
                # Update grid list, marker score and check for winning pattern.
                self.grid[grid_index] = mark
                if mark == 'X':
                    for row in self.x_score:
                        if player_choice in row:
                            self.x_score[row] += 1
                            if self.x_score[row] == 3:
                                self.x_win = True
                elif mark == 'O':
                    for row in self.o_score:
                        if player_choice in row:
                            self.o_score[row] += 1
                            if self.o_score[row] == 3:
                                self.o_win = True

    def game_in_play(self):
        """Check if the grid is full or if a player has 3 in a row.
        Returns True or False."""
        # Check for winner.
        if self.x_win or self.o_win:
            return False
        # Check if grid is full
        elif self.grid.count('X') + self.grid.count('O') == 9:
            return False
        else:
            return True

    def next_player(self, round_number):
        """Choose who's go it is based on round number (odd or even) and if
        there are an even amount of X & O marks. Returns player number."""
        x_count = self.grid.count('X')
        o_count = self.grid.count('O')
        if round_number % 2 == 0:
            if x_count == o_count:
                return 2
            else:
                return 1
        else:
            if x_count == o_count:
                return 1
            else:
                return 2

    def game_result(self):
        """Returns the marker with 3 in a row or draw if board is full."""
        if self.x_win:
            return 'X'
        elif self.o_win:
            return 'O'
        else:
            return 'draw'
