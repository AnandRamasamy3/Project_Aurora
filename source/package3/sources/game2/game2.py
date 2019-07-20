import pygame,sys,time,os,string
from pygame.locals import *
from os import *

pygame.init()
surface=pygame.display.set_mode((600+200,600-100),0,32)
fps=20
ft=pygame.time.Clock()
pygame.display.set_caption('Towers of Hanoi')
try:
    current_directory=os.getcwd().replace(chr(92),chr(47))
    temp_list=current_directory.split(":",2)
    current_directory=temp_list[0]+":/"+temp_list[1]
except:
    current_directory=os.getcwd()
wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package3/sources/game2/icons/game2_big.png")
wallpaper_icon_small=pygame.image.load(curent_directory+"/source/package3/sources/game2/icons/game2_small.png")
white=(255,255,255)
black=(0,0,0)
blue=(0,0,128)
red=(128,0,0)
green=(0,128,0)
grey=(128,128,128)
def get_app3_game2_big_icon():
	return wallpaper_icon_big
def get_app3_game2_small_icon():
	return wallpaper_icon_small
def show_moves(surface,moves,min_possible):
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface_moves1=myfont.render("moves:",False,white)
	textsurface_moves2=myfont.render(str(moves),False,white)
	textsurface_min1=myfont.render("minimum possible moves:",False,white)
	textsurface_min2=myfont.render(str(min_possible),False,white)
	surface.blit(textsurface_moves1,(630,0))
	surface.blit(textsurface_moves2,(700,0))
	surface.blit(textsurface_min1,(250,0))
	surface.blit(textsurface_min2,(520,0))
def draw_pointer(surface,pos):
	if pos==1:
		pygame.draw.line(surface,blue,(200,460),(180,480),3)
		pygame.draw.line(surface,blue,(200,460),(220,480),3)
	if pos==2:
		pygame.draw.line(surface,blue,(400,460),(380,480),3)
		pygame.draw.line(surface,blue,(400,460),(420,480),3)
	if pos==3:
		pygame.draw.line(surface,blue,(600,460),(580,480),3)
		pygame.draw.line(surface,blue,(600,460),(620,480),3)
def select_disc(i,j,k):
	temp=[0,0]
	if i==1:temp[0]=190;temp[1]=20
	if i==2:temp[0]=180;temp[1]=40
	if i==3:temp[0]=170;temp[1]=60
	if i==4:temp[0]=160;temp[1]=80
	if i==5:temp[0]=150;temp[1]=100
	if i==6:temp[0]=140;temp[1]=120
	if i==7:temp[0]=130;temp[1]=140
	if i==8:temp[0]=120;temp[1]=160
	
	if j==1:temp[0]=390;temp[1]=20
	if j==2:temp[0]=380;temp[1]=40
	if j==3:temp[0]=370;temp[1]=60
	if j==4:temp[0]=360;temp[1]=80
	if j==5:temp[0]=350;temp[1]=100
	if j==6:temp[0]=340;temp[1]=120
	if j==7:temp[0]=330;temp[1]=140
	if j==8:temp[0]=320;temp[1]=160
	
	if k==1:temp[0]=590;temp[1]=20
	if k==2:temp[0]=580;temp[1]=40
	if k==3:temp[0]=570;temp[1]=60
	if k==4:temp[0]=560;temp[1]=80
	if k==5:temp[0]=550;temp[1]=100
	if k==6:temp[0]=540;temp[1]=120
	if k==7:temp[0]=530;temp[1]=140
	if k==8:temp[0]=520;temp[1]=160
	#print(i,j,k,temp)
	return temp
def check_pos(pos):
	if pos<1:pos=1
	if pos>3:pos=3
	return pos
def draw_discs(surface,plate1,plate2,plate3,spoon,pos):
	if spoon!=0:
		if pos==1:
			plate=select_disc(spoon,99,99)
			pygame.draw.rect(surface,red,(plate[0],50,plate[1],35))
		if pos==2:
			plate=select_disc(99,spoon,99)
			pygame.draw.rect(surface,red,(plate[0],50,plate[1],35))
		if pos==3:
			plate=select_disc(99,99,spoon)
			pygame.draw.rect(surface,red,(plate[0],50,plate[1],35))
	n=360;i=0
	if len(plate1)>0:
		while i<len(plate1):
			#print("\n\n",i,"\n\n")
			plate=select_disc(plate1[i],99,99)
			pygame.draw.rect(surface,red,(plate[0],n,plate[1],35))
			n-=40
			i+=1
	n=360;i=0
	if len(plate2)>0:
		while i<len(plate2):
			#print("\n\n",i,"\n\n")
			plate=select_disc(99,plate2[i],99)
			pygame.draw.rect(surface,red,(plate[0],n,plate[1],35))
			n-=40
			i+=1
	n=360;i=0
	if len(plate3)>0:
		while i<len(plate3):
			#print("\n\n",i,"\n\n")
			plate=select_disc(99,99,plate3[i])
			pygame.draw.rect(surface,red,(plate[0],n,plate[1],35))
			n-=40
			i+=1
