# Python-Projects (Total-06)

## Project-01: Rock Paper Scissors Game 

**Description:**
This project allows users to play Rock Paper Scissors against the computer. The user can select their choice (rock, paper, or scissors), and the computer makes a random choice. The program then determines the winner based on the standard rules of the game.

**Game Rules**

<img src="https://github.com/user-attachments/assets/873e3f73-6458-45af-88e8-815ea0d690fb" alt="Screenshot" width="400" />


**->** Rock crushes Scissors (Rock wins)

**->** Scissors cuts Paper (Scissors wins)

**->** Paper covers Rock (Paper wins)

**->** If both players choose the same, it's a draw.

**Output:**

![Screenshot 2024-10-23 223043](https://github.com/user-attachments/assets/c802c0c9-344f-4495-868c-604f50bc324f)


## Project-02:  Hangman game! 

**Description:**
 This game allows a player to guess letters to reveal a hidden word while having a limited number of incorrect guesses (lives). The game provides feedback on each guess, tracks progress, and displays the hangman stages as lives decrease.
 
 You can play a sample version of the game here:https://hangmanwordgame.com/?fca=1&success=0#/

**Approach:**

**Step-1: **Initialize the Game: Create a list of possible words.

**Step-2: **Select a Random Word: Randomly choose a target word from the list.

**Step-3: **Display Current State: Show the current state of the word and remaining attempts.

**Step-4: **User Input: Prompt for a letter guess and validate it.

**Step-5: **Check Win/Loss Conditions: Declare the user as the winner if they guess the word; declare them as the loser if they exceed incorrect guesses.

**Step-6: **Play Again: Ask the user if they want to play again; restart or exit based on their response.

**Output: **

###
<img src="https://github.com/user-attachments/assets/e6b8ca2b-cb26-407a-91e1-9aff5bcf6df0" alt="Screenshot" width="600" />

###
<img src="https://github.com/user-attachments/assets/d936ce16-b6a8-4413-8a5a-8a123e87e3a8" alt="Screenshot" width="600" />

###
<img src="https://github.com/user-attachments/assets/921f202c-3283-4df5-bcdb-281691c5f8a0" alt="Screenshot" width="600" />

###
<img src="https://github.com/user-attachments/assets/9ed8cbef-bebc-4493-96f5-c2537bbb34a9" alt="Screenshot" width="600" />


## Project-03:  BlackJack game! 

**Description:**

The Blackjack game is a classic card game that simulates a match between a player and the dealer (computer). The main objective is to get as close to 21 points as possible without going over, while having a higher score than the dealer. This project implements the rules of Blackjack using Python.

**Game Rules**

Card Values:

**1)** 2 through 10: Worth their face value (e.g., a 2 is worth 2 points).
**2)** Jack, Queen, King: Worth 10 points each.
**3)** Ace: Can be worth either 1 or 11 points, depending on the player’s current score.
**4)** Blackjack: A combination of an Ace and a 10-point card (10, Jack, Queen, or King) is known as a Blackjack and results in an automatic win if achieved with the initial two cards.

**Goal:**

The objective is to beat the dealer’s hand without exceeding a total of 21 points, known as "busting." If the player’s hand goes over 21, they lose automatically.

**Winning Conditions:**

If the player achieves a higher score than the dealer without going over 21, they win.

If the dealer has a higher score without busting, the player loses.

If both the player and the dealer have the same score, the game ends in a draw.


**Approach:**

**step-1:** Deal Cards: Randomly select cards for the player and dealer from a list of values.

**step-2** Calculate Scores: Add up the values of the cards. If there's an Ace and the score is over 21, count the Ace as 1 instead of 11.

**step-3** Player's Turn: The player can choose to get another card ("hit") or keep their current score ("stand"). If the score goes over 21, the player loses.

**step-4** Dealer's Turn: The dealer keeps drawing cards until they reach at least 17 points. If the dealer goes over 21, the player wins.

**step-5** Determine Winner: Compare the player's and dealer's scores. The higher score under 21 wins. If both scores are the same, it’s a draw.

**Output: **

