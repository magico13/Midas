#Base class for apps for the 2.8" PiTFT and "ArmOS"
import utils
import pygame
class App(object):
  
  def __init__(self):
    self.Buttons = []
    self.Texts = []
    self.PopUps = []
  
  def FirstDraw(self, screen):
    for button in self.Buttons:
      button.Draw(screen)
    for text in self.Texts:
      text.Draw(screen)
    pygame.display.update()
    return
      
  def Draw(self, screen):
    worked = len(self.PopUps) > 0
    for popup in self.PopUps:
      if not popup.Tick(screen):
        self.PopUps.remove(popup)
    return worked
    
  def Button_Release_1(self): #fired on button 1 release (#17)
    return
    
  def Button_Release_2(self): #fired on button 2 release (#22)
    return
    
  def Button_Release_3(self): #fired on button 3 release (#23)
    return
    
  def Button_Release_4(self): #fired on button 4 release (#27)
    return
    
  def MouseClick(self, mousePos):
    for button in self.Buttons:
      button.Check(mousePos)
    return
    
  def EventLoop(self, events):
  #  for event in events:
  #    if event.type == pygame.MOUSEBUTTONDOWN:
  #      self.MouseClick(pygame.mouse.get_pos())
    return
    
  def GetButtonByID(self, btnID):
    for b in self.Buttons:
      if b.NAME == btnID:
        return b
    return None
  
  def GetTxtByID(self, txtID):
    for t in self.Texts:
      if t.NAME == txtID:
        return t
    return None
