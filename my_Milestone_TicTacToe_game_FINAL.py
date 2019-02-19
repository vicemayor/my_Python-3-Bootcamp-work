#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# use a variable to control gameplay being active
game_active = "y"

# use a while loop to control game repeat
while game_active == "y":
    import time
    import os
    
    os.system('cls')
    
    # create a dictionary to store each board location and the player whose token holds it. Will be used to track changes during gameplay
    board_locs_dict = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

    # create a function to display the current board throughout the game
    def display_game_board():
        print(f"{board_locs_dict[1]} | {board_locs_dict[2]} | {board_locs_dict[3]}")
        print("\n--|---|--")
        print(f"{board_locs_dict[4]} | {board_locs_dict[5]} | {board_locs_dict[6]}")
        print("\n--|---|--")
        print(f"{board_locs_dict[7]} | {board_locs_dict[8]} | {board_locs_dict[9]}")

    # begin gameplay here
    print("Welcome to Tic-Tac-Toe! Let's begin!")
    time.sleep(2)
    print("\nIn this game, your moves will be recorded on a game board looking like the one below.\n")
    display_game_board()
    time.sleep(4)
    print("""\nThe spots are numbered in the order that you'll eventually use to select them during gameplay. But before we begin,
we'll need a little bit more information...\n""")

    # collect players names and assign player tokens below
    p1_token = None
    p2_token = None

    p1_name = str(input("Player 1 - what is your name?: "))

    # request token selection from player 1 - force to 'x' or 'o'
    p1_token = str(input("Great! And will you be playing as x or o?")).lower()
    while p1_token not in ['x','o']:
        p1_token = str(input(f"{p1_name}, please select 'x' or 'o'")).lower()

    print(f"\nThanks {p1_name}!")
    print("\n")
    time.sleep(2)

    p2_name = str(input("Player 2 - what is your name?: "))
    # set player 2 token equal to the opposite of player 1
    if p1_token == 'x':
        p2_token = 'o'
    else:
        p2_token = 'x'

    print(f"\nThanks {p2_name}!")

    # create a dictionary consisting of player identifiers as keys, name and token as values to use in later references
    player_dict = {"p1":[p1_name,p1_token],"p2":[p2_name,p2_token]}

    time.sleep(2)
    print("\n\nOkay, so {0[0]} will be player one and use {0[1]}, and {1[0]} will be player two, using {1[1]}. Let's begin!\n".format(player_dict["p1"],player_dict["p2"]))
    time.sleep(4)
    #####
    # create a function to identify the potential winning conditions. In this case that should mean that either a full row, a full
    # column, or a diagonal of three all share the same token. We'll refer to locations in the "board_locs_dict" to check for a win
    #####

    def check_for_win():
        row_cond = None
        col_cond = None
        diag_cond = None

        for x in [1,4,7]:
            if board_locs_dict[x] == board_locs_dict[x+1] == board_locs_dict[x+2]:
                row_cond = True
                break
        for x in [1,2,3]:
            if board_locs_dict[x] == board_locs_dict[x+3] == board_locs_dict[x+6]:
                col_cond = True
                break
        for x in [1,3]:
            if x == 1:
                if board_locs_dict[x] == board_locs_dict[x+4] == board_locs_dict[x+8]:
                    diag_cond = True
                    break
            if x == 3:
                if board_locs_dict[x] == board_locs_dict[x+2] == board_locs_dict[x+4]:
                    diag_cond = True
                    break

        return row_cond or col_cond or diag_cond

    # create a list to keep track of eligible selections from the board during gameplay and count of turns
    board_tracking_list = [key for key in board_locs_dict.keys()]
    
    # create a function to request a selection from the player
    def request_p_choice():
        choice = int(input(f"{cur_player[0]} - please choose an available numbered location from the board: "))
        while choice not in board_tracking_list:
            choice = int(input(f"That is not a valid selection. Please try again: "))
        return choice

    #####
    # CREATE AND EXECUTE THE CORE GAMEPLAY LOOP 
    #####

    # create a variable that will be used to alternate between players. Start at player 1
    cur_player = player_dict["p1"]
    
    os.system('cls')
    
    # begin a while loop referring to the length of the board tracking list. Each turn will remove an element from the list, so
    # the loop will end when all selections have been exhausted
    while len(board_tracking_list) > 0:
        display_game_board()
        print("\n")
        p_choice = request_p_choice()
        board_locs_dict[p_choice] = cur_player[1]
        board_tracking_list.pop(board_tracking_list.index(p_choice))
        if check_for_win() is True:
            os.system('cls')
            time.sleep(1)
            print("\nWe have a winner!\n")
            time.sleep(1)
            display_game_board()
            time.sleep(1)
            print(f"\nCongratulations {cur_player[0]}, you have won the game!")
            break
        else:
            if cur_player == player_dict["p1"]:
                cur_player = player_dict["p2"]
            else:
                cur_player = player_dict["p1"]
        time.sleep(1)
        os.system('cls')

    time.sleep(3)

    if len(board_tracking_list) == 0:
        print("\nLooks like we did not end up with a winner. Thanks for playing!")
    else:
        print("\nThanks for playing!\n")
    
    time.sleep(2)
    game_replay = str(input("Would you like to play again? Y or N: ")).lower()
    while game_replay not in ['y','n']:
        game_replay = str(input("Not a valid response - please enter Y or N: "))
    game_active = game_replay
    print("\n")

time.sleep(2)

print("\nOkay, later on!")

time.sleep(4)