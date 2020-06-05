import pyautogui as atg
import time as t

def paintLoad():
    atg.hotkey('winleft','r')
    t.sleep(1)
    atg.typewrite('mspaint')
    atg.press('enter')
    t.sleep(3)
    atg.hotkey('winleft','up')
    t.sleep(0.5)
    atg.click(x=268, y=68)
    t.sleep(0.5)
    atg.click(x=298, y=364)
    t.sleep(0.5)
    atg.click(x=763, y=86)
    atg.click(x=763, y=86)
    t.sleep(0.5)

def setBrush(x,y):
    atg.click(333, 101)
    t.sleep(0.5)
    atg.click(x,y)
    t.sleep(0.5)
    atg.click(634, 106)
    t.sleep(0.5)
    atg.click(634, 180)

def draw(dr):    
    atg.click(600,300)
    atg.dragRel(-100, 200,dr)
    atg.dragRel(200,0,dr)
    atg.dragRel(-60, -130,dr)
    atg.dragRel(-110, 230,dr)

def writeLP(dr):    
    # L
    atg.moveTo(x=818, y=279)    
    atg.dragRel(0,70,dr)
    atg.dragRel(50,0,dr)
    # I
    atg.moveTo(x=880, y=279)    
    atg.dragRel(0,74,dr)
    # N
    atg.moveTo(x=895, y=348)    
    atg.dragRel(0,-71,dr)     
    atg.dragRel(50,71,dr)
    atg.dragRel(0,-75,dr)
    # K
    atg.moveTo(x=960, y=279)
    atg.dragRel(0,73,dr)
    atg.moveTo(x=962, y=313)
    atg.dragRel(35,-36, dr)
    atg.moveTo(x=962, y=314)
    atg.dragRel(35,36, dr)
    # I
    atg.moveTo(x=1010, y=279)    
    atg.dragRel(0,74,dr)
    # N
    atg.moveTo(x=1025, y=348)    
    atg.dragRel(0,-71,dr)     
    atg.dragRel(50,71,dr)
    atg.dragRel(0,-75,dr)  
    # P
    atg.moveTo(x=818, y=435)
    atg.dragRel(0,-70,dr)
    atg.dragRel(30,0,dr)
    atg.dragRel(6,10,dr)
    atg.dragRel(0,13,dr)
    atg.dragRel(-6,10,dr)
    atg.dragRel(-30,0,dr)
    # A
    atg.moveTo(862, 434)
    atg.dragRel(25,-70,dr)
    atg.dragRel(25,73,dr)
    atg.moveTo(874, 397)
    atg.dragRel(25,0,dr)
    # R
    atg.moveTo(925, 433)
    atg.dragRel(0,-70,dr)
    atg.dragRel(30,0,dr)
    atg.dragRel(6,10,dr)
    atg.dragRel(0,13,dr)
    atg.dragRel(-6,10,dr)
    atg.dragRel(-30,0,dr)
    atg.moveTo(945, 395)
    atg.dragRel(15,40,dr)
    # K
    atg.moveTo(974, 433)
    atg.dragRel(0,-73,dr)
    atg.moveTo(974, 398)
    atg.dragRel(35,-36, dr)
    atg.moveTo(974, 399)
    atg.dragRel(35,36, dr)

def moveLP(coords):
    atg.click(coords[0], coords[1])
    atg.moveTo(coords[2], coords[3])
    atg.dragRel(coords[4],coords[5], coords[6])
    atg.moveTo(coords[7],coords[8])
    atg.dragRel(coords[9],coords[10], coords[11])
    atg.click(955,200)
    
def typeCredits():
    atg.click(x=293, y=69)
    atg.moveTo(x=449, y=645)
    atg.dragRel(559,16,0.5)  
    atg.click(x=128, y=97)
    atg.click(x=128, y=97)
    t.sleep(0.5)
    atg.press('backspace')
    t.sleep(0.5)
    atg.typewrite('12')
    t.sleep(0.5)
    atg.click(452,647)
    t.sleep(0.5)
    atg.typewrite('Automated Python Script By Hirusha Fernando',0.1)
    atg.click(955,200)

def finalize():
    atg.click(130,65)
    atg.moveTo(x=242, y=240)
    atg.dragRel(817, 452, 0.2)
    atg.click(x=187, y=59)
    t.sleep(0.5)
    atg.click(x=143, y=33)
    t.sleep(0.5)
    atg.click(x=254, y=71)

def fillBlack():
    atg.click(x=268, y=68)
    t.sleep(0.5)
    atg.click(x=763, y=60)
    atg.click(x=763, y=60)    
    t.sleep(0.5)
    atg.click(x=856, y=270)

if __name__ == "__main__": 
    dr = 0.3
    paintLoad()
    setBrush(333, 200)
    draw(dr)
    draw(dr)
    setBrush(363, 180)
    writeLP(dr)
    moveLP((130,65,785,253,335,211,0.3,955,358,0,50,0.3))
    moveLP((130,65,395,269,728,364,0.3,743,444,-150,0,0.3))
    typeCredits()
    fillBlack()
    finalize()
