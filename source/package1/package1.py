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
wallpaper1=pygame.image.load(current_directory+'/source/package1/images/cycle_big.jpg')
wallpaper11=pygame.image.load(current_directory+'/source/package1/images/cycle_small.jpg')
wallpaper2=pygame.image.load(current_directory+'/source/package1/images/eiffel_big.jpeg')
wallpaper22=pygame.image.load(current_directory+'/source/package1/images/eiffel_small.jpeg')
wallpaper3=pygame.image.load(current_directory+'/source/package1/images/stone_big.jpeg')
wallpaper33=pygame.image.load(current_directory+'/source/package1/images/stone_small.jpeg')
wallpaper4=pygame.image.load(current_directory+'/source/package1/images/beach_big.jpeg')
wallpaper44=pygame.image.load(current_directory+'/source/package1/images/beach_small.jpeg')
wallpaper5=pygame.image.load(current_directory+'/source/package1/images/alone_big.jpg')
wallpaper55=pygame.image.load(current_directory+'/source/package1/images/alone_small.jpg')
wallpaper6=pygame.image.load(current_directory+'/source/package1/images/roller_coaster_big.jpg')
wallpaper66=pygame.image.load(current_directory+'/source/package1/images/roller_coaster_small.jpg')
white=(255,255,255)
black=(0,0,0)
def set_wallpaper(wallpaper_id,w):
	if wallpaper_id==1:
		wallpaper=w[1]
	if wallpaper_id==2:
		wallpaper=w[2]
	if wallpaper_id==3:
		wallpaper=w[3]
	if wallpaper_id==4:
		wallpaper=w[4]
	if wallpaper_id==5:
		wallpaper=[5]
	if wallpaper_id==6:
		wallpaper=[6]
	return wallpaper
def draw_menu_for_wallpaper(surface,mouse_pos):
	if mouse_pos==1:
		surface.blit(wallpaper1,(50,50))
		surface.blit(wallpaper22,(325,75))
		surface.blit(wallpaper33,(575,75))
		surface.blit(wallpaper44,(75,300))
		surface.blit(wallpaper55,(325,300))
		surface.blit(wallpaper66,(575,300))
	if mouse_pos==2:
		surface.blit(wallpaper11,(75,75))
		surface.blit(wallpaper2,(300,50))
		surface.blit(wallpaper33,(575,75))
		surface.blit(wallpaper44,(75,300))
		surface.blit(wallpaper55,(325,300))
		surface.blit(wallpaper66,(575,300))
	if mouse_pos==3:
		surface.blit(wallpaper11,(75,75))
		surface.blit(wallpaper22,(325,75))
		surface.blit(wallpaper3,(550,50))
		surface.blit(wallpaper44,(75,300))
		surface.blit(wallpaper55,(325,300))
		surface.blit(wallpaper66,(575,300))
	if mouse_pos==4:
		surface.blit(wallpaper11,(75,75))
		surface.blit(wallpaper22,(325,75))
		surface.blit(wallpaper33,(575,75))
		surface.blit(wallpaper4,(50,275))
		surface.blit(wallpaper55,(325,300))
		surface.blit(wallpaper66,(575,300))
	if mouse_pos==5:
		surface.blit(wallpaper11,(75,75))
		surface.blit(wallpaper22,(325,75))
		surface.blit(wallpaper33,(575,75))
		surface.blit(wallpaper44,(75,300))
		surface.blit(wallpaper5,(300,275))
		surface.blit(wallpaper66,(575,300))
	if mouse_pos==6:
		surface.blit(wallpaper11,(75,75))
		surface.blit(wallpaper22,(325,75))
		surface.blit(wallpaper33,(575,75))
		surface.blit(wallpaper44,(75,300))
		surface.blit(wallpaper55,(325,300))
		surface.blit(wallpaper6,(550,275))
def get_app1_big_icon():
	return wallpaper_icon_big
def get_app1_small_icon():
	return wallpaper_icon_small
def app1(surface,wallpaper,wallpaper_id,code,w):
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
				if event.key==pygame.K_RIGHT:
					mouse_pos+=1
					if mouse_pos>6:mouse_pos=1
				if event.key==pygame.K_LEFT:
					mouse_pos-=1
					if mouse_pos<1:mouse_pos=6
				if event.key==pygame.K_UP:
					if mouse_pos==4:mouse_pos=1
					if mouse_pos==5:mouse_pos=2
					if mouse_pos==6:mouse_pos=3
				if event.key==pygame.K_DOWN:
					if mouse_pos==1:mouse_pos=4
					if mouse_pos==2:mouse_pos=5
					if mouse_pos==3:mouse_pos=6
				if event.key==pygame.K_RETURN:
					conn.execute("UPDATE settings SET wallpaper=("+str(mouse_pos)+") WHERE wallpaper in (1,2,3,4,5,6);")
					wallpaper_id=mouse_pos
					wallpaper=set_wallpaper(mouse_pos,w)
					conn.commit()
					close=True
		if code==333:
			draw_menu_for_wallpaper(surface,mouse_pos)
		pygame.display.update()
		ft.tick(fps)
	return wallpaper_id