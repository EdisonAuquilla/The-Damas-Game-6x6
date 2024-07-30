CHECKERS GAME-DRAFT
"Central University of Ecuador"
Programming I
MEMBERS:
-Edison Auquilla
- Jaren Tuarez
Checkers game in Python 🎮
![image](https://github.com/user-attachments/assets/072ae9b1-b511-4b01-9101-45ac84e92649)
DESCRIPCTION 📜:
Welcome to Checkers in Python! This project is an implementation of the classic Checkers game using Python and Tkinker. Below you will find all the information about the project.

Game Overview🕹️
The game of checkers is a strategic board game for two players that is played on a square board divided into 64 squares arranged in an 8x8 matrix, in this case 6x6. Each player starts with 6 pieces, which are placed on the dark squares of the board in the three rows closest to them. The basic rules are the following:

Objective of the game:

Capture all of the opponent's pieces or block them so that they cannot move.
Movements:

The pieces move diagonally on the dark squares of the board.
In their normal movement, the pieces move one square diagonally forward.
Capture:

To capture an opponent's piece, a piece must jump over it in a diagonal movement. The captured piece is removed from the board.

Promotion to Lady:

When a piece reaches the farthest row of the board, it becomes a "queen" (or "queen"). Checkers have the ability to move diagonally in any direction, not just forward like normal pieces.
Victory:

The game ends when one player captures all of the opponent's pieces or blocks the opponent from making valid moves.

The game of checkers combines strategy and tactics, as players must plan both their moves and the moves of their opponents to achieve victory.

Functional Requirements
1) User Interface:

Board: Show a checkerboard of 6x6 squares, with alternating squares in dark and light colors, easy to distinguish and appreciate.
Pieces: Show 6 pieces for each player on the dark squares in the three rows closest to them.
Interaction: Allow players to select and move pieces according to the game rules.
2) Piece Movements:

Normal Movement: Allowing pieces to move diagonally forward on an empty square.
Capture: Allow pieces to jump over opponent's pieces to capture them, and remove captured pieces from the board.
Queen Movement: Allow queens to move diagonally in any direction and capture pieces in any direction.
3) Rules of the Game:

Promotion to Queen: Promote a piece to a queen when it reaches the opposite row of the board.
Mandatory Capture: Implement mandatory capture rules if applicable.
End of the Game: Determine victory when a player has captured all of the opponent's pieces or has blocked the opponent.
4) Shifts:

Turn Control: Alternate turns between players in a fair and appropriate manner, starting with the color black.
5) Messages and Notifications:

Victory/Loss: Display a message when the game ends, indicating the winner or if there has been a tie.

Non-Functional Requirements
1) Usability:

Intuitive Interface: The game should be easy for users to understand and play, with a clear interface and intuitive buttons.
Accessibility: Design should consider accessibility for players with disabilities, such as adequate contrast and support for assistive technologies.
2) Performance:

Response Speed: User interactions, such as moving parts and capturing, must be fast and fluid.

3) Security:

Error Prevention: The system must correctly handle erroneous input and invalid game states.
Data Protection: If required, ensure the protection of user data and the state of the game.
4) Compatibility:

Cross-Platform: The game must be compatible with all major browsers and operating systems if played on a web platform.
Devices: Should work well on different screen sizes and devices, such as desktops, tablets, and mobile phones.
5) Maintainability:

Clean Code: The code should be modular and well documented to facilitate future updates and maintenance.
Documentation: Provide clear documentation on how the game works and its code for future developers.
These requirements ensure that the checkers game works correctly and offers a satisfactory user experience.

Features ✨
Dmas Game: includes a database (Sulite3), where certain information about the game will be saved.
Educational user interface: designed with tkinter for an easy-to-use and visually striking experience.
Players will have a space where they can see whose turn it is and the player's score is tracked.
Game 🎮
![image](https://github.com/user-attachments/assets/0c026ade-3af7-489f-84e8-637515f67c5d)
![image](https://github.com/user-attachments/assets/44f34394-f616-466c-b288-bb23786346a1)

Game controls
The game is controlled only with the mouse.

