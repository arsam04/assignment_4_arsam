import tkinter as tk

gui_dim = (1102, 568)
level_caption = ('Entry', 'Level 1', 'Level 2', 'Level 3', 'Finished')
state_caption = ('undiscovered', 'discovered', 'solved', 'failed')
directions = ('n', 's', 'w', 'e', 'north', 'south', 'west', 'east', '1', '2', '3', '4')
question_answer = ('y', 'n', 'yes', 'no')
board_cells_caption = ("-2 , 2", "-1 , 2", "0 , 2", "1 , 2", "2 , 2", "-2 , 1", "-1 , 1", "0 , 1", "1 , 1", "2 , 1",
                       "-2 , 0", "-1 , 0", "0 , 0", "1 , 0", "2 , 0", "-2 , -1", "-1 , -1", "0 , -1", "1 , -1",
                       "2 , -1",
                       "-2 , -2", "-1 , -2", "0 , -2", "1 , -2", "2 , -2")
challenge_question = ((
                          "What color is the sky on a clear day?",
                          'What is the name of the capital city of France?',
                          'What is the smallest continent in the world?',
                          'What is the name of the biggest planet in our solar system?',
                          'What is the largest animal on earth?',
                          'How many sides does a triangle have?',
                          'Who wrote the Harry Potter book series?',
                          "What is the name of the world's tallest mountain?",
                          'How many legs does a spider have?',
                          'What is the name of the largest desert in the world?',
                          "What is the name of the world's largest ocean?",
                          'What is the chemical symbol for water?',
                          'base cell',
                          'What is the capital city of the United States?',
                          'How many planets are in our solar system?',
                          'Who painted the famous artwork "Mona Lisa"?',
                          'What is the name of the smallest planet in our solar system?',
                          'How many hours are in a day?',
                          'What is the name of the closest star to Earth?',
                          'How many continents are there in the world?',
                          'What is the name of the largest country in the world by land area?',
                          'Who invented the telephone?',
                          'What is the name of the highest waterfall in the world?',
                          'What color is a banana?',
                          'Who is the current president of the United States?'),
                      ('What is the name of the biggest ocean in the world?',
                       'What is the capital of Spain?',
                       'How many days are in a week?',
                       'What is the name of the currency used in Japan?',
                       'What is the name of the smallest planet in our solar system?',
                       'Who is the author of "To Kill a Mockingbird"?',
                       'What is the name of the largest country in South America?',
                       'What is the name of the river that runs through Egypt?',
                       'Who invented the light bulb?',
                       'What is the name of the smallest continent in the world?',
                       'What is the capital of Italy?',
                       'What is the name of the biggest animal in the world?',
                       'base cell',
                       'What is the chemical symbol for gold?',
                       'Who is the founder of Microsoft?',
                       'What is the name of the process by which plants make their own food?',
                       'What is the name of the highest mountain in Africa?',
                       'Who was the first person to step on the moon?',
                       'What is the name of the highest mountain in North America?',
                       'What is the name of the largest desert in the world?',
                       'What is the name of the smallest state in the United States?',
                       'What is the name of the country that is also a continent?',
                       'Who painted the famous artwork "The Starry Night"?',
                       "What is the name of the bird that can't fly?",
                       'What is the name of the largest state in the United States by land area?'),
                      ('What is the name of the largest city in the world by population?',
                       "What is the name of the world's largest reef system?",
                       'What is the name of the smallest ocean in the world?',
                       'Who is the creator of Facebook?',
                       'What is the name of the process by which water turns into vapor?',
                       'What is the name of the largest animal on land?',
                       'What is the name of the currency used in the United Kingdom?',
                       'Who is the creator of Apple Inc.?',
                       'What is the name of the smallest bone in the human body?',
                       'What is the name of the largest lake in Africa?',
                       'What is the name of the largest country in the world by land area?',
                       'What is the name of the instrument used to measure air pressure?',
                       'base cell',
                       'Who is the author of the "Harry Potter" series?',
                       'What is the name of the bird that is known for its long neck?',
                       'What is the name of the largest country in South Asia?',
                       'What is the name of the second largest continent in the world?',
                       'What is the name of the planet known as the "Red Planet"?',
                       'What is the name of the largest moon in our solar system?',
                       'What is the name of the largest waterfall in the United States?',
                       'What is the name of the metal that is liquid at room temperature?',
                       'Who is the founder of Amazon?',
                       'What is the name of the smallest particle of an element that retains its chemical properties?',
                       'What is the name of the largest peninsula in the world?',
                       'What is the name of the unit used to measure energy?'))
