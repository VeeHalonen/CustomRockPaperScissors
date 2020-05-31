# CustomRockPaperScissors

This is your classic Rock, Paper, Scissors game. The only difference is that the user is able to customize it by choosing their own Rock, Paper, and Scissors. For example: Dragon beats Orc, Orc beats Hobbit, Hobbit beats Dragon.

When launched, the following menu opens:

<code>*** Welcome to Rock-Paper-Scissors! ***</code>

<code>(P)lay</code><br>
<code>(C)ustom Game</code><br>
<code>(R)estore Defaults</code><br>
<code>(Q)uit program</code><br>
<code>: </code><br>

All commands are recognized as either upper or lower case.

**Play** starts a new game where the user and the computer play Rock, Paper, Scissors against each other. **Q** quits the game and prints the win statistics, for example:

<code>&#42;&#42;&#42;STATS&#42;&#42;&#42;</code><br>
<code>Rounds played: 5</code><br>
<code>Won: 1 (20.0%)</code><br>
<code>Lost: 2 (40.0%)</code><br>
<code>Tied: 2 (40.0%)</code><br>

<code>[Press enter to continue]</code><br>

After this, the game returns to the main menu where the user can choose a new game or customize their gameplay.

**Custom Game** allows the user to set their own names for the rock, the paper, and the scissors. Any type of name is accepted as long as the three names are different from each other. There is a confirmation dialogue at the end. After the changes have been made, the user is brought back to the now updated main menu.

<code>*** Welcome to Fire-Water-Grass! ***</code><br>

<code>(P)lay</code><br>
<code>(C)ustom Game</code><br>
<code>(R)estore Defaults</code><br>
<code>(Q)uit program</code><br>
<code>: </code><br>

The Play mode still works the same way as before but now using the user-defined commands.

<code>*** Starting new game ***</code><br>

<code>Round 1</code><br>
<code>Fire, Water, or Grass? ("Q" to quit game)</code><br>
<code>You: fire</code><br>
<code>AI: Fire</code><br>
<code>It's a tie!</code><br>

**Restore Defaults** returns the game back to the initial state of Rock-Paper-Scissors. This command only executes if a custom mode has been set. There is once again a confirmation dialogue before the default state is restored.

**Quit** exits the program.

