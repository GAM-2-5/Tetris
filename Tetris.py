import pygame
import sys
import random
import time
pygame.init()
dis = pygame.display.set_mode((640, 480))
pygame.mixer.init()
pygame.display.set_caption('Tetris') 
kraj = False
begtime=time.time()
oldtime=0
setblock=[]
for i in range(12):
    setblock.append([200+20*i,420,[50,50,50]])
for i in range(21):
    setblock.append([200,420-20*i,[50,50,50]])
for i in range(21):
    setblock.append([200+20*11,420-20*i,[50,50,50]])
score=0
font = pygame.font.Font('freesansbold.ttf', 32)
font1=pygame.font.Font('freesansbold.ttf', 16)
cool=False
new=True
rjumptime=1.00
jumptime=1.00
start=True
cher=0
jumptimejump=0.01
while start:
    dis.fill((0,0,0))
    text = font.render("TETRIS", True, (100,100,200))
    text1= font1.render("Controls:", True, (200,200,200))
    text2= font1.render("A and D for moving right and left, Q and E for rotating, S for fast fall.", True, (200,200,200))
    text3= font1.render("Press C to toggle Chernobyl mode, press F to toggle Fast mode.", True, (200,200,200))
    text4= font1.render("Press W to start.",True, (200,200,200))
    text5= font1.render("Chernobyl mode enabled.",True, (200,100,100))
    text6= font1.render("Fast mode enabled.",True,(200,100,100))

    textRect = text.get_rect()
    text1Rect= text1.get_rect()
    text2Rect= text2.get_rect()
    text3Rect= text3.get_rect()
    text4Rect= text4.get_rect()
    text5Rect= text5.get_rect()
    text6Rect= text6.get_rect()
    
    
    textRect.center = (300, 100)
    text1Rect.center = (300, 150)
    text2Rect.center = (300, 180)
    text3Rect.center = (300, 210)
    text4Rect.center = (300, 240)
    text5Rect.center = (300, 280)
    text6Rect.center = (300, 300)

    dis.blit(text, textRect)
    dis.blit(text1, text1Rect)
    dis.blit(text2, text2Rect)
    dis.blit(text3, text3Rect)
    if cher:
        dis.blit(text5, text5Rect)
    if jumptimejump==0.1:
        dis.blit(text6, text6Rect)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.display.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                start=False
                if jumptimejump==0.1:
                    pygame.mixer.quit()
                    pygame.mixer.init(55000)
                if cher:
                    music="sounds\Chernobil_theme.mp3"
                    pygame.mixer.music.load("sounds\Chernobil_theme.mp3")
                    pygame.mixer.music.play(-1)
                else:
                    music="sounds\Tetris_theme.mp3"
                    pygame.mixer.music.load("sounds\Tetris_theme.mp3")
                    pygame.mixer.music.play(-1)
            if event.key==pygame.K_c:
                cher=not cher
            if event.key==pygame.K_f:
                if jumptimejump==0.01:
                    jumptimejump=0.1
                else:
                    jumptimejump=0.01

        
def gameover():
    global kraj
    for i in setblock:
        if i[0]==300 and i[1]==80:
            kraj=True
            if cher:
                pygame.mixer.music.load("sounds\Chernobil_death.mp3")
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("sounds\Tetris_death.wav")
                pygame.mixer.music.play()
            time.sleep(2.7)
            pygame.display.quit()
            sys.exit()
        
def clear():
    global cool
    global rjumptime
    global jumptime
    global score
    cleared=[]
    for i in range(20):
        b=0
        for t in setblock:
            if t[1]==400-20*(19-i):
                b+=1
        if b==12:
            cleared.append(400-20*(19-i))

    if len(cleared)==4:
        if cool:
            score+=1200
        else:
            score+=800
        cool=True
    else:
        cool=False
        score+=len(cleared)*100
    for i in cleared:
        rjumptime-=rjumptime*jumptimejump
        jumptime=rjumptime
        c=[]
        for n in range(len(setblock)):
            if setblock[n][1]==i and setblock[n][0]!=200 and setblock[n][0]!=420:
                c.append(setblock[n])
        for n in c:
            setblock.remove(n)
        for n in range(len(setblock)):
            if setblock[n][1]<i and setblock[n][0]!=200 and setblock[n][0]!=420:
                setblock[n][1]+=20
