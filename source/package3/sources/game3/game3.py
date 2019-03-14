import pygame,sys,time,os,string,random,sqlite3
from pygame.locals import *
from os import *
from random import *

pygame.init()
fps=20
ft=pygame.time.Clock()
curent_directory=getcwd().replace(chr(92),chr(47))
temp_list=curent_directory.split(":",2)
curent_directory=temp_list[0]+":/"+temp_list[1]
wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package3/sources/game3/icons/game3_big.png")
wallpaper_icon_small=pygame.image.load(curent_directory+"/source/package3/sources/game3/icons/game3_small.png")
white=(255,255,255)
black=(0,0,0)
red=(128,0,0)
blue=(0,0,128)
green=(0,128,0)
gray=(128,128,128)
def get_app3_game3_big_icon():
	return wallpaper_icon_big
def get_app3_game3_small_icon():
	return wallpaper_icon_small
def draw_layout(surface,name):
	pygame.draw.rect(surface,blue,(0,0,800,40))
	pygame.draw.line(surface,blue,(0,0),(0,500),3)
	pygame.draw.line(surface,blue,(0,500),(800,500),3)
	pygame.draw.line(surface,blue,(800,0),(800,500),3)
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface=myfont.render(name,False,white)
	surface.blit(textsurface,(100,0))
def show_high_score(high_score,surface):
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface1=myfont.render("high score:",False,white)
	textsurface2=myfont.render(str(high_score),False,white)
	surface.blit(textsurface1,(300,5))
	surface.blit(textsurface2,(420,5))
def show_score(score,surface):
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface1=myfont.render("score:",False,white)
	textsurface2=myfont.render(str(score),False,white)
	surface.blit(textsurface1,(520,5))
	surface.blit(textsurface2,(600,5))
def check_for_self_out(worm,food,status,position):
	for i in range(1,len(worm)):
		if worm[i][0]==worm[0][0] and worm[i][1]==worm[0][1] and position>=20:
			status="out"
	return status
def feed_the_worm(worm,food,status):
	check=0
	if food[0]==worm[0][0] or food[0]+20==worm[0][0] or food[0]-20==worm[0][0]:
		check=1
	if check==1:
		if food[1]==worm[0][1] or food[1]+20==worm[0][1] or food[1]-20==worm[0][1]:
			check=2
	if check==2:
		worm.append(food)
		status="check_food"
	return worm,food,status
def show_food(food,surface):
	pygame.draw.rect(surface,green,(food[0],food[1],20,20))
def select_food(status,worm):
	food=[1,1]
	while food[0]%20!=0 and (food[0] not in worm):
		food[0]=randint(1,780)
	while food[1]%20!=0 and (food[1] not in worm):
		food[1]=randint(40,480)
	return food,"feeded"
def check_boundary(worm):
	for i in range(0,len(worm)):
		for j in range(0,len(worm[i])):
			if j==0:
				if worm[i][j]<0:worm[i][j]=780
				if worm[i][j]>=800:worm[i][j]=0
			if j==1:
				if worm[i][j]<40:worm[i][j]=480
				if worm[i][j]>=500:worm[i][j]=40
	return worm
def show_worm(worm,surface):
	for i,j in worm:
		pygame.draw.rect(surface,blue,(i,j,20,20))
def move_worm(worm,direction):
	worm1=worm
	len_i=len(worm)
	while(len_i>1):
		len_i-=1
		len_j=len(worm[len_i])
		while(len_j>=0):
			len_j-=1
			worm[len_i][len_j]=worm[len_i-1][len_j]
	if direction=="right":
		worm[0][0]+=20
	if direction=="left":
		worm[0][0]-=20
	if direction=="up":
		worm[0][1]-=20
	if direction=="down":
		worm[0][1]+=20
	return worm
def game3(surface,name,database_location):
	worm=[[200,160],[220,160],[240,160],[260,160]]#]
	position=1
	direction="right"
	status="check_food"
	play=True
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from high_scores;")
	for row in cursor:
		high_score=row[0]
	while play:
		surface.fill(gray)
		position+=1
		score=(len(worm)-4)*100
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_RIGHT and direction!="left":
					direction="right"
				if event.key==pygame.K_LEFT and direction!="right":
					direction="left"
				if event.key==pygame.K_UP and direction!="down":
					direction="up"
				if event.key==pygame.K_DOWN and direction!="up":
					direction="down"
				if event.key==pygame.K_BACKSPACE:
					play=False
				if event.key==pygame.K_SPACE:
					i=1
					while(i<2):
						for event in pygame.event.get():
							if event.type==QUIT:
								pygame.quit()
								sys.exit()
							if event.type==KEYDOWN:
								if event.key==pygame.K_SPACE:
									i=3
		draw_layout(surface,name)
		if status=="check_food":food,status=select_food(status,worm)
		if status=="out":
			play=False
		worm=move_worm(worm,direction)
		show_food(food,surface)
		show_worm(worm,surface)
		worm=check_boundary(worm)
		worm,food,status=feed_the_worm(worm,food,status)
		status=check_for_self_out(worm,food,status,position)
		show_score(score,surface)
		show_high_score(high_score,surface)
		pygame.display.update()
		ft.tick(fps)
	if score>high_score:
		cursor.execute("UPDATE high_scores SET snake=("+str(score)+") WHERE snake>100;")
		print(score)
		conn.commit()
def app3_game3(surface,database_location):
	get=True
	name=""
	temp=0
	myfont=pygame.font.SysFont('Segoe Print',49,bold=True,italic=False)
	myfont1=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface_game=myfont.render("WORM",False,red)
	textsurface_get=myfont.render("enter your name to continue...",False,blue)
	while get:
		surface.fill(gray)
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
		game3(surface,name,database_location)