challenge_results = ((
                         'blue',
                         'paris',
                         'australia',
                         'jupiter',
                         'blue whale',
                         'three',
                         'J.K. rowling',
                         'mount everest',
                         'eight',
                         'sahara',
                         'pacific',
                         'h2O',
                         'base cell',
                         'washington D.C',
                         'eight',
                         'leonardo da vinci',
                         'mercury',
                         '24',
                         'proxima centauri',
                         'seven',
                         'russia',
                         'alexander graham bell',
                         'angel falls',
                         'yellow',
                         'joe biden'), (
                         'pacific ocean',
                         'madrid',
                         'seven',
                         'yen',
                         'mercury',
                         'harper Lee',
                         'brazil',
                         'nile',
                         'thomas edison',
                         'australia',
                         'rome',
                         'blue whale',
                         'base cell',
                         'au',
                         'bill gates',
                         'photosynthesis',
                         'mount kilimanjaro',
                         'neil armstrong',
                         'denali',
                         'sahara',
                         'rhode island',
                         'australia',
                         'vincent van gogh',
                         'penguin',
                         'alaska'), (
                         'tokyo',
                         'great barrier reef',
                         'arctic ocean',
                         'mark zuckerberg',
                         'evaporation',
                         'african elephant',
                         'pound sterling',
                         'steve jobs',
                         'stapes',
                         'lake victoria',
                         'russia',
                         'barometer',
                         'base cell',
                         'J.K. rowling',
                         'giraffe',
                         'india',
                         'africa',
                         'mars',
                         'ganymede',
                         'niagara falls',
                         'mercury',
                         'jeff bezos',
                         'atom',
                         'arabian peninsula',
                         'joule'))


def initial_player():
    """
    Initialize a new player with default attributes.

    This function creates a new player with default attributes, including an empty name, a level of 0,
    full health, starting position at cell 12, no solved cells, and not doing any challenge.


    :precondition: None.
    :post condition: A dictionary representing a new player with default attributes is returned.
    :return: A dictionary representing the new player with default attributes.
    :raises: None.
    """
    game_player = {
        "name": "",
        "level": 0,
        "health": 3,
        "current_position": 12,
        "solved_cells": 0,
        "doing_challenge": False
    }
    return game_player


def initial_board():
    """
    Initialize a new board with default attributes.

    This function creates a new game board with default attributes, including the level set to 0,
    and each of the 25 cells initialized to the first state caption.

    :precondition: None.
    :post condition: A dictionary representing a new game board with default attributes is returned.
    :return: A dictionary representing the new game board with default attributes.
    :raises: None.
    """
    game_board = {
        "level": 0
    }
    for cell_counter in range(0, 25):
        game_board.update({str(cell_counter): state_caption[0]})

    return game_board


