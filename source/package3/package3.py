import pygame,sys,time,os,string
import source.package3.sources.game1.game1
import source.package3.sources.game2.game2
import source.package3.sources.game3.game3
from pygame.locals import *
from source.package3.sources.game1.game1 import *
from source.package3.sources.game2.game2 import *
from source.package3.sources.game3.game3 import *
from os import *

pygame.init()
fps=20
ft=pygame.time.Clock()
curent_directory=getcwd().replace(chr(92),chr(47))
temp_list=curent_directory.split(":",2)
curent_directory=temp_list[0]+":/"+temp_list[1]
white=(255,255,255)
black=(0,0,0)
red=(128,0,0)
green=(0,128,0)
blue=(0,0,128)
icon_big_1=source.package3.sources.game1.game1.get_app3_game1_big_icon()
icon_big_2=source.package3.sources.game2.game2.get_app3_game2_big_icon()
icon_big_3=source.package3.sources.game3.game3.get_app3_game3_big_icon()
icon_small_1=source.package3.sources.game1.game1.get_app3_game1_small_icon()
icon_small_2=source.package3.sources.game2.game2.get_app3_game2_small_icon()
icon_small_3=source.package3.sources.game3.game3.get_app3_game3_small_icon()
wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package3/icons/games_big.png")
wallpaper_icon_small=pygame.image.load(curent_directory+"/source/package3/icons/games_small.png")
def draw_game_menu(surface,mouse_pos,icon_big_1,icon_big_2,icon_big_3,icon_small_1,icon_small_2,icon_small_3):
	if mouse_pos==1:
		surface.blit(icon_big_1,(200,50))
		surface.blit(icon_small_2,(437,87))
		surface.blit(icon_small_3,(637,87))
	if mouse_pos==2:
		surface.blit(icon_small_1,(237,87))
		surface.blit(icon_big_2,(400,50))
		surface.blit(icon_small_3,(637,87))
	if mouse_pos==3:
		surface.blit(icon_small_1,(237,87))
		surface.blit(icon_small_2,(437,87))
		surface.blit(icon_big_3,(600,50))
def get_app3_big_icon():
	return wallpaper_icon_big
def get_app3_small_icon():
	return wallpaper_icon_small
def app3(surface,wallpaper,code,database_location):
	if code==335:
		close=False
		conn=sqlite3.connect(database_location)
		cur=conn.cursor()
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			mouse_pos=row[7]
	while close==False:
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		draw_game_menu(surface,mouse_pos,icon_big_1,icon_big_2,icon_big_3,icon_small_1,icon_small_2,icon_small_3)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
				if event.key==pygame.K_RIGHT:
					mouse_pos+=1
					if mouse_pos>3:mouse_pos=1
				if event.key==pygame.K_LEFT:
					mouse_pos-=1
					if mouse_pos<1:mouse_pos=3
				if event.key==pygame.K_RETURN and mouse_pos==1:
					source.package3.sources.game1.game1.app3_game1(surface,wallpaper,344)
				if event.key==pygame.K_RETURN and mouse_pos==2:
					source.package3.sources.game2.game2.app3_game2(surface,wallpaper,345)
				if event.key==pygame.K_RETURN and mouse_pos==3:
					source.package3.sources.game3.game3.app3_game3(surface,database_location)
		cursor.execute("UPDATE settings SET game_menu_mouse=("+str(mouse_pos)+") WHERE wallpaper in (1,2,3,4,5,6);")
		conn.commit()
		pygame.display.update()
		ft.tick(fps)