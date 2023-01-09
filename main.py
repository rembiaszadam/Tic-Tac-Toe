from game_board import GameBoard
from game_board import logo
from platform import system as system_name  # Returns the system/OS name
from subprocess import call as system_call  # Execute a shell command


def clear_screen():
    """Clears the terminal screen."""
    # Clear screen command as function of OS. Must launch game in Terminal for this to work.
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    system_call([command])


def play(player, marker):
    """Take player name, and it's marker, show score, show grid
     and ask player to pick a field in the displayed grid"""
    clear_screen()

    show_score()
    board.show_grid()
    player_choice = input(f'{player} you are "{marker}", pick a field: ')

    # Process player's choice to update board and scores.
    board.update_grid(mark=marker, player_choice=player_choice)


def end_of_round(display_message):
    """Display score, display final game board in round
    and pass into display a message based on the result of the round"""
    clear_screen()

    show_score()
    board.show_grid()
    print(display_message)


def show_score():
    """Display round number and score of each player"""
    print(f'Round {game_round}, Score: {player1} {player1_score} : {player2_score} {player2}')


# Initial game setup.
player1_score = 0
player2_score = 0
game_round = 0
game_on = True

clear_screen()
logo()
player1 = input('Player 1 enter your name: ').title()
player2 = input('Player 2 enter your name: ').title()

# Loop each round.
while game_on:
    clear_screen()
    board = GameBoard()
    game_round += 1

    # Loop through each turn.
    while board.game_in_play():
        next_player = board.next_player(game_round)
        if next_player == 1:
            play(player1, 'X')
        elif next_player == 2:
            play(player2, 'O')

    # After game in play becomes false, check who won, process scores and display results.
    result = board.game_result()
    if result == 'X':
        player1_score += 1
        message = f'{player1} won the round.'
        end_of_round(message)
    elif result == 'O':
        player2_score += 1
        message = f'{player2} won the round.'
        end_of_round(message)
    elif result == 'draw':
        message = "It's a draw."
        end_of_round(message)

    # Ask users if they want to continue to next round, otherwise display results and exit game.
    next_round = game_round + 1
    continue_game = input(f"Would you like to continue to round {next_round}?"
                          f" Hit any key for yes or type 'n' to exit the game: ")
    if continue_game == 'n':
        game_on = False

end_of_round('Goodbye')