def can_move(direction, position):
    """
    Check if a move is valid.

    This function takes in a direction and a current position, and returns True if the move is valid,
    or False if it is not. The move is considered valid if it does not take the player off the board.

    :param direction: A string indicating the direction of the move. Valid directions are "n", "north", "1",
    "s", "south", "3", "e", "east", "2", "w", "west", "4".
    :param position: An integer indicating the current position of the player on the board. Position values
    range from 0 to 24, where 0 is the top-left cell and 24 is the bottom-right cell.
    :precondition: The direction parameter must be a string, and the position parameter must be an integer.
    The position parameter must be between 0 and 24 inclusive.
    :post condition The function returns a boolean value indicating whether the move is valid or not.
    :return: True if the move is valid, False otherwise.
    :raises: None.
    """
    result = True
    if (direction in {"n", "north", "1"}) and position < 5:
        result = False
    elif (direction in {"s", "south", "3"}) and position > 20:
        result = False
    elif (direction in {"e", "east", "2"}) and (position in {4, 9, 14, 19, 24}):
        result = False
    elif (direction in {"w", "west", "4"}) and (position in {0, 5, 10, 15, 20}):
        result = False
    return result


def do_command(command, game_player, game_board):
    """
    Process a command given by the user and update the game state accordingly.

    :param command: str, the command given by the user
    :param game_player: dict, containing the game's player information
    :param game_board: dict, containing the game's board information
    :precondition: game_player and game_board should be dictionaries with specific keys and values
    :post condition: The game state will be updated according to the given command
    :return: dict, containing the updated game state
    :raises ValueError: if the player tries to move to an invalid cell
    """
    result = {
        "succeed": False,
        "caption": "",
        "player": game_player,
        "board": game_board
    }
    if result["player"]["doing_challenge"]:
        result["succeed"] = True
        print(command)
        print(result["player"]["level"])
        print(result["player"]["current_position"])
        print(challenge_results[result["player"]["level"] - 1][result["player"]["current_position"]])
        if command.lower() == challenge_results[result["player"]["level"] - 1][result["player"]["current_position"]]:
            result["board"][str(result["player"]["current_position"])] = state_caption[2]
            result["player"]["solved_cells"] += 1
            result[
                "caption"] = "You won this challenge\nCommands:\n   1. N : go North\n   2. E : go East\n " \
                             "  3. S : go south\n   4. W : go West"
            result["player"]["doing_challenge"] = False
        else:
            result["board"][str(result["player"]["current_position"])] = state_caption[3]
            result["player"]["health"] -= 1
            result[
                "caption"] = "You lost this challenge\nCommands:\n   1. N : go North\n   2. E : go East\n " \
                             "  3. S : go south\n   4. W : go West\n   5. C : do Challenge"
            result["player"]["doing_challenge"] = False
        return result
    if result["player"]["level"] == 0:
        if len(command) <= 2:
            result["succeed"] = False
            result["caption"] = "  your name is too short.\n  select another name ! ! "
        else:
            result["succeed"] = True
            result["caption"] = f"hi {command}\nWelcome !!\nType H or h to get game commands"
            result["player"] = {
                "name": command,
                "level": 1,
                "health": 3,
                "current_position": 12,
                "solved_cells": 0,
                "doing_challenge": False
            }
            result["board"]["level"] = 1
            for cell_counter in range(0, 25):
                result["board"].update({str(cell_counter): state_caption[0]})
            result["board"]["12"] = state_caption[1]
    elif command.lower() == "h" or command.lower() == "help" or command.lower() == "?":
        result["succeed"] = True
        result["caption"] = "Commands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West"
        if result["player"]["current_position"] != 12:
            if result["board"][str(result["player"]["current_position"])] in (state_caption[1], state_caption[3]):
                result["caption"] = f"{result['caption']}\n   5. C : do Challenge"
    elif command.lower() in directions:
        result["succeed"] = True
        if can_move(command.lower(), result["player"]["current_position"]):
            result[
                "caption"] = "You moved\nCommands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n  " \
                             " 4. W : go West"
            if command.lower() in {"n", "north", "1"}:
                result["player"]["current_position"] -= 5
            elif command.lower() in {"s", "south", "3"}:
                result["player"]["current_position"] += 5
            elif command.lower() in {"e", "east", "2"}:
                result["player"]["current_position"] += 1
            elif command.lower() in {"w", "west", "4"}:
                result["player"]["current_position"] -= 1
            if result["board"][str(result["player"]["current_position"])] == state_caption[0]:
                result["board"][str(result["player"]["current_position"])] = state_caption[1]
        else:
            result[
                "caption"] = "You can't move\nCommands:\n   1. N : go North\n   2. E : go East\n  " \
                             " 3. S : go south\n   4. W : go West"
        if result["player"]["current_position"] != 12:
            if result["board"][str(result["player"]["current_position"])] in (state_caption[1], state_caption[3]):
                result["caption"] = f"{result['caption']}\n   5. C : do Challenge"
    elif command.lower() == result["player"]["name"].lower():
        result["succeed"] = True
        result["caption"] = f"hi, I know you {result['player']['name']}\nType H or h to get game commands\n"
    else:
        result["succeed"] = True
        result["caption"] = "Type H or h to get game commands\n"
    return result


