# Rock-Paper-Scissors Game

This is a Python implementation of the classic Rock Paper Scissors game using computer vision with OpenCV and MediaPipe. The game allows you to play against the computer by showing gestures through your webcam.



## Features

- Real-time gesture recognition using your webcam
- Play Rock Paper Scissors against the computer
- Keeps track of the number of wins for both you and the computer
- Displays the final score before quitting the game

## Prerequisites
Ensure you have the following 
- Python 3.x
- OpenCV (pip install opencv-python)
- MediaPipe (pip install mediapipe)

## How to Run the Game
- Download these two files into the **same directory**: **RPS_Game.py** & **run_RPS_Game.bat**.
- Double-click **"run_RPS_Game.bat"** batch file. And wait for the Game to start.
- For those with no coding experience, who would simply love to just run the application: I am deeply sorry, but at the moment I am unable to create a **.exe executable file** that you can run without having to worry about all the required dependencies. 

## Playing the Game
-Once you run the game, you will see a countdown displayed on the screen.

-Show your gesture (rock, paper, or scissors) to the webcam before the countdown ends.

-Acceptable gestures look something like the figure( [image_credit](https://www.al.com/entertainment/2012/03/redstone_arsenal_will_host_roc.html) ) below.

-**A paper is with the fingers held closely together.**

![Gestures](Game_package\RPS.jpg)

-The game will try to recognize your gesture and compare it with the computer's randomly chosen gesture.

-**Try out different orientations and ambient light until you get a hang of which positions produce the appropriate gesture.**

-**You can find a video of the demonstration here on my [linked post](https://www.al.com/entertainment/2012/03/redstone_arsenal_will_host_roc.html).**

-The results will be displayed on the screen along with the win counts.

-Press the "**q**" key on your keyboard to quit the game. The final score will be displayed for 5 seconds before the game exits.

