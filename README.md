# piface-led-flasher
LED Flasher Script for the Raspberry Pi PiFace board

Based on example script from here: http://www.piface.org.uk/guides/Install_PiFace_Software/First_steps_with_PiFace_Digital_Python/

Because a picture speaks a thousand words, the hardware setup looks a bit like this:

![PiFace LED Flasher Board Image](https://raw.github.com/smellygeekboy/piface-led-flasher/master/678475845.jpg)

The buttons control the speed of the LED flashing. Because we are polling the state of the buttons in the while loop, sometimes you have to hold them down for a second or so.