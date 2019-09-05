import pygame,sys,time,os,string
from pygame.locals import *
from os import *

pygame.init()
fps=20
ft=pygame.time.Clock()
try:
    current_directory=os.getcwd().replace(chr(92),chr(47))
    temp_list=current_directory.split(":",2)
    current_directory=temp_list[0]+":/"+temp_list[1]
except:
    current_directory=os.getcwd()
wallpaper_icon_big=pygame.image.load(current_directory+"/source/package3/sources/game1/icons/game1_big.png")
wallpaper_icon_small=pygame.image.load(current_directory+"/source/package3/sources/game1/icons/game1_small.png")
space_ship=pygame.image.load(current_directory+"/source/package3/sources/game1/icons/space_ship.png")
white=(255,255,255)
black=(0,0,0)
red=(128,0,0)
green=(0,128,0)
blue=(0,0,128)
grey=(128,128,128)
def get_app3_game1_big_icon():
	return wallpaper_icon_big
def get_app3_game1_small_icon():
	return wallpaper_icon_small
def move_bullets(bullets):
	for i in range(0,len(bullets)):
		bullets[i][1]-=20
	i=0;t=len(bullets)
	while i<t:
		if bullets[i][1]<0:
			bullets.remove(bullets[i])
		i+=1
		t=len(bullets)
	return bullets
def draw_bullets(surface,bullets):
	for i in range(0,len(bullets)):
		pygame.draw.line(surface,black,(bullets[i][0],bullets[i][1]),(bullets[i][0],bullets[i][1]+10),5)
def check_boundary(pos):
	if pos<0:pos=0
	if pos>600:pos=600
	return pos
def draw_layout(surface,name,high_score,score):
	pygame.draw.rect(surface,blue,(0,0,800,40))
	pygame.draw.line(surface,blue,(0,0),(0,500),3)
	pygame.draw.line(surface,blue,(0,500),(800,500),3)
	pygame.draw.line(surface,blue,(800,0),(800,500),3)
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface=myfont.render(name,False,white)
	surface.blit(textsurface,(100,0))
	textsurface1=myfont.render("high score:",False,white)
	textsurface2=myfont.render(str(high_score),False,white)
	surface.blit(textsurface1,(300,5))
	surface.blit(textsurface2,(420,5))
	textsurface1=myfont.render("score:",False,white)
	textsurface2=myfont.render(str(score),False,white)
	surface.blit(textsurface1,(520,5))
	surface.blit(textsurface2,(600,5))
def play_game(surface,name):
	play=True
	pos=0
	bullets=[[pos+100,340],[pos+100,320]]
	while play:
		surface.fill(green)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_q:
					pygame.quit()
					sys.exit()
				if event.key==pygame.K_BACKSPACE:
					play=False
				if event.key==pygame.K_RIGHT:
					pos+=200
				if event.key==pygame.K_LEFT:
					pos-=200
				if event.key==pygame.K_SPACE:
					i=3
					while i>2:
						for event in pygame.event.get():
							if event.type==QUIT:
								pygame.quit()
								sys.exit()
							if event.type==KEYDOWN:
								if event.key==pygame.K_q:
									pygame.quit()
									sys.exit()
								if event.key==pygame.K_SPACE:
									i=1
		pos=check_boundary(pos)
		surface.blit(space_ship,(pos,350))
		draw_bullets(surface,bullets)
		bullets=move_bullets(bullets)
		
		bullets.append([pos+100,340])
		draw_layout(surface,name,1000,200)
		pygame.display.update()
		ft.tick(fps)
def app3_game1(surface,wallpaper,code):
	get=True
	name=""
	temp=0
	myfont=pygame.font.SysFont('Segoe Print',49,bold=True,italic=False)
	myfont1=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface_game=myfont.render("space war",False,red)
	textsurface_get=myfont.render("enter your name to continue...",False,blue)
	while get:
		surface.fill(grey)
		textsurface_name=myfont.render(name,False,blue)
		surface.blit(textsurface_name,(200,270))
		surface.blit(textsurface_game,(300,70))
		surface.blit(textsurface_get,(20,200))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_a:name+="a"
				if event.key==pygame.K_b:name+="b"
				if event.key==pygame.K_c:name+="c"
				if event.key==pygame.K_d:name+="d"
				if event.key==pygame.K_e:name+="e"
				if event.key==pygame.K_f:name+="f"
				if event.key==pygame.K_g:name+="g"
				if event.key==pygame.K_h:name+="h"
				if event.key==pygame.K_i:name+="i"
				if event.key==pygame.K_j:name+="j"
				if event.key==pygame.K_k:name+="k"
				if event.key==pygame.K_l:name+="l"
				if event.key==pygame.K_m:name+="m"
				if event.key==pygame.K_n:name+="n"
				if event.key==pygame.K_o:name+="o"
				if event.key==pygame.K_p:name+="p"
				if event.key==pygame.K_q:name+="q"
				if event.key==pygame.K_r:name+="r"
				if event.key==pygame.K_s:name+="s"
				if event.key==pygame.K_t:name+="t"
				if event.key==pygame.K_u:name+="u"
				if event.key==pygame.K_v:name+="v"
				if event.key==pygame.K_w:name+="w"
				if event.key==pygame.K_x:name+="x"
				if event.key==pygame.K_y:name+="y"
				if event.key==pygame.K_z:name+="z"
				if event.key==pygame.K_RETURN:get=False
				if event.key==pygame.K_BACKSPACE:
					get=False
					temp=1
				if event.key==pygame.K_LEFT:
					temp_list=list(name)
					if len(temp_list)>0:temp_list.pop()
					name=""
					for character in temp_list:
						name+=character
		pygame.display.update()
		ft.tick(fps)
	if temp==0:
		play_game(surface,name)