def draw_layout(surface,name):
	pygame.draw.line(surface,black,(100,405),(700,405),10)
	pygame.draw.line(surface,blue,(200,100),(200,400),10)
	pygame.draw.line(surface,blue,(400,100),(400,400),10)
	pygame.draw.line(surface,blue,(600,100),(600,400),10)
	pygame.draw.rect(surface,blue,(0,0,800,40))
	pygame.draw.line(surface,blue,(0,0),(0,500),3)
	pygame.draw.line(surface,blue,(0,500),(800,500),3)
	pygame.draw.line(surface,blue,(800,0),(800,500),3)
	myfont=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface=myfont.render(name,False,white)
	surface.blit(textsurface,(100,0))
def play_game2(name,surface,no_of_discs):
	play=True
	n=no_of_discs
	pos=2
	spoon=moves=0
	plate1=[]
	plate2=[]
	plate3=[]
	win=[]
	min_possible=(2**no_of_discs)-1
	myfont=pygame.font.SysFont('Segoe Print',100,bold=True,italic=False)
	textsurface_win=myfont.render("you won",False,green)
	while n>=1:
		plate1.append(n)
		win.append(n)
		n-=1
	while play:
		surface.fill(grey)
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
					pos+=1
				if event.key==pygame.K_LEFT:
					pos-=1
				if event.key==pygame.K_UP:
					if spoon==0:
						if pos==1 and len(plate1)>0:
							spoon=plate1[len(plate1)-1]
							plate1.pop()
						if pos==2 and len(plate2)>0:
							spoon=plate2[len(plate2)-1]
							plate2.pop()
						if pos==3 and len(plate3)>0:
							spoon=plate3[len(plate3)-1]
							plate3.pop()
				if event.key==pygame.K_DOWN:
					if spoon!=0:
						if pos==1:
							if (len(plate1)>0 and spoon<plate1[len(plate1)-1]) or len(plate1)==0:
								plate1.append(spoon)
								spoon=0
								moves+=1
						if pos==2:
							if (len(plate2)>0 and spoon<plate2[len(plate2)-1]) or len(plate2)==0:
								plate2.append(spoon)
								spoon=0
								moves+=1
						if pos==3:
							if (len(plate3)>0 and spoon<plate3[len(plate3)-1]) or len(plate3)==0:
								plate3.append(spoon)
								spoon=0
								moves+=1
		pos=check_pos(pos)
		#print(plate1,plate2,plate3)
		draw_layout(surface,name)
		show_moves(surface,moves,min_possible)
		draw_pointer(surface,pos)
		draw_discs(surface,plate1,plate2,plate3,spoon,pos)
		if plate3==win and len(win)==no_of_discs:
			surface.blit(textsurface_win,(200,200))
		pygame.display.update()
		ft.tick(fps)
def get_no_of_discs(name,surface):
	myfont=pygame.font.SysFont('Segoe Print',49,bold=True,italic=False)
	textsurface_get=myfont.render("enter no of discs...",False,blue)
	get=True
	no_of_discs=""
	temp=0
	while get:
		surface.fill(grey)
		if len(no_of_discs)>0:
			if int(no_of_discs)<3:no_of_discs="3"
			if int(no_of_discs)>8:no_of_discs="8"
		textsurface_discs=myfont.render(no_of_discs,False,blue)
		surface.blit(textsurface_discs,(200,300))
		surface.blit(textsurface_get,(100,200))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_0:no_of_discs+="0"
				if event.key==pygame.K_1:no_of_discs+="1"
				if event.key==pygame.K_2:no_of_discs+="2"
				if event.key==pygame.K_3:no_of_discs+="3"
				if event.key==pygame.K_4:no_of_discs+="4"
				if event.key==pygame.K_5:no_of_discs+="5"
				if event.key==pygame.K_6:no_of_discs+="6"
				if event.key==pygame.K_7:no_of_discs+="7"
				if event.key==pygame.K_8:no_of_discs+="8"
				if event.key==pygame.K_9:no_of_discs+="9"
				if event.key==pygame.K_RETURN and len(no_of_discs)>0:
					no_of_discs=int(no_of_discs)
					get=False
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
		play_game2(name,surface,no_of_discs)
def app3_game2(surface,wallpaper,code):
	get=True
	name=""
	temp=0
	myfont=pygame.font.SysFont('Segoe Print',49,bold=True,italic=False)
	myfont1=pygame.font.SysFont('Segoe Print',21,bold=True,italic=False)
	textsurface_game=myfont.render("Towers Of Hanoi",False,red)
	textsurface_get=myfont.render("enter your name to continue...",False,blue)
	while get:
		surface.fill(grey)
		textsurface_name=myfont.render(name,False,blue)
		surface.blit(textsurface_name,(200,270))
		surface.blit(textsurface_game,(200,70))
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
		get_no_of_discs(name,surface)
#app3_game2(surface,wallpaper,346)
