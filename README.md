# Tic tac toe

## Installing

Create a new virtualenv & run `pip install -r requirements.txt` to install the
dependencies.

## Running

Run `make` to continously run the tests, `make test` to run tests once, `make run`
to run the game defined in `ttt.game.main`.

## Task: Tic-tac-toe

Implement [tic-tac-toe](http://en.wikipedia.org/wiki/Tic-tac-toe) as a CLI game for 2 players

- Player is asked to place their sign (X,O) by giving a position ((A,B,C) x (1,2,3))
- If a player chooses an already taken position, ask them again
- show updated grid
- repeat while
  - no player has 3 signs in a vertical, horizontal or diagonal row
  - OR the game is a draw (all positions filled, but no winner)


## Rules

- Switch seats at least every 5 min
- Try to limit yourself to adding logic when there is a failing test for it
- Start from the UI, not some abstract logic!
