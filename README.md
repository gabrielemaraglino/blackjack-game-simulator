# Blackjack Game Simulator

This is a **Blackjack game project** I coded in 2022 as the final project for my computer science class during my exchange year in Canada. The game simulates a full round of Blackjack, including player and dealer interactions, card drawing, and score calculations.

The game runs entirely through a **command-line interface (CLI)**, allowing users to play a classic game of Blackjack by inputting commands to make decisions like hitting or standing.

## Features

- Classic Blackjack rules with a dealer and player.
- Deck of 52 cards with suits and values.
- Player and dealer decision-making (hit or stand).
- Displays card graphics in the terminal.
- Randomized shuffling and card drawing.

## How to Play

The goal of Blackjack is to get as close to 21 points as possible without exceeding it. Face cards (King, Queen, Jack) are worth 10 points, Aces can be worth 1 or 11 points, and all other cards are worth their face value.

- **Hit**: Draw another card.
- **Stand**: Keep your current hand and end your turn.
- The dealer must hit until their score is at least 17.

## Installation

1. **Clone the repository**:

   ```bash
    git clone https://github.com/your-username/blackjack.git
    ```

3. **Navigate to the project directory**:

   ```bash
    cd blackjack
    ```

5. **Run the game**:
    Ensure you have Python installed. You can start the game by running:

   ```bash
    python blackjack.py
    ```

## Example Output
```
Player's Cards:
    ┌──────────┐     ┌──────────┐
    | 5        |     | K        |
    |          |     |          |
    |    ♣     |     |    ♥     |
    |          |     |          |
    |        5 |     |       K  |
    └──────────┘     └──────────┘
Player's Score: 15

Dealer's Cards:
    ┌──────────┐
    | 8        |
    |          |
    |    ♠     |
    |          |
    |        8 |
    └──────────┘
Dealer's Score: 8
```
## Closing Notes

- This project is being committed all at once, as it was developed in 2022.
- It serves as a classic terminal-based game, perfect for learning or practicing command-line Python applications.