![Screenshot 2024-11-02 204101](https://github.com/user-attachments/assets/0e373fe3-e419-4792-b049-e413fd95dbd2)



## Project-04: Quiz Game!

**Description:**

The Quiz Game is a simple interactive application built using Python that tests users' knowledge with True/False questions. This project demonstrates the principles of Object-Oriented Programming (OOP) by utilizing classes and constructors to create a modular and organized code structure.

**Approach**

The application is structured around two main classes: `Question` and `QuizBrain`. The `Question` class represents individual quiz questions, while the `QuizBrain` class manages the quiz flow, tracks the score, and provides feedback to the user.

**Key Components:**

**Question Class:** Holds the question text and the correct answer.
**QuizBrain Class:** Manages the quiz logic, including asking questions, checking answers, and tracking the score.

**Features**

**Question Prompt**: Users are presented with questions and can answer with True or False.

**Score Tracking**: The application keeps track of the number of correct answers and displays the final score at the end of the quiz.

**Instant Feedback**: After each question, users receive immediate feedback on whether their answer was correct or not

**Output:**

![Screenshot 2024-11-10 222759](https://github.com/user-attachments/assets/5c633a5d-81e6-48a1-a995-854c0e19282c)
###
![Screenshot 2024-11-10 222809](https://github.com/user-attachments/assets/5baddfde-296d-47f2-8611-81c755689d68)


# Project-05: Snake Game

## Description:
The Snake Game is a classic arcade game where the player controls a snake that grows in length as it eats food while avoiding collisions with itself and the walls. This project demonstrates fundamental game development concepts, including screen setup, object-oriented programming, and user input handling.

## Game Rules:
- The player controls the snake using the arrow keys.
- The objective is to eat the food that appears on the screen, which causes the snake to grow longer.
- The game ends if the snake collides with itself or the walls.
- The score increases with each piece of food consumed.

## Approach:
1. **Screen Setup**: Created a game window with a defined width and height for an interactive experience.
2. **Snake Class**: Implemented a Snake class using Object-Oriented Programming principles to manage the snake's properties and behaviors.
3. **Movement Control**: Enabled smooth movement of the snake, allowing it to change direction based on keypress events.
4. **Food Generation**: Randomly generated food items on the screen for the snake to consume.
5. **Collision Detection**: Implemented logic to detect collisions with the walls and the snake's own body.

## Features:
- **Interactive Gameplay**: Control the snake with keyboard inputs.
- **Dynamic Scoring**: Track and display the player's score based on the number of food items consumed.
- **Game Over Conditions**: End the game when the snake collides with itself or the walls, with an option to restart.

## Output:

https://github.com/user-attachments/assets/fe6f25c4-0b61-46b3-b2ac-3e0da0466276



## Project-06: Pongman Game 🎾  

**Description**:  
The Pongman Game is a recreation of the classic arcade game Pong. This two-player game allows players to control paddles to prevent the ball from crossing their side of the screen. The game demonstrates essential programming concepts like object-oriented programming, event handling, and collision detection.  



### Game Rules:  
- **Control the paddles** to prevent the ball from crossing your side of the screen.  
- The ball bounces off the walls and paddles, increasing speed over time.  
- A player scores a point if their opponent misses the ball.  
- The first player to reach the winning score wins the game.  



### Approach:  

#### **Step 1: Create the Game Screen**  
- Used the `turtle` library to set up a game window.  
- Added a background color, screen title, and a central dividing line.  

#### **Step 2: Create the Paddles**  
- Created two paddles using a `Paddle` class with methods for movement.  
- Assigned keyboard controls for both players.  

#### **Step 3: Create the Ball**  
- Designed a ball using the `Ball` class to move across the screen.  
- Implemented logic for bouncing off walls and paddles.  

#### **Step 4: Detect Collisions**  
- Added collision detection to bounce the ball off the paddles and walls.  
- Detected when a paddle misses the ball and updated the score.  

#### **Step 5: Keep Score**  
- Introduced a scoreboard to track the score for both players.  

### Features:  
- Two-player control with `W/S` keys and `Up/Down` arrow keys.  
- Dynamic ball movement with collision detection.  
- Score tracking and display for competitive gameplay.  
- Option to restart the game after it ends.

### Output:

https://github.com/user-attachments/assets/0a949058-c24e-4e15-983e-ea46f472c86b







