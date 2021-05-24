# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:35:15 2021

@author: USER
"""

import pygame
from pygame.locals import*
import time
import random






life = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\LIFE123.PNG')
player = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerNomal.png')

Normal = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerNomal.png')
Board = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\normal.png')
Nails = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\nails.png')


RIGHT1 = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerR1.png')
RIGHT2 = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerR2.png')

LEFT1 = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerL1.png')
LEFT2= pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerL2.png')
wall =  pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\wall.png')
ceil = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\ceiling.png')

ImgList = {'life'  : life, 'player' : player, 'Normal' : Normal, 'Board' : Board,
           'Nails' : Nails, 'RIGHT1' :RIGHT1, 'RIGHT2' : RIGHT2,'LEFT1' : LEFT1, 
           'LEFT2' : LEFT2, 'wall'  : wall,  'ceil' :ceil}


             



pygame.init()


FPS = 100#設定幀數
width, height = 480, 640 #把螢幕長寬變數丟進去
screen = pygame.display.set_mode((width, height))#設定螢幕長寬
pygame.display.set_caption('小朋友下樓梯')#設定視窗名稱




lef = 0#判斷往左兩個動作的參數
rig = 0#判斷往右兩個動作的參數
keys =  [False, False, False, False]#設定上下左右判定的list
CountF = 0#設定往下樓層的變數
playerpos = [240, 320]#自訂XY
Xlist  = []#紀錄每個X值
Ylist  = []#紀錄每個y值
Kindlist = []#紀錄每個板子的種類
count = 0#刷新板子亂數
count2 = 0
# 宣告 font 文字物件

# 渲染方法會回傳 surface 物件

# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
Platform = {0 :Board , 1 : Nails}#各種種類的平台的dict


class player:
    def __init__(self, X, Y, HP, img):
        self.X = X
        self.Y = Y
        self.HP = HP
        self.img = img
        
    
    
player1 = player(240, 320, 12,ImgList['player'] )



while 1:
    
    ##環境設定
    screen.fill((0, 0, 0))#把畫布塗黑
    timing = pygame.time.get_ticks()#設定一個計時器 單位為毫秒
    time = timing % 2500#計時器每2.5秒歸0
    boardtime = timing % 8000#板子計時器每8秒歸0
    print(boardtime)#測試秒數到哪裡 程式有沒有預期跑
    if time < 3:
        CountF += 1
    
    head_font = pygame.font.SysFont(None, 60)#設定大小60的標題框框
    text_surface = head_font.render('B%04dF'%CountF, True, (121, 255, 121))#設定標題的字跟顏色
    screen.blit(text_surface, (300, 25))#讓標題印在畫布300,25的地方
    # 5 - clear the screen before drawing it again
    #screen.fill((0, 0, 0))
    # 6 - draw the screen elements
    for x in range (80, 700, 100):#設定牆壁 以及生命值
        screen.blit(ImgList['wall'],  (0, x))
        screen.blit(ImgList['wall'],  (460, x))
    screen.blit(player1.img, (player1.X, player1.Y))
    screen.blit(ImgList['ceil'],  (20, 80))
    screen.blit(ImgList['ceil'],  (55, 80))
    screen.blit(ImgList['life'],  (10, 0))
    
    screen.blit(ImgList['Board'],  (270,350))
    
    
    playerRect  = pygame.Rect(240, 320, 29, 29)#測試碰撞的程式
    BoardRect   = pygame.Rect(270, 350, 95, 16)
    if (pygame.Rect.colliderect(playerRect, BoardRect) == 1 ):
         print('碰撞')
    else: 
        print('沒有碰撞')
    
    
    kind = random.randint(0, 1)
    Kindlist.append(kind)
    X = random.randint(0, 350)
    Xlist.append(X)
    Y = 600
    Ylist.append(Y)
    if (boardtime < 3800) :
       screen.blit(Platform[Kindlist[count]], (Xlist[count], Ylist[count]))
       Ylist[count] -= 0.5
    #count += 1
    elif(3900 > boardtime >3800):
        count += 1
     
    if (2000 < boardtime < 5800) :
       screen.blit(Platform[Kindlist[count2]], (Xlist[count2], Ylist[count2]))
       Ylist[count2] -= 0.5    
    elif( 5801< boardtime < 5900) :
       count2 += 1
       
       
    if (4001 < boardtime < 7800) :
       screen.blit(Platform[Kindlist[count]], (Xlist[count], Ylist[count]))
       Ylist[count] -= 0.5    
    elif (7801 < boardtime < 7900) :
       count += 1
       
    if (boardtime > 6000 or boardtime < 1800 ) :
       screen.blit(Platform[Kindlist[count2]], (Xlist[count2], Ylist[count2]))
       Ylist[count2] -= 0.5    
    elif (1801 < boardtime < 1900):
       count2 += 1
       
       
       
    pygame.display.flip()#環境更新
   
   
    '''
    if (time == 3500):
        kind = random.randint(0, 1)
        Kindlist.append(kind)
        X = random.randint(0, 450)
        Xlist.append(X)
        Y = 600
        Ylist.append(Y)
        screen.blit(Platform[Kindlist[count]], (Xlist[count], Ylist[count]))
        Ylist[count] -= 0.5
    #screen.blit(Kindlist[count[0]], (Xlist[count[0]], Ylist[count[0]]))
        count += 1    
    
    kind = random.randint(0, 1)
    X = random.randint(0, 450)
    boardposX.append(X)
    screen.blit(Platform[kind], (boardposX[count], 440) )
    count += 1
    '''
    # 7 - update the screen
    
    # 8 - loop through the events
   
    

    #操控角色    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)       

        
        if event.type == pygame.KEYDOWN:#左
            if event.key==K_LEFT:
                keys[2]=True
                
        
        if event.type == pygame.KEYDOWN:#右
            if event.key==K_RIGHT:
                keys[3]=True
                
                
        
        if event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                keys[2]=False
               
                player1.img = ImgList['Normal']
                
        if event.type == pygame.KEYUP:
            if event.key==K_RIGHT:
                keys[3]=False
                
                player1.img = ImgList['Normal']
        #print( f'上{keys[0]} 下{keys[1]} 左{keys[2]} 右{keys[3]}') 測試有無Work
        
      
               
            
        if keys[2] == True and lef % 2 == 0: #兩張跑步圖片 
            player1.img = ImgList['LEFT1']
            player1.X -= 8
            lef += 1
        elif keys[2] == True and lef % 2 == 1: 
            player1.img = ImgList['LEFT2']
            player1.X -= 8
            lef += 1
        
        elif keys[3] == True and rig % 2 == 0:
            player1.img = ImgList['RIGHT1']
            player1.X  += 8
            rig += 1 
        elif keys[3] == True and rig % 2 == 1: 
            player1.img = ImgList['RIGHT2']
            player1.X += 8
            rig += 1

       
    
    


    #playerImg = pygame.image.load('C:\\Users\\USER\\PythonGame\\LittleKids\\assets\\playerNomal.png')  

#if __name__ == '__main__':