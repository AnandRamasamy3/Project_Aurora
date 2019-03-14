import pygame,sys,time,sqlite3
from pygame.locals import *
import source.package1.package1
import source.package2.package2
import source.package3.package3
import source.package4.package4
import source.package5.package5
import source.package6.package6
from source.package1.package1 import *
from source.package2.package2 import *
from source.package3.package3 import *
from source.package4.package4 import *
from source.package5.package5 import *
from source.package6.package6 import *

pygame.init()
fps=20
ft=pygame.time.Clock()
surface=pygame.display.set_mode((800,500),0,32)
pygame.display.set_caption('aurora_OS')
current_directory=getcwd().replace(chr(92),chr(47))
temp_list=current_directory.split(":",2)
current_directory=temp_list[0]+":/"+temp_list[1]
#wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package3/icons/games_big.png")
w=[0,1,0,10,10,000,0]
database_location=current_directory+'/source/database/aos.db'
w[1]=wallpaper1=pygame.image.load(current_directory+'/source/wallpapers/cycle.jpg')
w[2]=wallpaper2=pygame.image.load(current_directory+'/source/wallpapers/eiffel.jpeg')
w[3]=wallpaper3=pygame.image.load(current_directory+'/source/wallpapers/stone.jpeg')
w[4]=wallpaper4=pygame.image.load(current_directory+'/source/wallpapers/beach.jpeg')
w[5]=wallpaper5=pygame.image.load(current_directory+'/source/wallpapers/alone.jpg')
w[6]=wallpaper6=pygame.image.load(current_directory+'/source/wallpapers/roller_coaster.jpg')
conn=sqlite3.connect(database_location)
cur=conn.cursor()
cursor=conn.execute("SELECT * from settings;")
for row in cursor:
	wallpaper_id=row[0]
	lock=row[5]
time_font=pygame.font.SysFont('segoe print',64,bold=True,italic=False)
date_font=pygame.font.SysFont('segoe print',24,bold=True,italic=False)
white=(255,255,255)
black=(0,0,0)
def set_wallpaper(wallpaper_id):
	if wallpaper_id==1:
		wallpaper=wallpaper1
	if wallpaper_id==2:
		wallpaper=wallpaper2
	if wallpaper_id==3:
		wallpaper=wallpaper3
	if wallpaper_id==4:
		wallpaper=wallpaper4
	if wallpaper_id==5:
		wallpaper=wallpaper5
	if wallpaper_id==6:
		wallpaper=wallpaper6
	return wallpaper
def draw_menu_icons(mouse_pos,big_1,big_2,big_3,big_4,big_5,big_6,small_1,small_2,small_3,small_4,small_5,small_6):
	if mouse_pos==1:
		surface.blit(big_1,(200,50))
		surface.blit(small_2,(437,87))
		surface.blit(small_3,(637,87))
		surface.blit(small_4,(237,287))
		surface.blit(small_5,(437,287))
		surface.blit(small_6,(637,297))
	if mouse_pos==2:
		surface.blit(small_1,(237,87))
		surface.blit(big_2,(400,50))
		surface.blit(small_3,(637,87))
		surface.blit(small_4,(237,287))
		surface.blit(small_5,(437,287))
		surface.blit(small_6,(637,297))
	if mouse_pos==3:
		surface.blit(small_1,(237,87))
		surface.blit(small_2,(437,87))
		surface.blit(big_3,(600,50))
		surface.blit(small_4,(237,287))
		surface.blit(small_5,(437,287))
		surface.blit(small_6,(637,297))
	if mouse_pos==4:
		surface.blit(small_1,(237,87))
		surface.blit(small_2,(437,87))
		surface.blit(small_3,(637,87))
		surface.blit(big_4,(200,250))
		surface.blit(small_5,(437,287))
		surface.blit(small_6,(637,297))
	if mouse_pos==5:
		surface.blit(small_1,(237,87))
		surface.blit(small_2,(437,87))
		surface.blit(small_3,(637,87))
		surface.blit(small_4,(237,287))
		surface.blit(big_5,(400,250))
		surface.blit(small_6,(637,297))
	if mouse_pos==6:
		surface.blit(small_1,(237,87))
		surface.blit(small_2,(437,87))
		surface.blit(small_3,(637,87))
		surface.blit(small_4,(237,287))
		surface.blit(small_5,(437,287))
		surface.blit(big_6,(600,270))
def back_to_home(wallpaper,wallpaper_id,w,database_location,lock):
	i=-200
	while i<=100:
		surface.fill((255,255,255))
		surface.blit(wallpaper,(0,0))
		i+=40
		print_time(i)
		pygame.display.update()
		ft.tick(fps)
	home(wallpaper_id,w,database_location,lock)
