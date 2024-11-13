# Othello_Player
A real-time Othello player game engine to play a very famous board game Othello vs computer.

Developed an Othello player gaming engine as my college project under the course COL106(Data Structures and Algorithms) under the guidance of Prof. Kirti Chaudhary (Dept. of Computer Science).

Developed the logic and strategy for the engine using the concepts of MinMax theorem of Game theory and Decision Tree to make the best possible decision to place the piece.

For every piece the engine places on the board it creates a decision tree for all possibilities and picks the one which maximizes the computer's and minimizes the opponent's gain. The depth of the tree is user-controlled and can significantly increase the difficulty of the game. -This allows us to play the game in different difficulty modes with an easy-to-understand UI built using Streamlit.

At last, to play the game seamlessly, created a whole frontend using Streamlit the frontend library of Python.

Both engine and code for UI reside in one file Othello_engine+UI.py
