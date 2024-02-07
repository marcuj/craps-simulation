## 4-Player Craps Simulation

Simulation of a 4-player game of Craps meant to test different strategies over a set number of rounds, with the option to do larger scale Monte Carlo simulation by setting the number of matches to be played.

The simulation can be adjusted by specifying the various initialization values in `Craps.py`.

Start the simulation by running `Craps.py`. Results are outputted to `conv_data.csv` and `hist_data.csv` with plots (if enabled). 

### To-do: 
- Add more result visualization options
- Add availability for more players
- Add ability for more complex strategies, such as changing strategy in the middle of a round
- Clean up the code, separate certain functions and initializations into different files
  - Bet returns specified in separate file
  - Default strategies specified in separate file
- Add interface to ask to specify initialization values
  - starting money, rounds, etc.
  - ask if want to do large simulation (with plot) or just low number of rounds (gives simple winning results)
  - ask how many players and what strategies
  
