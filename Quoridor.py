# CS 162
# Aaron Wheaton
# 8/6/2021
# This is a python replication of the game Quoridor

class QuoridorGame:
    """This is the main class for the Quoridor Game"""

    def __init__(self):
        """Define the initial conditions for the game"""
        # Initialize the first turn belonging to player one
        self._current_turn = 1
        # Initialize the lists of vertical and horizontal fences
        self._v_list = []
        self._h_list = []
        # Initialize the fences "off the board" aka the ones in each players inventory
        self._p1_fence_count = 8
        self._p2_fence_count = 8
        # Initialize the pieces to their proper spots
        self._p1 = (4, 0)
        self._p2 = (4, 8)
        # Initialize the individual coordinates of the pieces to allow further analysis of moves, etc.
        self._p1_x_coord = (self._p1[0])
        self._p1_y_coord = (self._p1[1])
        self._p2_x_coord = (self._p2[0])
        self._p2_y_coord = (self._p2[1])
        # Add the "exterior fences" aka the limits of the game board by iterating 0 to 8 on the horizontal and
        # vertical edges and adding those to the fence lists
        for i in range(0, 8):
            self._v_list.append((0, i))
            self._v_list.append((8, i))
            self._h_list.append((i, 0))
            self._h_list.append((i, 8))


        # Define getters and setters for various private data classes associated with the QuoridorGame class
    def get_p1(self):
        """Returns p1 position"""
        return self._p1

    def get_p2(self):
        """Returns p2 position"""
        return self._p2

    def get_v_list(self):
        """Returns list of vertical fences"""
        return self._v_list

    def get_h_list(self):
        """Returns list of horizontal fences"""
        return self._h_list

    def set_p1(self, p1_pos):
        """Sets the position of p1"""
        self._p1 = p1_pos

    def set_p2(self, p2_pos):
        """Sets the position of p2"""
        self._p2 = p2_pos

    def turn_check(self, player_turn):
        """Checks to make sure the player isn't playing out of turn"""
        if player_turn != self._current_turn:
            return False
        else:
            return True

    def on_top_check(self, coord):
        """Checks to make sure the player isn't attempting to place something directly on top of another"""
        if coord == self._p1 or coord == self._p2:
            return False
        else:
            return True

    def fence_check(self, coord):
        """Checks to see if the coordinate chosen contains a fence"""
        if coord in self.get_v_list() or coord in self.get_h_list():
            return False
        else:
            return True

    def get_player_turn(self):
        """Returns whos turn it is"""
        return self._current_turn

    def turn_swap(self, player_turn):
        """Changes the move from one player to the other, i.e. if player one just went,
        it's player 2s turn now and vice versa"""
        if player_turn == 1:
            self._current_turn = 2

        if player_turn == 2:
            self._current_turn = 1

    # Check to see if any player has won yet
    def is_winner(self, player_numb):
        """Checks to see if either player has won"""
        # Initialize lists to contain all the potential victory conditions for each player
        p1_win_con = []
        p2_win_con = []
        # Add the win conditions to each players win condition list, which is the opposite end of the board
        for i in range(0, 8):
            p1_win_con.append((8, i))
            p2_win_con.append((0, i))
        # If player one's location is in the list of win condition areas, player one wins
        if player_numb == 1:
            if self.get_p1() in p1_win_con:
                return True
            else:
                return False
        # If player two's location is in the list of win condition areas, player two wins
        if player_numb == 2:
            if self.get_p2() in p2_win_con:
                return True
            else:
                return False

    def pawn_jump(self, player_turn, coord):
        """Check validity of a pawn jump move by seeing if the opponent pawn is in a nearby square"""
        # If either player is attempting to pawn jump, check for pawn facing to allow a pawn jump
        if player_turn == 1:
            # If the x coordinate or y coordinate being declared is two spaces away, ensure the opposing pawn is only
            # one space away
            if coord[0] == (self._p1_x_coord + 2) or coord[1] == (self._p1_y_coord + 2):
                if coord[0] is not (self._p2_x_coord + 1) or coord[1] is not (self._p2_y_coord + 1):
                    return False
            else:
                return True
            # See comments above, same concept just for player two instead of player one
        if player_turn == 2:
            if coord[0] == (self._p2_x_coord + 2) or coord[1] == (self._p2_y_coord + 2):
                if coord[0] is not (self._p1_x_coord + 1) or coord[1] is not (self._p1_y_coord + 1):
                    return False
            else:
                return True

    def normal_move_check(self, player_turn, coord):
        """Checks that the player is making a standard move up, down, left, or right"""
        if player_turn == 1:
            # Calculate the four possible normal moves in every direction
            p1_norm_1 = (coord[0] == (self._p1_x_coord + 1)) and (coord[1] == self._p1_y_coord)
            p1_norm_2 = (coord[0] == (self._p1_x_coord - 1)) and (coord[1] == self._p1_y_coord)
            p1_norm_3 = (coord[0] == self._p1_x_coord) and (coord[1] == (self._p1_y_coord + 1))
            p1_norm_4 = (coord[0] == self._p1_x_coord) and (coord[1] == (self._p1_y_coord - 1))
            # If the attempted coordinate is any normal move, return True
            if p1_norm_1 or p1_norm_2 or p1_norm_3 or p1_norm_4 == True:
                return True

        if player_turn == 2:
            # See notes above, same calculations just for player 2 instead of player 1
            p2_norm_1 = (coord[0] == (self._p2_x_coord + 1)) and (coord[1] == self._p2_y_coord)
            p2_norm_2 = (coord[0] == (self._p2_x_coord - 1)) and (coord[1] == self._p2_y_coord)
            p2_norm_3 = (coord[0] == self._p2_x_coord) and (coord[1] == (self._p2_y_coord + 1))
            p2_norm_4 = (coord[0] == self._p2_x_coord) and (coord[1] == (self._p2_y_coord - 1))
            if p2_norm_1 or p2_norm_2 or p2_norm_3 or p2_norm_4 == True:
                return True

    def diag_check(self, player_turn, coord):
        """Check to see if the pawn move attempting to be committed is forbidden, either because it is not the players turn,
    or because it violates the pawn movement rules of Quoridor"""
        # Check all combinations of diagonals, if it's confirmed a player is attempting to move diagonally,
        # check if that's a valid option based off the presence of a pawn + fence
        if player_turn == 1:
            p1_diag_1 = (coord[0] == (self._p1_x_coord + 1) and coord[1] == (self._p1_y_coord + 1))
            p1_diag_2 = (coord[0] == (self._p1_x_coord - 1) and coord[1] == (self._p1_y_coord + 1))
            p1_diag_3 = (coord[0] == (self._p1_x_coord - 1) and coord[1] == (self._p1_y_coord - 1))
            p1_diag_4 = (coord[0] == (self._p1_x_coord + 1) and coord[1] == (self._p1_y_coord - 1))
            if p1_diag_1 or p1_diag_2 or p1_diag_3 or p1_diag_4 == True:
                return False

        if player_turn == 2:
            # Same calculations as above, just performed for player 2
            p2_diag_1 = (coord[0] == (self._p2_x_coord + 1) and coord[1] == (self._p2_y_coord + 1))
            p2_diag_2 = (coord[0] == (self._p2_x_coord - 1) and coord[1] == (self._p2_y_coord + 1))
            p2_diag_3 = (coord[0] == (self._p2_x_coord - 1) and coord[1] == (self._p2_y_coord - 1))
            p2_diag_4 = (coord[0] == (self._p2_x_coord + 1) and coord[1] == (self._p2_y_coord - 1))
            if p2_diag_1 or p2_diag_2 or p2_diag_3 or p2_diag_4 == True:
                return False

        return True

    def is_move_forbidden(self, player_turn, coord):
        """Checks to see if the currently attempted move is legal, with regards to things such as pawn jumping,
        diagonal moves, moving out of turn, attempting to move through fences, etc."""
        # If it's not the chosen players turn to move, return False
        if not self.turn_check(player_turn):
            return False
        # If the player is attempting to sit in place, or move directly on top of another pawn, return False
        if not self.on_top_check(coord):
            return False
        # If where the player is attempting to move to has a fence in place, return False
        if not self.fence_check(coord):
            return False
        # If the player is attempting a pawn jump, check validity of that move
        if not self.pawn_jump(player_turn, coord):
            return False
        # If the player is attempting to move diagonally, check the validity of that move
        if not self.diag_check(player_turn, coord):
            return False
        # Check to make sure the move is considered "normal" i.e. a move in one space up, down, left, or right
        if not self.normal_move_check(player_turn, coord):
            return False

        return True

    # Check to see if the fence placement attempting to be committed is forbidden, either because it is not the
    # players turn, or because it violates the fence placing rules of Quoridor

    def fence_inventory(self, player_turn):
        """Makes sure players have not run out of fences and are attempting to place a new one"""
        # If the player attempting to place the fence has zero fences, return False
        if player_turn == 1:
            if self._p1_fence_count == 0:
                return False
        if player_turn == 2:
            if self._p2_fence_count == 0:
                return False

    def is_fence_forbidden(self, player_turn, orientation, coord):
        """Checks to see if the currently attempted fence placement is legal"""
        # If it's not the chosen players turn to move, return False
        if not self.turn_check(player_turn):
            return False
        # Check that the player has fences available to place
        if not self.fence_inventory(player_turn):
            return False
        # If the player attempts to place a fence on top of either pawn, return False
        if not self.on_top_check(coord):
            return False
        # If the player attempts to place a fence where there's already a fence, return False
        if not self.fence_check(coord):
            return False

    # Method used to move the player's pawn
    def move_pawn(self, player_turn, coord):
        """Method that allows the player to move a pawn to a selected spot"""
        # If a player has already won, return False
        if self.is_winner(player_turn) is True:
            return False
        # Ensure the move is not forbidden by using the is move forbidden method
        if not self.is_move_forbidden(player_turn, coord):
            return False
        # If it's player ones turn, set the p1 coordinate to the input coordinate. Then return true either if the game
        # has been won, or if the move was succesful
        if player_turn == 1:
            self.turn_swap(player_turn)
            self._p1 = coord
            if self.is_winner(1):
                return True
            return True
        # Same as the above code for player 1, only this time for player 2
        if player_turn == 2:
            self.turn_swap(player_turn)
            self._p2 = coord
            if self.is_winner(2):
                return True
            return True

    def place_fence(self, player_turn, orientation, coord):
        """Method that allows the player to move a pawn to a selected spot"""
        # If a player has already won, return False
        if self.is_winner(player_turn) is True:
            return False
        # Check to make sure the fence placement is possible via the rules of the game
        self.is_fence_forbidden(player_turn, orientation, coord)
        # Change turns
        self.turn_swap(player_turn)
        # If the fence being placed is horizontal, append the fence to the horizontal fence list
        if orientation == "h":
            self._h_list.append(coord)
            return True
        # If the fence being placed is vertical, append the fence to the vertical fence list
        if orientation == "v":
            self._v_list.append(coord)
            return True

# q = QuoridorGame()
# print(q.get_player_turn())
# print(q.move_pawn(2, (4,7))) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
# print(q.get_player_turn())
# print(q.move_pawn(1, (4,1))) #moves the Player1 pawn -- valid move, returns True
# print(q.get_player_turn())
# print(q.place_fence(1, 'h',(6,5))) #places Player1's fence -- out of turn move, returns False
# print(q.move_pawn(2, (4,7))) #moves the Player2 pawn -- valid move, returns True
# print(q.place_fence(1, 'h',(6,5))) #places Player1's fence -- returns True
# print(q.place_fence(2, 'v',(3,3))) #places Player2's fence -- returns True
# q.is_winner(1) #returns False because Player 1 has not won
# q.is_winner(2) #returns False because Player 2 has not won