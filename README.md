Blackjack Game Simulator
This is a Blackjack game project I coded in 2022 as the final project for my computer science class during my exchange year in Canada. The game simulates a full round of Blackjack, including player and dealer interactions, card drawing, and score calculations.

The game runs entirely through a command-line interface (CLI), allowing users to play a classic game of Blackjack by inputting commands to make decisions like hitting or standing.

How the Game Works
A deck of cards is generated, shuffled, and used to deal cards to both the player and the dealer.
The player receives two cards, and the dealer also receives two cards (one face-up and one face-down).
The player can choose to "Hit" (draw another card) or "Stand" (end their turn) by typing these options in the command line.
The dealer follows Blackjack rules, drawing cards until reaching at least 17 points.
The game automatically handles ace values, adjusting their score from 11 to 1 when necessary to prevent a bust.
The winner is determined by comparing the final scores, or based on whether the player or dealer busts (goes over 21).
Key Features
Full simulation of Blackjack rules, including handling for busts and Blackjack wins.
Simple, interactive command-line interface where the player inputs their choices.
Dynamic score calculation with ace value adjustments.
Dealer logic that adheres to standard Blackjack rules.
How to Play
Clone or download the project files to your machine.
Open a terminal or command-line window.
Run the game using Python:
bash
Copy code
python improved_blackjack.py
Follow the on-screen prompts to play a round of Blackjack.
Notes
This project is being committed all at once, as it was developed in 2022.
It serves as a classic terminal-based game, perfect for learning or practicing command-line Python applications.
