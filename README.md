# Assignment-3 Final-Project: Link Up Game  
## Introductions  
This program is a GUI game application created by Python called Link Up. The player needs to find all the same Pokemon images that can be connected in pairs and click on them to clear them. When all the images are cleared, the player wins.  
## Install  
This project uses pygame package. Check if you have locally installed pygame in your console.  
> -m pip install -U pygame --user  
## Classes  
Main: Main method  
Map: Build map of the game  
Scan: The algorithm of scanning the location of images player clicked  
Check: Check if a pair of images can be cleared  
ImageButton: Build image button  
Settings: Set game title, backgrond color, screen size and game size  
## Maintainer  
@RXC0765  
## How to Play  
When game starts, 24 pairs of Pokemon images are shuffled into the screen.   
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/images/1.png)
The player needs to find and click all the same Pokemon images that can be connected in pairs. Every time a pair is clicked, they will disappear.  
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/images/2.png)
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/images/3.png)
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/images/4.png)
To be able to connect means that the connection from one image to another cannot be more than two bends, whether horizontal or vertical.  
This is an example of two images that can be cleared.  
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/ok.png)
This is an example of connection between two images is over two bends, which cannot be cleared.  
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/over2.png)
The connection between two images also cannot pass over other images.
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/col.png)
When all images are cleared, the player wins.
![avatar](https://github.com/RXC0765/Assignment-3---Final-Project/blob/main/images/5.png)