def menu(wallpaper,wallpaper_id,w,database_location,lock):
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		mouse_pos=row[6]
	while True:
		#print("menu")conn=sqlite3.connect(database_location)
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			lock=row[5]
		surface.fill(white)
		wallpaper=set_wallpaper(wallpaper_id)
		surface.blit(wallpaper,(0,0))
		big_1=source.package1.package1.get_app1_big_icon()
		big_2=source.package2.package2.get_app2_big_icon()
		big_3=source.package3.package3.get_app3_big_icon()
		big_4=source.package4.package4.get_app4_big_icon()
		big_5=source.package5.package5.get_app5_big_icon()
		big_6=source.package6.package6.get_app6_big_icon()
		small_1=source.package1.package1.get_app1_small_icon()
		small_2=source.package2.package2.get_app2_small_icon()
		small_3=source.package3.package3.get_app3_small_icon()
		small_4=source.package4.package4.get_app4_small_icon()
		small_5=source.package5.package5.get_app5_small_icon()
		small_6=source.package6.package6.get_app6_small_icon()
		draw_menu_icons(mouse_pos,big_1,big_2,big_3,big_4,big_5,big_6,small_1,small_2,small_3,small_4,small_5,small_6)
		cursor.execute("UPDATE settings SET main_menu_mouse=("+str(mouse_pos)+") WHERE wallpaper in (1,2,3,4,5,6);")
		conn.commit()
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					back_to_home(wallpaper,wallpaper_id,w,database_location,lock)
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
					if mouse_pos==1:
						wallpaper_id=source.package1.package1.app1(surface,wallpaper,wallpaper_id,333,w)
					if mouse_pos==2:
						source.package2.package2.app2(surface,wallpaper,334,database_location)
					if mouse_pos==3:
						source.package3.package3.app3(surface,wallpaper,335,database_location)
					if mouse_pos==4:
						source.package4.package4.app4(surface,wallpaper,336,database_location)
					if mouse_pos==5:
						source.package5.package5.app5(surface,wallpaper,337,database_location)
					if mouse_pos==6:
						source.package6.package6.app6(surface,wallpaper,338,database_location)
		pygame.display.update()
		ft.tick(fps)
def get_unlocked(wallpaper,lock):
	pin=""
	status="lock"
	while status=="lock":
		surface.blit(wallpaper,(0,0))
		get_pin_surface=time_font.render("enter PIN",False,white)
		surface.blit(get_pin_surface,(200,100))
		temp=""
		if len(pin)>0:
			for i in range(0,len(pin)):
				temp+="*"
		pin_surface=time_font.render(temp,False,white)
		surface.blit(pin_surface,(250,200))
		#print(status,pin,temp)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					status="nope"
				if  event.key==pygame.K_LEFT:
					if len(pin)>0:
						temp_list=list(pin)
						temp_list.pop()
						pin=""
						for character in temp_list:
							pin+=character
				if event.key==pygame.K_1:pin+="1"
				if event.key==pygame.K_2:pin+="2"
				if event.key==pygame.K_3:pin+="3"
				if event.key==pygame.K_4:pin+="4"
				if event.key==pygame.K_5:pin+="5"
				if event.key==pygame.K_6:pin+="6"
				if event.key==pygame.K_7:pin+="7"
				if event.key==pygame.K_8:pin+="8"
				if event.key==pygame.K_9:pin+="9"
				if event.key==pygame.K_0:pin+="0"
		if pin==str(lock):
			status="unlock"
		pygame.display.update()
		ft.tick(fps)
	return status
def transition_to_home(wallpaper,wallpaper_id,w,database_location,lock):
	i=100
	while i>=-200:
		surface.fill((255,255,255))
		surface.blit(w[wallpaper_id],(0,0))
		i-=40
		print_time(i)
		pygame.display.update()
		ft.tick(fps)
	if lock>0:
		status=get_unlocked(w[wallpaper_id],lock)
	else:status="unlock"
	if status=="unlock":
		menu(wallpaper,wallpaper_id,w,database_location,lock)
	else:
		back_to_home(wallpaper,wallpaper_id,w,database_location,lock)
def print_time(a):
	timee=time.ctime()
	words=timee.split(" ",4)
	#print(words)
	try:
		timme=words[3].split(":",2)
	except:
		timme=words[4].split(":",2)
	if int(timme[0])>12:
		timme[0]=str(int(timme[0])-12)
	actual_time=str(timme[0])+":"+str(timme[1])
	actual_date=str(words[0])+"  "+str(words[1])+" "+str(words[2])
	#print(actual_time)
	time_surface=time_font.render(actual_time,False,(white))
	date_surface=date_font.render(actual_date,False,(white))
	#print(a+10,80)
	surface.blit(time_surface,(a,80))
	surface.blit(date_surface,(a+10,165))
def home(wallpaper_id,w,database_location,lock):
	while True:
		#print("home")
		surface.fill(white)
		wallpaper=set_wallpaper(wallpaper_id)
		surface.blit(wallpaper,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_RETURN or event.key==pygame.K_RIGHT:
					transition_to_home(default_wallpaper,wallpaper_id,w,database_location,lock)
				if event.key==pygame.K_q:
					pygame.quit()
					sys.exit()
		print_time(100)
		pygame.display.update()
		ft.tick(fps)
default_wallpaper=set_wallpaper(wallpaper_id)
home(wallpaper_id,w,database_location,lock)