def checkrot(side):
    global coords
    global setblocks
    global rot
    fakecoords=coords[0:2]
    if shape==1:#O
        color=[100,100,20]
        fakecoords.extend([coords[0]+20,coords[1],coords[0]+20,coords[1]+20,coords[0],coords[1]+20])
    if shape==2:#I
        color=[0,100,100]
        fakecoords.extend([coords[0]+20*crot[1]+20*crot[3],coords[1]+20*crot[0]+20*crot[2],coords[0]-20*crot[1]-20*crot[3],coords[1]-20*crot[0]-20*crot[2],coords[0]-40*crot[1]-40*crot[3],coords[1]-40*crot[0]+40*crot[2]])
    if shape==3:#Z
        color=[100,0,0]
        fakecoords.extend([coords[0]+20*crot[0]+20*crot[2],coords[1]-20*crot[1]-20*crot[3],coords[0]+20*crot[1]+20*crot[3],coords[1]+20*crot[0]+20*crot[2],coords[0]-20*crot[0]+20*crot[1]-20*crot[2]+20*crot[3],coords[1]+20*crot[0]+20*crot[1]+20*crot[2]+20*crot[3]])
    if shape==4:#S
        color=[20,100,20]
        fakecoords.extend([coords[0]-20*crot[0]+20*crot[2],coords[1]+20*crot[1]+20*crot[3],coords[0]+20*crot[1]+20*crot[3],coords[1]+20*crot[0]-20*crot[2],coords[0]+20*crot[0]+20*crot[1]+20*crot[3]-20*crot[2],coords[1]+20*crot[0]-20*crot[1]-20*crot[2]-20*crot[3]])
    if shape==5:#L
        color=[150,100,0]
        fakecoords.extend([coords[0]+20*crot[1]-20*crot[3],coords[1]-20*crot[0]-20*crot[2],coords[0]-20*crot[1]+20*crot[3],coords[1]+20*crot[0]+20*crot[2],coords[0]+20*crot[0]-20*crot[1]-20*crot[2]+20*crot[3],coords[1]+20*crot[0]+20*crot[1]-20*crot[2]-20*crot[3]])
    if shape==6:#J
        color=[0,10,100]
        fakecoords.extend([coords[0]-20*crot[1]+20*crot[3],coords[1]-20*crot[0]+20*crot[2],coords[0]+20*crot[1]-20*crot[3],coords[1]+20*crot[0]-20*crot[2],coords[0]-20*crot[0]+20*crot[2]-20*crot[1]+20*crot[3],coords[1]+20*crot[0]-20*crot[2]-20*crot[1]+20*crot[3]])
    if shape==7:#T
        color=[100,10,100]
        fakecoords.extend([coords[0]+20*crot[0]-20*crot[2],coords[1]-20*crot[1]+20*crot[3],coords[0]-20*crot[1]+20*crot[3],coords[1]+20*crot[0]-20*crot[2],coords[0]-20*crot[0]+20*crot[2],coords[1]+20*crot[1]-20*crot[3]])
    for i in range(4):
        for t in setblock:
            if fakecoords[i*2]==t[0] and fakecoords[i*2+1]==t[1]:
                global yes
                yes=False
    

def check():
    global new
    global setblock
    global coords
    for i in range(4):
        if coords[i*2+1]==400:
            setblock.append([coords[0],coords[1],color])
            setblock.append([coords[2],coords[3],color])
            setblock.append([coords[4],coords[5],color])
            setblock.append([coords[6],coords[7],color])
            new=True
            break
        for t in setblock:
            if coords[i*2]==t[0] and coords[i*2+1]+20==t[1]:
                setblock.append([coords[0],coords[1],color])
                setblock.append([coords[2],coords[3],color])
                setblock.append([coords[4],coords[5],color])
                setblock.append([coords[6],coords[7],color])
                new=True
                break
        if new:
            break