def game_gui():
    """
    Display and manages the game GUI.

    The function consists of several helper functions. The game board and player status are displayed as Tkinter
    widgets. The board cells are colored according to their status. The player can interact with the game board by
    clicking the cells.

    :precondition: None
    :post condition: The game GUI is displayed and managed by the user.
    :return: None
    :raises: None
    """
    def write_to_text(text_var, text_caption, insert_index, delete_bindex, delete_eindex):
        """
        Write text to a Text widget, optionally deleting a range of characters first.

        :param text_var: tkinter Text widget to modify
        :param text_caption: string to insert into text_var
        :param insert_index: string representing the location to insert text_caption into text_var
        :param delete_bindex: string representing the beginning index of the text to delete from text_var (if any)
        :param delete_eindex: string representing the ending index of the text to delete from text_var (if any)
        :precondition: `text_var` is a valid tkinter Text widget object. `insert_index`, `delete_bindex`, and
        `delete_eindex` are valid index strings for the Text widget.
        :post condition: The specified text has been written to the Text widget. If applicable, the range of characters
        between `delete_bindex` and `delete_eindex` has been deleted.
        :return: None.
        :raises: None.
        """
        text_var.config(state="normal")
        if delete_bindex != "-1.-1":
            text_var.delete(delete_bindex, delete_eindex)
        if insert_index != "-1.-1":
            text_var.insert(insert_index, text_caption)
        text_var.config(state="disabled")

    def draw_board_cells(game_player, game_board):
        """
        Draw the cells of the game board with the corresponding state colors based on the game state.

        :param game_player: A dictionary that represents the current state of the game player.
        :param game_board: A dictionary that represents the current state of the game board.
        :precondition: The `game_player` and `game_board` parameters must be dictionaries containing the current state
        of
        the game player and game board, respectively.
        :post condition: The cells of the game board are drawn with the corresponding state colors based on the game
        state.
        :return: None.
        :raises: None.
        """
        for cell_counter in range(0, 25):
            label_board_cells[cell_counter].config(background="light grey")
            if game_board[str(cell_counter)] == state_caption[0]:
                label_board_cells[cell_counter].config(foreground="lightgrey")
            elif game_board[str(cell_counter)] == state_caption[1]:
                label_board_cells[cell_counter].config(foreground="black")
            elif game_board[str(cell_counter)] == state_caption[2]:
                label_board_cells[cell_counter].config(foreground="green")
            elif game_board[str(cell_counter)] == state_caption[3]:
                label_board_cells[cell_counter].config(foreground="red")
        label_board_cells[game_player["current_position"]].config(background="light green")

    def show_status(game_player, game_board):
        """
        Display the player's status and draw the game board cells.

        :param game_player: A dictionary containing the player's information.
        :param game_board: A dictionary containing the game board information.
        :precondition: game_player and game_board are valid dictionaries.
        :postcondition: The player's status is displayed and the game board cells are drawn accordingly.
        :return: None
        :raises: None
        """
        write_to_text(text_status, f"{game_player['name']}\n---------------------------", tk.INSERT, "1.0", tk.END)
        write_to_text(text_status, f"\nCurrent level : {level_caption[game_player['level']]}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nYour position : {board_cells_caption[game_player['current_position']]}",
                      tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nHealth : {game_player['health']}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nSolved : {game_player['solved_cells']}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nFailed : {3 - game_player['health']}", tk.INSERT, "-1.-1", "")
        draw_board_cells(game_player, game_board)

    def initial_gui():
        """
        Initializes the GUI with default settings.

        :precondition: None
        :post condition: The GUI is displayed with default settings
        :return: None
        :raises: none
        """
        label_board_cells[12].config(background="light green")

        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->\n\nenter your name:", tk.INSERT, "1.0",
                      tk.END)

        write_to_text(text_status, "", "-1.-1", "1.0", tk.END)

        entry_command.delete("0", tk.END)

    def show_challenge(position, level):
        """
        Display the challenge at the given position for the given level in the text_room_space widget.

        :param position: an integer representing the position of the challenge within the level
        :param level: an integer representing the level of the challenge
        :precondition: `position` and `level` are valid indices for the `challenge_question` list
        :postcondition: the challenge is displayed in the `text_room_space` widget
        :return: None
        :raises: None
        """
        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->", tk.INSERT, "1.0", tk.END)
        write_to_text(text_room_space, f"\nLevel : {level} - Challenge No : {position}", tk.INSERT, "-1.-1", "")
        write_to_text(text_room_space, f"\n{challenge_question[level - 1][position]}", tk.INSERT, "-1.-1", "")

    def play_game(event):
        """
        Play the game based on user input.

        This function takes the user input from the game window and processes it. It updates the player and board
        based on the user's input and displays the appropriate message to the user. If the game is over or the user
        has won, the function prompts the user to play again or quit the game.

        :param event: The event object for the user input.
        :precondition: event must be a valid event object.
        :post condition: The game will be played based on user input, and the appropriate messages will be displayed.
        :return: None.
        :raises: None.
        """
        if event.char == "\r":
            nonlocal player, board
            if player["health"] <= 0 or player["solved_cells"] > 23:
                if entry_command.get() in question_answer:
                    if entry_command.get() in ('y', 'yes'):
                        swap_level = 1
                        swap_health = 3
                        if player["solved_cells"] > 23 and player["level"] < 4:
                            swap_level = player["level"]
                            swap_health = player["health"]
                        player = initial_player()
                        board = initial_board()
                        player["level"] = swap_level
                        board["level"] = swap_level
                        player["health"] = swap_health
                        board["12"] = state_caption[1]
                    else:
                        game_windows.destroy()
                        return
                else:
                    entry_command.delete(0, tk.END)
                    return
            if (entry_command.get() in {"c", "5"}) and (not player["doing_challenge"]):
                if player["current_position"] != 12 and board[str(player["current_position"])] != state_caption[2]:
                    player["doing_challenge"] = True
                    show_challenge(player["current_position"], player["level"])
                    entry_command.delete(0, tk.END)
                    return
            command_result = do_command(entry_command.get(), player, board)
            entry_command.delete(0, tk.END)
            write_to_text(text_room_space, "<----   PUZZLE LAND   ---->", tk.INSERT, "1.0", tk.END)
            write_to_text(text_room_space, f"\n{command_result['caption']}", tk.INSERT, "-1.-1", "")
            if command_result["succeed"]:
                player = command_result["player"]
                board = command_result["board"]
                show_status(player, board)
                if player["health"] <= 0:
                    write_to_text(text_room_space, "<----   PUZZLE LAND   ---->", tk.INSERT, "1.0", tk.END)
                    write_to_text(text_room_space, "\n<><> GAME OVER <><>\nDo you want to play again ? (y/n)",
                                  tk.INSERT, "-1.-1", "")
                elif player["solved_cells"] > 23:
                    if player["level"] == 3:
                        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->", tk.INSERT, "1.0", tk.END)
                        write_to_text(text_room_space, "\n<><> YOU WIN <><>\nDo you want to play again ? (y/n)",
                                      tk.INSERT, "-1.-1", "")
                    else:
                        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->", tk.INSERT, "1.0", tk.END)
                        write_to_text(text_room_space,
                                      "\n/\\__/\\/\\ Level up /\\/\\__/\\\nDo you want to continue ? (y/n)", tk.INSERT,
                                      "-1.-1", "")
                    player["level"] += 1
            else:
                write_to_text(text_room_space, "\nPlease enter your name:", tk.INSERT, "-1.-1", "")

    def make_gui(dims):
        """
        Create a GUI window with given dimensions.

        :param dims: a tuple containing the width and height of the GUI window
        :precondition: dims must be a tuple containing two positive integers
        :post condition: a GUI window will be created with the specified dimensions
        :return: a tkinter object representing the created GUI window
        :raises TypeError and ValueError: TypeError if dims is not a tuple or contains non-integer values,
        ValueError if dims contains non-positive integers
        """
        gui_windows = tk.Tk()
        screen_width = gui_windows.winfo_screenwidth()
        screen_height = gui_windows.winfo_screenheight()
        position_right = int(screen_width / 2 - dims[0] / 2)
        position_top = int(screen_height / 2 - dims[1] / 2)
        gui_windows.resizable(width=False, height=False)
        gui_windows.geometry(f'{dims[0]}x{dims[1]}+{position_right}+{position_top}')
        gui_windows.title("this da game panel")

        gui_windows.rowconfigure(0, weight=3)
        gui_windows.rowconfigure(1, weight=3)
        gui_windows.rowconfigure(2, weight=4)
        gui_windows.rowconfigure(3, weight=2)
        gui_windows.rowconfigure(4, weight=1)
        gui_windows.columnconfigure(0, weight=1)
        gui_windows.columnconfigure(1, weight=20)
        gui_windows.columnconfigure(2, weight=1)

        return gui_windows

    game_windows = make_gui(gui_dim)
    label_board_cells = []

    text_room_space = tk.Text(game_windows, font=('helvetica', 25, 'bold'), width=44, height=13, foreground="yellow",
                              background="blue")
    text_status = tk.Text(game_windows, font=('helvetica', 20, 'normal'), width=10, height=7, foreground="orange",
                          background="black")
    label_command = tk.Label(game_windows, text="Command line :", width=12, font=('helvetica', 12, 'bold'))
    entry_command = tk.Entry(game_windows, font=('helvetica', 17, 'normal'), foreground="white", background="black")
    frm_map = tk.Frame(game_windows, relief=tk.FLAT, bd=1)
    for row_counter in range(0, 5):
        for col_counter in range(0, 5):
            label_board_cells.append(
                tk.Label(frm_map, text=board_cells_caption[row_counter * 5 + col_counter], height=3, width=7,
                         background="light grey"))
            label_board_cells[row_counter * 5 + col_counter].grid(row=row_counter, column=col_counter, sticky="nsew",
                                                                  padx=1, pady=1)
    btn_exit = tk.Button(game_windows, text="Exit", font=('Times New Roman', 17, 'bold'), command=game_windows.destroy)

    text_room_space.grid(row=0, column=0, sticky="nsew", rowspan=4, columnspan=2, padx=5, pady=5)
    frm_map.grid(row=0, column=2, sticky="nsew", rowspan=2, padx=5, pady=5)
    text_status.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
    label_command.grid(row=4, column=0, padx=5, pady=5)
    entry_command.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
    btn_exit.grid(row=4, column=2, sticky="ewns", padx=5, pady=5)

    initial_gui()

    player = initial_player()
    board = initial_board()

    game_windows.bind("<Key>", play_game)

    game_windows.mainloop()
