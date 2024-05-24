### 4. Shoot The Circles

Project Features: <br>
- Shooter Control: A shooter circle is placed at the bottom of the player's screen, and it can be moved horizontally using the 'a' and 'd' keys. The shooter's movement is restricted to stay within the screen boundaries.
- Firing Mechanism: Players can shoot by pressing the spacebar, sending a fire projectile upwards on the screen.
- Falling Circles: Circles fall vertically from the top of the screen. To score a point, the shooter must hit a falling circle directly. The horizontal position of each falling circle is randomized.
- Scoring: Successfully hitting a falling circle increases the player's score by 1 and both the projectile and falling circle will be removed from the screen upon hit. The current score is displayed in the console for tracking.
- Game Over: The game can be over in any of the first two following ways:
- If a falling circle touches the circle shooter directly, the game will be over immediately.
- If the player misses three falling circles to shoot, i.e. falling circles crossing the bottom boundary before the circle shooter manages to vanish them three times, the game will be over.  
- Bonus and Optional: The game will also be over if a player misfires, i.e. shoots but fails to hit any falling circle three times, the game will be over.
In this state, falling circles disappear, shooter movement is disabled, and "Game Over" is displayed in the console along with the final score.
- Control Buttons: Three clickable buttons are positioned at the top of the screen:
- Left Arrow (Restart): Clicking this button restarts the game, resetting the score and circle speed. A message like "Starting Over" is shown in the console.
- Play/Pause Icon (Amber Colored): This button toggles the game between play and pause states. The icon represents the current state. In the pause state, falling circles freeze, and shooter movement is disabled.
- Cross (Red Colored): Clicking this button prints "Goodbye" in the console along with the final score and terminates the game.
- Circle Drawing: All circles on the screen are drawn using the midpoint circle drawing algorithm. The primitive type used for drawing circles is GL_POINTS. The size of the circles is designed to be visible but not overly large, similar to the shooter's size.
