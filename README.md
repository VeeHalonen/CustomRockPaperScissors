# CustomRockPaperScissors

This is your classic Rock, Paper, Scissors game. The only difference is that the user is able to customize it by choosing their own "rock", "paper", and "scissors".

When launched, the following menu opens:

<code>*** Welcome to Rock-Paper-Scissors! ***</code>

<code>(P)lay</code><br>
<code>(C)ustom Game</code><br>
<code>(R)estore Defaults</code><br>
<code>(Q)uit program</code><br>
<code>: </code><br>

All commands are recognized as either upper or lower case.

<b>Play</b> starts a new game where the user and the computer play Rock, Paper, Scissors against each other. <b>Q</b> quits the game and prints the win statistics, for example:

<code>&#42;&#42;&#42;STATS&#42;&#42;&#42;</code><br>
<code>Rounds played: 5</code><br>
<code>Won: 1 (20.0%)</code><br>
<code>Lost: 2 (40.0%)</code><br>
<code>Tied: 2 (40.0%)</code><br>

<code>[Press enter to continue]</code><br>

After this, the game returns to the main menu where the user can choose a new game or customize their gameplay.

<b>Custom Game</b> allows the user to set their own names for the rock, the paper, and the scissors. Any type of names are accepted as long as the three names are different from each other. There is a confirmation dialogue at the end. After the changes have been made, the user is brought back to the now updated main menu.

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

<b>Restore Defaults</b> returns the game back to the initial state of Rock-Paper-Scissors. This command is only accessible if custom commands have been set. There is once again a confirmation dialogue before any changes are reversed.

<b>Quit</b> exits the program.

