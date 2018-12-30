# The point of this program is to be a WYSIWYG App Builder
# At the very least it should let you assign colors, buttons, and text

import pygame, sys, os, time, json
from pygame.locals import *


import utils
from utils import COLORS

AppName = "App_NEW"

LoadFile = "load.json"

Buttons = []
Texts = []

#mouse modes
M_NORMAL = 0
M_BTN_START = 1
M_BTN_ACTIVE = 2
M_TXT_START = 3

MouseMode = M_NORMAL
Mouse_Prev_Pt = (0, 0)

SELECTED_ITEM = None

WIDTH = 800
HEIGHT = 480

WIN_W = WIDTH + 320
WIN_H = HEIGHT + 240

#utils.ACTIVE_TXTFIELD = None

#Keyboard modes


bkColor = COLORS.BLACK
ScreenButtons = []
ScreenTexts = []

def init(window):
    #intialize all the buttons/text we need for the program
    Texts.append(utils.Text("na", "N/A", (0, WIN_H-20), 24, COLORS.RED))
    #background color buttons
    Texts.append(utils.Text("txtBkColor", "Bk Color", (0, 0), 24))
    x=64
    Buttons.append(utils.Button("bkWhite", (x, 0), (16, 16), COLORS.WHITE, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkBlack", (x, 0), (16, 16), COLORS.BLACK, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkRed", (x, 0), (16, 16), COLORS.RED, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkGreen", (x, 0), (16, 16), COLORS.GREEN, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkBlue", (x, 0), (16, 16), COLORS.BLUE, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkCyan", (x, 0), (16, 16), COLORS.CYAN, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkMagenta", (x, 0), (16, 16), COLORS.MAGENTA, onClick=ChangeScreenBackground))
    x+=16
    Buttons.append(utils.Button("bkYellow", (x, 0), (16, 16), COLORS.YELLOW, onClick=ChangeScreenBackground))

    Buttons.append(utils.Button("btnNewBtn", (0, 32), (80, 32), COLORS.BLACK, "New Btn", COLORS.WHITE, NewBtnFn, 24))
    
    
    Buttons.append(utils.Button("btnNewTxt", (0, 72), (80, 32), COLORS.BLACK, "New Txt", COLORS.WHITE, NewTxtFn, 24))
    
    
    x=WIN_W-150
    Buttons.append(utils.Button("btnWhite", (x, 200), (16, 16), COLORS.WHITE, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnBlack", (x, 200), (16, 16), COLORS.BLACK, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnRed", (x, 200), (16, 16), COLORS.RED, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnGreen", (x, 200), (16, 16), COLORS.GREEN, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnBlue", (x, 200), (16, 16), COLORS.BLUE, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnCyan", (x, 200), (16, 16), COLORS.CYAN, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnMagenta", (x, 200), (16, 16), COLORS.MAGENTA, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnYellow", (x, 200), (16, 16), COLORS.YELLOW, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    
    x=WIN_W-150
    Buttons.append(utils.Button("btnTxtWhite", (x, 280), (16, 16), COLORS.WHITE, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtBlack", (x, 280), (16, 16), COLORS.BLACK, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtRed", (x, 280), (16, 16), COLORS.RED, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtGreen", (x, 280), (16, 16), COLORS.GREEN, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtBlue", (x, 280), (16, 16), COLORS.BLUE, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtCyan", (x, 280), (16, 16), COLORS.CYAN, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtMagenta", (x, 280), (16, 16), COLORS.MAGENTA, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    x+=16
    Buttons.append(utils.Button("btnTxtYellow", (x, 280), (16, 16), COLORS.YELLOW, onClick=ChangeActiveItemColor))
    Buttons[len(Buttons)-1].SetVisible(False)
    
    Buttons.append(utils.Button("btnSave", (0, 110), (80, 32), COLORS.BLACK, "SAVE", COLORS.WHITE, SaveApp, 24))
    
    try:
        global ScreenButtons, ScreenTexts
        ScreenButtons, ScreenTexts = utils.load(None, LoadFile)
        for b in ScreenButtons: b.OnClick = SelectScreenBtn
    except:
        print("couldn't load existing file")
        pass
    
    
def DrawFull(window, screen):
    #draws the full window each frame, including the screen portion
    window.fill(COLORS.WHITE)
    
    DrawScreen(screen)
    #draw the pseudo status bar
    #StatusBarSurf = pygame.Surface((320, 10))
    #StatusBarSurf.fill(COLORS.WHITE)
    #screen.blit(StatusBarSurf, (0, 0))
    StatusBarSurf = pygame.Surface((800, 40))
    StatusBarSurf.fill(COLORS.WHITE)
    screen.blit(StatusBarSurf, (0, 440))
    
    #draw the home button
    #homeBtn = utils.Button("btnHome", (0, 0), (50, 10), COLORS.RED, "HOME", COLORS.WHITE, None)
    #homeBtn.TXTSIZE = 18
    #homeBtn.Draw(screen)
    
    
    #Draw the time on the right
    #clockTxt = utils.Text("txtClock", "12:00", (285, -2), 18)
    #clockTxt.Draw(screen)
    
    #draw the slight background around the screen
    border = pygame.Surface((WIDTH+6, HEIGHT+6))
    borderColor = COLORS.BLACK
    if bkColor == COLORS.BLACK: borderColor = COLORS.CYAN
    border.fill(borderColor)
    window.blit(border, (157, 117))
    
    #draw the screen
    window.blit(screen, (160, 120))
    
    #draw all buttons and texts
    for button in Buttons:
        button.Draw(window)
    for text in Texts:
        text.Draw(window)
    
    global AppName
    AppName = utils.TextField("txtAppName", AppName, (160, 90), (WIDTH, 20)).Draw(window)
    
    if (SELECTED_ITEM != None):
        if (isinstance(SELECTED_ITEM, utils.Button)):
            DrawSidebarButton(window)
        elif (isinstance(SELECTED_ITEM, utils.Text)):
            DrawSidebarText(window)
    
    pygame.display.update()

def DrawScreen(screen):
    screen.fill(bkColor)
    #draw everything else that was added to the screen
    for button in ScreenButtons:
        button.Draw(screen)
    for text in ScreenTexts:
        text.Draw(screen)
        
    if (MouseMode == M_BTN_ACTIVE and InScreen(pygame.mouse.get_pos())):
       # mousePosAdj = TupleMath(pygame.mouse.get_pos(), (160, 120), True)
        #draw a rectangle to help with sizing buttons
        pygame.draw.rect(screen, COLORS.CYAN, (TupleMath(Mouse_Prev_Pt, (160, 120), True),  TupleMath(pygame.mouse.get_pos(), Mouse_Prev_Pt, True)))

def EVENTLOOP():
    #global SELECTED_ITEM
    #handle the arrow keys
    keys = pygame.key.get_pressed()
    if (keys[K_UP] or keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT]) and SELECTED_ITEM != None:
        #move or size up
        mods = pygame.key.get_mods()
        MoveOrSizeObject(mods, keys)
    
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            print("Shutting down")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            if key == K_DELETE and SELECTED_ITEM != None:
                #delete the selected item
                if (isinstance(SELECTED_ITEM, utils.Button)):
                    ScreenButtons.remove(SELECTED_ITEM)
                    Deselect()
                elif (isinstance(SELECTED_ITEM, utils.Text)):
                    ScreenTexts.remove(SELECTED_ITEM)
                    Deselect() 
            unic = event.unicode
            if (utils.KeyMode == utils.K_TEXT_ENTER and utils.ACTIVE_TXTFIELD != None):
                #the keyboard is actually entering text
                if (key == K_BACKSPACE):
                    if (len(utils.ACTIVE_TXTFIELD.TXT) > 0):
                        utils.ACTIVE_TXTFIELD.TXT = utils.ACTIVE_TXTFIELD.TXT[:-1] #remove the last part
                elif (key == K_RETURN):
                    utils.KeyMode = utils.K_NORMAL
                    utils.ACTIVE_TXTFIELD = None
                else:
                    utils.ACTIVE_TXTFIELD.TXT += unic

        elif event.type == pygame.MOUSEBUTTONDOWN:
            global MouseMode
            mousePos = pygame.mouse.get_pos()
            for button in Buttons:
                button.Check(mousePos)
          #  if (utils.ACTIVE_TXTFIELD != None):
          #      if (not utils.ACTIVE_TXTFIELD.Clicked(mousePos)):
          #          utils.KeyMode = utils.K_NORMAL
           #         utils.ACTIVE_TXTFIELD = None
            if (MouseMode == M_NORMAL and InScreen(mousePos)):
                #check if any buttons selected
                mousePosAdj = TupleMath(mousePos, (160, 120), True)
                clicked = False
                for button in ScreenButtons:
                    if button.Check(mousePosAdj):
                        clicked = True
                for txt in ScreenTexts:
                    if txt.Clicked(mousePosAdj):
                        SelectScreenTxt(txt.NAME)
                        clicked = True
                if not clicked:
                    Deselect()
                    
            elif (MouseMode == M_BTN_START and InScreen(mousePos)):
                #start a new button
                print("starting button")
                global Mouse_Prev_Pt
                Mouse_Prev_Pt = mousePos
                Texts[0].SetText("Click to Finish Button")
                MouseMode = M_BTN_ACTIVE
            elif (MouseMode == M_BTN_ACTIVE and InScreen(mousePos)):
                #get last pos and this pos, make a new button
                
                holder = len(ScreenButtons)
                taken = True
                while taken:
                #generate a unique name
                    btnName = "btn"+str(holder)
                    #taken = (GetButton(btnName) is not None)
                    taken = False
                    for btn in ScreenButtons:
                        if btn.NAME == btnName: taken = True
                    holder += 1
                    
                ScreenButtons.append(utils.Button(btnName, TupleMath(Mouse_Prev_Pt, (160, 120), True), TupleMath(mousePos, Mouse_Prev_Pt, True), onClick=SelectScreenBtn))
                MouseMode = M_NORMAL
                print("finished button "+btnName)
                Texts[0].SetText("N/A")
                SelectScreenBtn(btnName)
                
            elif (MouseMode == M_TXT_START and InScreen(mousePos)):
                holder = len(ScreenTexts)
                taken = True
                while taken:
                #generate a unique name
                    txtName = "txt"+str(holder)
                    taken = False
                    for txt in ScreenTexts:
                        if txt.NAME == txtName: taken = True
                    holder += 1
                    
                ScreenTexts.append(utils.Text(txtName, txtName, TupleMath(mousePos, (160, 120), True), 36, COLORS.WHITE))
                MouseMode = M_NORMAL
                print("finished text "+txtName)
                Texts[0].SetText("N/A")
                SelectScreenTxt(txtName)
                
def TupleMath(tupleA, tupleB, subtract=False):
    if (not subtract):
        return (tupleA[0]+tupleB[0], tupleA[1]+tupleB[1])
    else:
        return (tupleA[0]-tupleB[0], tupleA[1]-tupleB[1])

def InScreen(pos):
    return pygame.Rect((160, 120), (WIDTH, HEIGHT)).collidepoint(pos)

def DrawSidebarButton(window):
    global SELECTED_ITEM
    x = WIN_W-150
    #draws all the sidebar items for the selected button
    #change name
    SELECTED_ITEM.NAME = utils.TextField("txtFRename", SELECTED_ITEM.NAME, (x, 120), (140, 20)).Draw(window)
    
    #change position
    utils.Text("txtPos", "Pos: ({}, {})".format(SELECTED_ITEM.POS[0], SELECTED_ITEM.POS[1]), (x, 140), 24).Draw(window)
    #change size
    utils.Text("txtSize", "Size: ({}, {})".format(SELECTED_ITEM.SIZE[0], SELECTED_ITEM.SIZE[1]), (x, 160), 24).Draw(window)
    #change color
    utils.Text("txtColor", "Color:", (x, 180), 24).Draw(window)

    #change text
    utils.Text("txtTxt", "Txt: ", (x, 220), 24).Draw(window)
    SELECTED_ITEM.TXT = utils.TextField("txtFBtnTxt", SELECTED_ITEM.TXT, (x, 240), (140, 20)).Draw(window)
    #change text color
    utils.Text("txtTxtColor", "Txt Color:", (x, 260), 24).Draw(window)
    #change text size
    utils.Text("txtTxtSize", "Txt Size:", (x, 300), 24).Draw(window)
    try:
        SELECTED_ITEM.TXTSIZE = int(utils.TextField("txtFBtnTxtSz", str(SELECTED_ITEM.TXTSIZE), (x+70, 300), (70, 20)).Draw(window))
    except:
        pass
        #print("Invalid integer")
    #str(SELECTED_ITEM.TXTSIZE)
    
    #change callback
    if (not hasattr(SELECTED_ITEM, "CallbackTxt")):
        SELECTED_ITEM.CallbackTxt = "None"
    utils.Text("txtCallback", "Callback: ", (x, 320), 24).Draw(window)
    SELECTED_ITEM.CallbackTxt = utils.TextField("txtFBtnCallback", SELECTED_ITEM.CallbackTxt, (x, 340), (140, 20)).Draw(window)

def DrawSidebarText(window):
    global SELECTED_ITEM
    x = WIN_W-150
    SELECTED_ITEM.NAME = utils.TextField("txtFRename", SELECTED_ITEM.NAME, (x, 120), (140, 20)).Draw(window)
    #change position
    utils.Text("txtPos", "Pos: ({}, {})".format(SELECTED_ITEM.POS[0], SELECTED_ITEM.POS[1]), (x, 140), 24).Draw(window)
    #change color
    utils.Text("txtColor", "Color:", (x, 180), 24).Draw(window)

    #change text
    utils.Text("txtTxt", "Txt: ", (x, 220), 24).Draw(window)
    SELECTED_ITEM.TXT = utils.TextField("txtFTxt", SELECTED_ITEM.TXT, (x, 240), (140, 20)).Draw(window)
    #change text size
    utils.Text("txtTxtSize", "Txt Size:", (x, 260), 24).Draw(window)
    try:
        SELECTED_ITEM.HT = int(utils.TextField("txtFTxtSz", str(SELECTED_ITEM.HT), (x+70, 262), (70, 20)).Draw(window))
    except:
        pass


def GetButton(name):
    for button in Buttons:
        if button.NAME == name:
            return button
    return None

def Deselect():
    global SELECTED_ITEM
    SELECTED_ITEM = None
    SetColorButtons(False)

def SetColorButtons(state, btn=True):
    GetButton("btnWhite").SetVisible(state)
    GetButton("btnBlack").SetVisible(state)
    GetButton("btnRed").SetVisible(state)
    GetButton("btnGreen").SetVisible(state)
    GetButton("btnBlue").SetVisible(state)
    GetButton("btnCyan").SetVisible(state)
    GetButton("btnMagenta").SetVisible(state)
    GetButton("btnYellow").SetVisible(state)
        
    if btn or not state:
        GetButton("btnTxtWhite").SetVisible(state)
        GetButton("btnTxtBlack").SetVisible(state)
        GetButton("btnTxtRed").SetVisible(state)
        GetButton("btnTxtGreen").SetVisible(state)
        GetButton("btnTxtBlue").SetVisible(state)
        GetButton("btnTxtCyan").SetVisible(state)
        GetButton("btnTxtMagenta").SetVisible(state)
        GetButton("btnTxtYellow").SetVisible(state)

def MoveOrSizeObject(mods, keys):
    global SELECTED_ITEM
    step = 1
    if (mods & KMOD_SHIFT): step = 10
    if (keys[K_UP]):
        if (mods & KMOD_CTRL and isinstance(SELECTED_ITEM, utils.Button)):
            #size up
            SELECTED_ITEM.SIZE = TupleMath(SELECTED_ITEM.SIZE, (0, step), True)
        else:
            #move up
            SELECTED_ITEM.POS = TupleMath(SELECTED_ITEM.POS, (0, step), True)
    if (keys[K_DOWN]):
        if (mods & KMOD_CTRL and isinstance(SELECTED_ITEM, utils.Button)):
            #size
            SELECTED_ITEM.SIZE = TupleMath(SELECTED_ITEM.SIZE, (0, step), False)
        else:
            #move
            SELECTED_ITEM.POS = TupleMath(SELECTED_ITEM.POS, (0, step), False)
    if (keys[K_LEFT]):
        if (mods & KMOD_CTRL and isinstance(SELECTED_ITEM, utils.Button)):
            #size
            SELECTED_ITEM.SIZE = TupleMath(SELECTED_ITEM.SIZE, (step, 0), True)
        else:
            #move
            SELECTED_ITEM.POS = TupleMath(SELECTED_ITEM.POS, (step, 0), True)
    if (keys[K_RIGHT]):
        if (mods & KMOD_CTRL and isinstance(SELECTED_ITEM, utils.Button)):
            #size
            SELECTED_ITEM.SIZE = TupleMath(SELECTED_ITEM.SIZE, (step, 0), False)
        else:
            #move
            SELECTED_ITEM.POS = TupleMath(SELECTED_ITEM.POS, (step, 0), False)

def SetActiveTxtField(text):
    utils.ACTIVE_TXTFIELD = text
    utils.KeyMode = K_TEXT_ENTER
    print("Set utils.ACTIVE_TXTFIELD to "+text.TXT)
    
def IsActiveTxtField(name):
    if utils.ACTIVE_TXTFIELD == None: return False
    return utils.ACTIVE_TXTFIELD.NAME == name

## Button Callbacks ##
def ChangeScreenBackground(btnName):
    global bkColor
    if (btnName == "bkWhite"):
        bkColor = COLORS.WHITE
    elif (btnName == "bkBlack"):
        bkColor = COLORS.BLACK
    elif (btnName == "bkRed"):
        bkColor = COLORS.RED
    elif (btnName == "bkGreen"):
        bkColor = COLORS.GREEN
    elif (btnName == "bkBlue"):
        bkColor = COLORS.BLUE
    elif (btnName == "bkCyan"):
        bkColor = COLORS.CYAN
    elif (btnName == "bkMagenta"):
        bkColor = COLORS.MAGENTA
    elif (btnName == "bkYellow"):
        bkColor = COLORS.YELLOW

def NewBtnFn(btnName):
    global MouseMode
    Texts[0].SetText("Click to Start Button")
    MouseMode = M_BTN_START

def NewTxtFn(btnName):
    global MouseMode
    Texts[0].SetText("Click to Place Text")
    MouseMode = M_TXT_START

def SelectScreenBtn(btnName):
    global SELECTED_ITEM
    for button in ScreenButtons:
        if (button.NAME == btnName):
            if (SELECTED_ITEM != None and not isinstance(SELECTED_ITEM, utils.Button)):
                SetColorButtons(False)
            SELECTED_ITEM = button
            print("Selected button: "+SELECTED_ITEM.NAME)
            SetColorButtons(True)
            break

def SelectScreenTxt(txtName):
    global SELECTED_ITEM
    for txt in ScreenTexts:
        if (txt.NAME == txtName):
            if (SELECTED_ITEM != None and not isinstance(SELECTED_ITEM, utils.Text)):
                SetColorButtons(False)
            SELECTED_ITEM = txt
            SetColorButtons(True, False)
            break
            
def ChangeActiveItemColor(btnName):
    global SELECTED_ITEM
    if (btnName == "btnWhite"):
        SELECTED_ITEM.COLOR = COLORS.WHITE
    elif (btnName == "btnBlack"):
        SELECTED_ITEM.COLOR = COLORS.BLACK
    elif (btnName == "btnRed"):
        SELECTED_ITEM.COLOR = COLORS.RED
    elif (btnName == "btnGreen"):
        SELECTED_ITEM.COLOR = COLORS.GREEN
    elif (btnName == "btnBlue"):
        SELECTED_ITEM.COLOR = COLORS.BLUE
    elif (btnName == "btnCyan"):
        SELECTED_ITEM.COLOR = COLORS.CYAN
    elif (btnName == "btnMagenta"):
        SELECTED_ITEM.COLOR = COLORS.MAGENTA
    elif (btnName == "btnYellow"):
        SELECTED_ITEM.COLOR = COLORS.YELLOW
        
    elif (btnName == "btnTxtWhite"):
        SELECTED_ITEM.TXTCOLOR = COLORS.WHITE
    elif (btnName == "btnTxtBlack"):
        SELECTED_ITEM.TXTCOLOR = COLORS.BLACK
    elif (btnName == "btnTxtRed"):
        SELECTED_ITEM.TXTCOLOR = COLORS.RED
    elif (btnName == "btnTxtGreen"):
        SELECTED_ITEM.TXTCOLOR = COLORS.GREEN
    elif (btnName == "btnTxtBlue"):
        SELECTED_ITEM.TXTCOLOR = COLORS.BLUE
    elif (btnName == "btnTxtCyan"):
        SELECTED_ITEM.TXTCOLOR = COLORS.CYAN
    elif (btnName == "btnTxtMagenta"):
        SELECTED_ITEM.TXTCOLOR = COLORS.MAGENTA
    elif (btnName == "btnTxtYellow"):
        SELECTED_ITEM.TXTCOLOR = COLORS.YELLOW
    
def SaveApp(btnID):
    print("Saving .json")
    data = {}
    data['buttons'] = []
    data['texts'] = []
    for b in ScreenButtons:
        if (not hasattr(b, "CallbackTxt")):
            b.CallbackTxt = "None"
        bjson = {}
        bjson['name'] = b.NAME
        bjson['position'] = b.POS
        bjson['size'] = b.SIZE
        bjson['color'] = b.COLOR
        bjson['text'] = b.TXT
        bjson['textColor'] = b.TXTCOLOR
        bjson['textSize'] = b.TXTSIZE
        bjson['callback'] = b.CallbackTxt
        data['buttons'].append(bjson)
    
    #Add Texts
    for t in ScreenTexts:
        tjson = {}
        tjson['name'] = t.NAME
        tjson['text'] = t.TXT
        tjson['position'] = t.POS
        tjson['height'] = t.HT
        tjson['color'] = t.COLOR
        data['texts'].append(tjson)
        
    with open(AppName+".json", "w") as w:
        json.dump(data, w, indent=2)
    
    #create an app template
    #create all the buttons and texts
    #create all the callback functions needed
    print("Saving .py")
    with open(AppName+".py", "w") as f:
        writeline(f, "from app import App")
        writeline(f, "import utils")
        writeline(f, "from utils import COLORS")
        writeline(f, "")
        writeline(f, "class "+AppName+"(App):")
        writeline(f, "\tdef __init__(self):")
        writeline(f, "\t\tsuper("+AppName+", self).__init__()")
        writeline(f, "\t\tself.Buttons, self.Texts = utils.load(self, '{0}.json')".format(AppName))
        writeline(f, "")
        
        #Start FirstDraw function
        writeline(f, "\tdef FirstDraw(self, screen):")      
        #Draw background
        writeline(f, "\t\t#Draw the background")
        writeline(f, "\t\tbackground = pygame.Surface(screen.get_size())")
        writeline(f, "\t\tbackground.fill({0})".format(bkColor))
        writeline(f, "\t\tscreen.blit(background, (0, 0))")
        
        writeline(f, "")
        writeline(f, "\t\tsuper("+AppName+", self).FirstDraw(screen)")
        writeline(f, "")
        #End FirstDraw function
        #Start callback functions
        for b in ScreenButtons:
            if b.CallbackTxt != "None":
                writeline(f, "\tdef "+b.CallbackTxt+"(self, btnID):")
                writeline(f, "\t\t#Autogenerated Method Stub")
                writeline(f, "\t\tprint('"+b.CallbackTxt+" - {}'.format(btnID))")
                writeline(f, "")
         

def writeline(filehandle, line):
    filehandle.write(line+"\n")
    
## MAIN ##
pygame.init()
window = pygame.display.set_mode((WIN_W, WIN_H), 0, 32)
windowBack = pygame.Surface((WIN_W, WIN_H))
windowBack.fill(COLORS.WHITE)
window.blit(windowBack, (0,0))
# controls will be on the sides mainly, but maybe top/bottom too
#screen is a 320x240 surface in the center
screen = pygame.Surface((WIDTH, HEIGHT))
screen.fill(bkColor)

init(window)

PyClock = pygame.time.Clock()
while True:
    EVENTLOOP()
    DrawFull(window, screen)
    PyClock.tick(30) #keep the framerate at a reasonable limit
