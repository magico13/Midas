# Midas
UI Builder/Editor for Raspberry Pi Touch Interfaces using Pygame

Built around Python 2 but might work with Python 3 without conversion. Requires pygame to run. Running Midas.py will open up the editor and let you click to place buttons and text labels, including editing their position, color, and other attributes. Saving will create two files, a .json file containing the button/text data (for easy editing later) and a .py file that can be used to run the created applications.

To edit an existing app, rename the .json file to "load.json" and restart Midas, it will load the buttons and texts from the .json file so you can edit them. To change the size of the display (320x240 by default, as that matches the PiTFT displays from Adafruit) edit the WIDTH and HEIGHT parameters in Midas.py.

These apps are originally intended to be used as sub-apps within a main app referred to as ArmOS but can be run independently by adding the following code (the commented out section is for running on a PiTFT):
```python
if __name__=="__main__":
    #os.environ["SDL_FBDEV"] = "/dev/fb1"
    #os.environ["SDL_MOUSEDRV"] = "TSLIB"
    #os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
    #os.environ["SDL_VIDEODRIVER"] = "fbcon"

    pygame.init()
    pygame.mouse.set_visible(True)
    screen = pygame.display.set_mode((320, 240), 0, 32)
    app = New_App()
    app.FirstDraw(screen)
    pygame.display.update()
    PyClock = pygame.time.Clock()
    while True:
        app.EventLoop(pygame.event.get())
        if app.Draw(screen):
            pygame.display.update()
        PyClock.tick(2)
```


