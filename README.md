# SnakeGame
This is a SnakeGame which is a classic arcade game where the player controls a snake, guiding it around a grid to consume food items that appear at random locations. Each time the snake eats food, it grows longer, making the game progressively more challenging as the player must avoid colliding with the walls and the snake's own body.
Game Mechanics:

Grid Layout:

The game board consists of a grid of 25 rows and 25 columns.
Each grid tile is 25x25 pixels in size.
The game window is 625x625 pixels (25 tiles * 25 pixels per tile).
Snake:

The snake starts at a predetermined position on the grid.
The snake's body is initially a single tile but grows longer each time it eats food.
The snake can move in four directions: up, down, left, and right.
The direction is controlled by the arrow keys.
Food:

Food items appear randomly on the grid.
When the snake's head reaches the food tile, the food is "eaten," and a new food item appears at a different random location.
Eating food causes the snake to grow by one tile.
Movement:

The snake moves continuously in the current direction.
The player changes the direction of the snake using the arrow keys.
The game logic ensures that the snake cannot reverse direction directly (e.g., from moving right to left).
Collision Detection:

The game ends if the snake's head collides with the wall of the game window.
The game also ends if the snake's head collides with any part of its body.
Upon game over, a message displaying the player's score is shown on the screen.
Score:

The score increases by one point for each food item eaten.
The current score is displayed in the top-left corner of the game window.
Upon game over, the final score is displayed in the center of the screen.
Gameplay Experience:
The player navigates the snake around the game board to eat food and grow longer. The challenge increases as the snake grows longer, making it more difficult to avoid collisions with the walls and its own body. The game tests the player's reflexes and strategic planning skills.

Controls:

Up Arrow: Move the snake upward.
Down Arrow: Move the snake downward.
Left Arrow: Move the snake to the left.
Right Arrow: Move the snake to the right.
Game Over Conditions:

The snake's head hits the wall.
The snake's head collides with any part of its body.
Visual Elements:

The game board has a black background.
The snake is represented by white tiles.
The food is represented by a red tile.
Game Loop:

The game runs continuously, updating the snake's position and checking for collisions at regular intervals (every 100 milliseconds).
Starting the Game:

The game starts automatically when the program is run.
The player can start controlling the snake immediately using the arrow keys.
This classic Snake game is a simple yet engaging way to test and improve one's reaction time and strategic thinking skills. The game's increasing difficulty as the snake grows provides a fun and challenging experience.
