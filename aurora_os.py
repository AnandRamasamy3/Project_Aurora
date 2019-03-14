import pygame,sys,time,sqlite3
from pygame.locals import *
from math import *
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
number_font=pygame.font.SysFont('segoe print',21,bold=True,italic=False)
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
def back_to_home(wallpaper,w,database_location,lock):
	i=-200
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		wallpaper_id=row[0]
		time_type=row[11]
	wallpaper=set_wallpaper(wallpaper_id)
	while i<=100:
		surface.fill((255,255,255))
		surface.blit(wallpaper,(0,0))
		i+=40
		print_time(i,time_type)
		pygame.display.update()
		ft.tick(fps)
	home(wallpaper,database_location,lock)
def menu(wallpaper,w,database_location,lock):
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
			wallpaper_id=row[0]
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
					back_to_home(wallpaper,w,database_location,lock)
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
						try:
							source.package1.package1.app1(surface,wallpaper,333,database_location,w)
						except:
							home(wallpaper,database_location,lock)
					if mouse_pos==2:
						try:
							source.package2.package2.app2(surface,wallpaper,334,database_location)
						except:
							home(wallpaper,database_location,lock)
					if mouse_pos==3:
						try:
							source.package3.package3.app3(surface,wallpaper,335,database_location)
						except:
							home(wallpaper,database_location,lock)
					if mouse_pos==4:
						try:
							source.package4.package4.app4(surface,wallpaper,336,database_location,w)
						except:
							home(wallpaper,database_location,lock)
					if mouse_pos==5:
						try:
							source.package5.package5.app5(surface,wallpaper,337,database_location)
						except:
							home(wallpaper,database_location,lock)
					if mouse_pos==6:
						try:
							source.package6.package6.app6(surface,wallpaper,338,database_location)
						except:
							home(wallpaper,database_location,lock)
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
def transition_to_home(wallpaper,w,database_location,lock):
	i=100
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		wallpaper_id=row[0]
		time_type=row[11]
	wallpaper=set_wallpaper(wallpaper_id)
	while i>=-200:
		surface.fill((255,255,255))
		surface.blit(w[wallpaper_id],(0,0))
		i-=40
		print_time(i,time_type)
		pygame.display.update()
		ft.tick(fps)
	if lock>0:
		status=get_unlocked(w[wallpaper_id],lock)
	else:status="unlock"
	if status=="unlock":
		menu(wallpaper,w,database_location,lock)
	else:
		back_to_home(wallpaper,w,database_location,lock)
def print_analog_time(timme,words,a):
	#print("analog")
	pygame.draw.circle(surface,white,(a+80,130),80,1)
	
	twelve_surface=number_font.render("12",False,(white))
	three_surface=number_font.render("3",False,(white))
	six_surface=number_font.render("6",False,(white))
	nine_surface=number_font.render("9",False,(white))
	
	surface.blit(twelve_surface,(a+60,45))
	surface.blit(three_surface,(a+10,110))
	surface.blit(six_surface,(a+70,175))
	surface.blit(nine_surface,(a+140,110))
	
	pygame.draw.line(surface,white,(a+39.8,60.8),(a+47,73.7),1)
	pygame.draw.line(surface,white,(a+10.6,90),(a+23.6,97.6),1)
	pygame.draw.line(surface,white,(a+10.7,170),(a+23.7,162.5),1)
	pygame.draw.line(surface,white,(a+40,199),(a+47.5,186.3),1)
	pygame.draw.line(surface,white,(a+120,199),(a+112.5,186),1)
	pygame.draw.line(surface,white,(a+149,169.9),(a+136,162),1)
	pygame.draw.line(surface,white,(a+149,90),(a+136,97.5),1)
	pygame.draw.line(surface,white,(a+120,60.7),(a+112.5,73.7),1)
	
	second_angle=(360-(6*int(timme[2]))-90)*3.14/180
	minute_angle=(360-(6*int(timme[1]))-90)*3.14/180
	hour_angle=(360-(30*int(timme[0]))-90)*3.14/180
	s1=180+(60*cos(second_angle))
	s2=130+(60*sin(second_angle))
	m1=180+(62*cos(minute_angle))
	m2=130+(62*sin(minute_angle))
	h1=180+(50*cos(hour_angle))
	h2=130+(50*sin(hour_angle))
	#print(timme,s1,s2)
	pygame.draw.line(surface,white,(a+80,130),(s1,s2),1)
	pygame.draw.line(surface,white,(a+80,130),(m1,m2),2)
	pygame.draw.line(surface,white,(a+80,130),(h1,h2),3)
	
	actual_date=str(words[0])+"  "+str(words[1])+" "+str(words[2])
	date_surface=date_font.render(actual_date,False,(white))
	surface.blit(date_surface,(a+10,210))
def print_digital_time(timme,words,a):
	actual_time=str(timme[0])+":"+str(timme[1])
	actual_date=str(words[0])+"  "+str(words[1])+" "+str(words[2])
	#print(actual_time)
	time_surface=time_font.render(actual_time,False,(white))
	date_surface=date_font.render(actual_date,False,(white))
	surface.blit(time_surface,(a,80))
	surface.blit(date_surface,(a+10,165))
	#print(a+10,80)
def print_time(a,time_type):
	timee=time.ctime()
	words=timee.split(" ",4)
	#print(words)
	try:
		timme=words[3].split(":",2)
	except:
		timme=words[4].split(":",2)
	if int(timme[0])>12:
		timme[0]=str(int(timme[0])-12)
	if time_type=="digital":
		print_digital_time(timme,words,a)
	else:
		print_analog_time(timme,words,a)
def home(wallpaper,database_location,lock):
	time_type="digital"
	while True:
		surface.fill(white)
		#print("home")
		conn=sqlite3.connect(database_location)
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			wallpaper_id=row[0]
			time_type=row[11]
		wallpaper=set_wallpaper(wallpaper_id)
		surface.blit(wallpaper,(0,0))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_RETURN or event.key==pygame.K_RIGHT:
					transition_to_home(wallpaper,w,database_location,lock)
				if event.key==pygame.K_q:
					pygame.quit()
					sys.exit()
				if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
					if time_type=="digital":
						time_type="analog"
					else:
						time_type="digital"
		print_time(100,time_type)
		pygame.display.update()
		ft.tick(fps)
wallpaper=set_wallpaper(wallpaper_id)
home(wallpaper,database_location,lock)
