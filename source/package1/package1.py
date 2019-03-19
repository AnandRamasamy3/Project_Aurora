import pygame,sys,time,os,string
import sqlite3
from pygame.locals import *
from os import *

pygame.init()
fps=20
ft=pygame.time.Clock()
current_directory=getcwd().replace(chr(92),chr(47))
temp_list=current_directory.split(":",2)
current_directory=temp_list[0]+":/"+temp_list[1]
conn=sqlite3.connect(current_directory+'/source/database/aos.db')
cur=conn.cursor()
wallpaper_icon_big=pygame.image.load(current_directory+"/source/package1/icons/icon_for_wallpaper_big.png")
wallpaper_icon_small=pygame.image.load(current_directory+"/source/package1/icons/icon_for_wallpaper_small.png")
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
def get_app1_big_icon():
	return wallpaper_icon_big
def get_app1_small_icon():
	return wallpaper_icon_small
def draw_layout(surface):
	pygame.draw.rect(surface,grey,(50,50,700,400))
	
	pygame.draw.line(surface,black,(50,50),(750,50),3)
	pygame.draw.line(surface,black,(50,50),(50,450),3)
	pygame.draw.line(surface,black,(750,50),(750,450),3)
	pygame.draw.line(surface,black,(50,450),(750,450),3)
	
	pygame.draw.line(surface,black,(137,50),(137,450),3)
	pygame.draw.line(surface,black,(225,50),(225,450),3)
	pygame.draw.line(surface,black,(312,50),(312,450),3)
	pygame.draw.line(surface,black,(400,50),(400,450),3)
	
	pygame.draw.line(surface,black,(400,50),(400,450),3)
	
def app1(surface,wallpaper,code,database_location,w):
	if code==333:
		close=False
		mouse_pos=1
	while close==False:
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
		#draw_layout(surface)
		pygame.display.update()
		ft.tick(fps)