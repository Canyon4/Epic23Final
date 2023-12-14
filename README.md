This project is an RC car that has a digital screen to display things such as text, images or pretty much whatever. Along with 2 LEDs that flash between colors and 2 speakers that can play audio clips like a car horn.
This project utilizes the SparkFun JetBot Ai kit v3.0. which acts as the main component for the RC car. This project only includes the basic cardinal direction movement and camera of the jetbot, but there are more
librarys within the jetbot like object collision and object following that you can implement. This project also uses a raspberry pi with a 7 inch capacitive touch screen from Eviciv and 2 RGB LEDs from Keyestudio.
There are 3 scripts for this project, the LED light bulb script called bulb.py and the soundboard script to play sounds called Horn.py. Both of which you run via the raspberry pi. The last script is for
the movement of the robot and activiting the camera, which is called Car.py. Car.py will need to be run from the jupiter notebook lab that is associated with your robot's IP adress. Below are steps for setting up each
indivdual compenent of this project. There are also plenty of documentaiton online regarding all of this if you need it.



Project Parts:

- SparkFun jetbot:
  https://www.sparkfun.com/products/18486

- 7 inch touch screen:
  https://www.amazon.com/EVICIV-Raspberry-Dual-Speaker-Compatible-Drive-Free/dp/B07L6WT77H

- Keyestudio LED lights:
  https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiyupGjh42DAxVsMDQIHZxNCU0QFnoECA8QAQ&url=https%3A%2F%2Fwww.keyestudio.com%2Fproducts%2Fkeyestudio-full-color-red-green-blue-rgb-module-for-arduino&usg=AOvVaw2PulBPY7EWT0kFtUH8uQiV&opi=89978449

- Raspberry Pi

-2 battery packs for the jetbot and the 7 in screen. One comes with the Jetbot starter kit.


Setting up the car:

https://learn.sparkfun.com/tutorials/assembly-guide-for-sparkfun-jetbot-ai-kit-v20/introduction
This is a link to the actual step by step assembly guide for the jetbot which includes the softwar setup.

During the assembly process I did have some issue getting one of the motors to work. I am lucky enough to have multiple motors on hand that I could swap with untill I found one that works but you may need to buy new
or differnet motors for this kit. Its also important to note that the SSD comes PRE FLASHED so dont flash an image onto the SSD. Refer to the Car.py python file which involves setting up the movement of the car and the camera.


Setting up the 7 in display:
Using the the screws and holes on the back of the screen, I mounted the raspberry to the back of the screen and used a display, ribbon to HDMI, cable to connect them. I then connected the display power cable to a USB port on the raspberry pi and
a power bank to the raspberry pi.

Setting up the LED lights:
I used keyestudio LED lights by connecting them to the raspberrypi gpio pins with female-to-female jumper cables. Then, I taped the LEDs to the back of the screen to hold them up. The code to use the LEDs is uploaded as bulb.py.

