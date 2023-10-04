# Zombie Math Escape: A Text-Based Game

This game represents my final assignment for the University of Gävle. In "Zombie Math Escape", both skill and luck are required to win. The player is trapped in a house with zombies. The only way out? Answering math questions correctly and choosing the right door to avoid the zombies.


## Game Overview

- **Objective**: Answer math questions correctly and choose the right door to escape the zombies and win the game.
- **Challenges**: Each math question is followed by a choice of doors. Beware, zombies lurk behind one!

## Game Setup

- **Number of Questions**: Players choose the number of questions (ranging from 12 - 39).
- **Math Operations**: Players select the mathematical operation for the game. Options are:
  - Multiplikation (Multiplication)
  - Heltalsdivision (Integer Division)
  - Modulus
  - Slumpade räknesätt (Randomized Operations)

- **Number Selection**:
  - For multiplication: Choose a table (2 - 12).
  - For integer division and modulus: Choose a divisor (2 - 5).
  - For randomized operations: Both factor and table/divisor are randomized.

## Game Rules

- The same math question should not be repeated unless necessary.
- Depending on the number of questions, repetition limits apply:
  - 13 or fewer questions: No repetitions.
  - 14 - 26 questions: Maximum two repetitions.
  - 27 - 39 questions: Maximum three repetitions.

- The game begins with a math question. Answer correctly to proceed to the door choice.
- The number of doors matches the number of questions. It decreases with each round.
- Only one door has zombies behind it. Make the right choice to continue.
- The final question doesn't have a door choice. Answering it correctly wins the game.

## User Interface

- Players are constantly informed about their game progress: number of correct answers, remaining questions, and which door had zombies in the previous round.
- The game has robust input validation. It ensures inputs are integers and within valid ranges.

## Game Flow

- An incorrect answer or wrong door choice ends the game.
- Players are asked if they want a rematch upon game completion.
- If a player loses and opts for a rematch, the game parameters remain the same.
- If a player wins and opts for a rematch, they can choose new game parameters.

---