def move(gej, gae):
    global coords
    global color
    coords=[coords[0],coords[1]]
    if shape==1:#O
        color=[100,100,20]
        coords.extend([coords[0]+20,coords[1],coords[0]+20,coords[1]+20,coords[0],coords[1]+20])
    if shape==2:#I
        color=[0,100,100]
        coords.extend([coords[0]+20*rot[1]+20*rot[3],coords[1]+20*rot[0]+20*rot[2],coords[0]-20*rot[1]-20*rot[3],coords[1]-20*rot[0]-20*rot[2],coords[0]-40*rot[1]-40*rot[3],coords[1]-40*rot[0]+40*rot[2]])
    if shape==3:#Z
        color=[100,0,0]
        coords.extend([coords[0]+20*rot[0]+20*rot[2],coords[1]-20*rot[1]-20*rot[3],coords[0]+20*rot[1]+20*rot[3],coords[1]+20*rot[0]+20*rot[2],coords[0]-20*rot[0]+20*rot[1]-20*rot[2]+20*rot[3],coords[1]+20*rot[0]+20*rot[1]+20*rot[2]+20*rot[3]])
    if shape==4:#S
        color=[20,100,20]
        coords.extend([coords[0]-20*rot[0]+20*rot[2],coords[1]+20*rot[1]+20*rot[3],coords[0]+20*rot[1]+20*rot[3],coords[1]+20*rot[0]-20*rot[2],coords[0]+20*rot[0]+20*rot[1]+20*rot[3]-20*rot[2],coords[1]+20*rot[0]-20*rot[1]-20*rot[2]-20*rot[3]])
    if shape==5:#L
        color=[150,100,0]
        coords.extend([coords[0]+20*rot[1]-20*rot[3],coords[1]-20*rot[0]-20*rot[2],coords[0]-20*rot[1]+20*rot[3],coords[1]+20*rot[0]+20*rot[2],coords[0]+20*rot[0]-20*rot[1]-20*rot[2]+20*rot[3],coords[1]+20*rot[0]+20*rot[1]-20*rot[2]-20*rot[3]])
    if shape==6:#J
        color=[0,10,100]
        coords.extend([coords[0]-20*rot[1]+20*rot[3],coords[1]-20*rot[0]+20*rot[2],coords[0]+20*rot[1]-20*rot[3],coords[1]+20*rot[0]-20*rot[2],coords[0]-20*rot[0]+20*rot[2]-20*rot[1]+20*rot[3],coords[1]+20*rot[0]-20*rot[2]-20*rot[1]+20*rot[3]])
    if shape==7:#T
        color=[100,10,100]
        coords.extend([coords[0]+20*rot[0]-20*rot[2],coords[1]-20*rot[1]+20*rot[3],coords[0]-20*rot[1]+20*rot[3],coords[1]+20*rot[0]-20*rot[2],coords[0]-20*rot[0]+20*rot[2],coords[1]+20*rot[1]-20*rot[3]])
while not kraj:
    
    if new:
        gameover()
        clear()
        global coords
        coords=[300,60]
        global rot
        rot=[1,0,0,0]
        color=[0,0,0]
        shape=random.choice([1,2,3,4,5,6,7])
        move(coords, rot)
        new=False

    if time.time()-begtime>oldtime+jumptime:
        check()
        coords[1]+=20
        oldtime=time.time()-begtime
        move(coords, rot)
        
            
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            kraj=True
            pygame.mixer.music.stop()
            pygame.display.quit()
            sys.exit()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_p:
                jumptime=rjumptime
            if event.key==pygame.K_s:
                jumptime=rjumptime
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                jumptime=1000000
            if event.key==pygame.K_s:
                jumptime=0.1
            if event.key==pygame.K_q:
                yes=True
                crot=list(rot)
                for i in range(len(crot)):
                    if crot[i]==1:
                        crot[i]=0
                        crot[i-1]=1
                        break
                checkrot(2)
                if yes:
                    for i in range(len(rot)):
                        if rot[i]==1:
                            rot[i]=0
                            rot[i-1]=1
                            break
                    move(coords, rot)
            if event.key==pygame.K_e:
                yes=True
                crot=list(rot)
                for i in range(len(crot)):
                    if crot[i]==1:
                        if i==3:
                            crot[3]=0
                            crot[0]=1
                        else:
                            crot[i]=0
                            crot[i+1]=1
                        break
                checkrot("asda")
                if yes:
                    for i in range(len(rot)):
                        if rot[i]==1:
                            if i==3:
                                rot[3]=0
                                rot[0]=1
                            else:
                                rot[i]=0
                                rot[i+1]=1
                            break
                    move(coords, rot)
            if event.key==pygame.K_a:
                yes=True
                for t in setblock:
                    for i in range(4):
                        if coords[i*2]-20==t[0] and coords[i*2+1]==t[1]:
                            yes=False
                if yes:
                    coords[0]-=20
                    move(coords, rot)
            if event.key==pygame.K_d:
                yes=True
                for t in setblock:
                    for i in range(4):
                        if coords[i*2]+20==t[0] and coords[i*2+1]==t[1]:
                            yes=False
                if yes:
                    coords[0]+=20
                    move(coords, rot)
    dis.fill((0,0,0))

    for t in setblock:
            pygame.draw.rect(dis, t[2],[t[0],t[1],20,20])
    text = font.render(str(score), True, (200,200,200))
    textRect = text.get_rect()
    textRect.center = (100, 200)
    dis.blit(text, textRect)
    
    pygame.draw.rect(dis, color,[coords[0],coords[1],20,20], cher*50)
    pygame.draw.rect(dis, color,[coords[2],coords[3],20,20], cher*50)
    pygame.draw.rect(dis, color,[coords[4],coords[5],20,20], cher*50)
    pygame.draw.rect(dis, color,[coords[6],coords[7],20,20], cher*50)
    pygame.display.update()
