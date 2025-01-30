# SET
## Introduction
SET is a card game where the goal is to collect as many sets as possible. There are 81 unique cards, each with 4 properties: number (1, 2, or 3), symbol (⋄, ∼, ◦), color (red, green, or purple), and shading (solid, striped, or open). A set consists of 3 cards that are either all the same or all different for each characteristic. There are 12 cards on the table; the player who first recognizes a set can take it and keep it. The cards on the table are then replenished, and the game continues until all cards are used. If at any time there are no sets on the table, 3 cards are added. In this assignment, we wrote a program to play the SET game against the computer. The variant differs slightly from what is described above:
* There are always 12 cards on the table, and the player who first recognizes a set gets a point. Afterward, the set is removed, and the cards are replenished to 12.
* If, after a fixed time (e.g., 30 seconds), no set is found, the top 3 cards are removed, and 3 new cards are added.
## Manual
To run the code all of the documents must be downloaded into the same folder and pygame must be installed, the instructions can be found at https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/ . Next you can open 'Main code.py' on your preffered IDE and run it. It should immediately open the game, which then speaks for itself. 
## Making adaptations 
If you would like to change the difficulty levels, you can find the timers at line 350, 355, 360 and 365 (depending on the difficulty you're changing). There you have to change the number to the amount of seconds, times thousand, plus nine-hundred (this will put it in the right format and give the player 0.9 extra seconds during which the new cards will be displayed). For example, if you would like the timer to last 10 seconds, you can change the timer to 10900.
> Most importantly, don't forget to have fun while playing our game!
