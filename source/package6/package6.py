import pygame,sys,time,os,string
from pygame.locals import *
from os import *

pygame.init()
fps=20
ft=pygame.time.Clock()
curent_directory=getcwd().replace(chr(92),chr(47))
temp_list=curent_directory.split(":",2)
curent_directory=temp_list[0]+":/"+temp_list[1]
wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package6/icons/chat_big.png")
wallpaper_icon_small=pygame.image.load(curent_directory+"/source/package6/icons/chat_small.png")
white=(255,255,255)
black=(0,0,0)
def get_app6_big_icon():
	return wallpaper_icon_big
def get_app6_small_icon():
	return wallpaper_icon_small
def app6(surface,wallpaper,code,database_location):
	if code==338:
		close=False
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
			
		pygame.display.update()
		ft.tick(fps)