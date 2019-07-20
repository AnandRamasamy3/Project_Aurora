import pygame,sys,time,os,string,sqlite3
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
wallpaper_icon_big=pygame.image.load(current_directory+"/source/package4/icons/lock_big.png")
wallpaper_icon_small=pygame.image.load(current_directory+"/source/package4/icons/lock_small.png")
wallpaper1=pygame.image.load(current_directory+'/source/package4/images/cycle_big.jpg')
wallpaper11=pygame.image.load(current_directory+'/source/package4/images/cycle_small.jpg')
wallpaper2=pygame.image.load(current_directory+'/source/package4/images/eiffel_big.jpeg')
wallpaper22=pygame.image.load(current_directory+'/source/package4/images/eiffel_small.jpeg')
wallpaper3=pygame.image.load(current_directory+'/source/package4/images/stone_big.jpeg')
wallpaper33=pygame.image.load(current_directory+'/source/package4/images/stone_small.jpeg')
wallpaper4=pygame.image.load(current_directory+'/source/package4/images/beach_big.jpeg')
wallpaper44=pygame.image.load(current_directory+'/source/package4/images/beach_small.jpeg')
wallpaper5=pygame.image.load(current_directory+'/source/package4/images/alone_big.jpg')
wallpaper55=pygame.image.load(current_directory+'/source/package4/images/alone_small.jpg')
wallpaper6=pygame.image.load(current_directory+'/source/package4/images/roller_coaster_big.jpg')
wallpaper66=pygame.image.load(current_directory+'/source/package4/images/roller_coaster_small.jpg')
big_font=pygame.font.SysFont('segoe print',64,bold=True,italic=False)
small_font=pygame.font.SysFont('segoe print',24,bold=True,italic=False)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,128)
grey=(128,128,128)
def get_app4_big_icon():
	return wallpaper_icon_big
def get_app4_small_icon():
	return wallpaper_icon_small
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
		wallpaper=w[5]
	if wallpaper_id==6:
		wallpaper=w[6]
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
def reset_os(database_location,cursor,conn):
	cursor.execute("UPDATE settings SET wallpaper=('4') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_position=('0') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_pointer=('0') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_current_top=('0') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_current_base=('1') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET lock=('0') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET main_menu_mouse=('1') WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET game_menu_mouse=('1') WHERE wallpaper in (1,2,3,4,5,6);")
	
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		cursor.execute("DELETE from contacts where name=(?) and phone=(?);",(row[0],row[1]))
	cursor.execute("INSERT into contacts values('ram','8765432100');")
	
	cursor=conn.execute("SELECT * from notes;")
	for row in cursor:
		cursor.execute("DELETE from notes where note=(?) and title=(?);",(row[0],row[1]))
	cursor.execute("INSERT into contacts values('aurora is an operating system with user friendly interface','aurora');")
	
	cursor.execute("UPDATE high_scores SET snake=('200') WHERE snake>0;")
	
	conn.commit()
	
	pygame.quit()
	sys.exit()
def get_pin(surface,wallpaper,database_location):
	close=False
	pin=""
	while close==False:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		get_pin_surface=small_font.render("Enter pin",False,blue)
		pin_surface=small_font.render(pin,False,blue)
		surface.blit(get_pin_surface,(200,150))
		surface.blit(pin_surface,(250,200))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					pin="0000"
					close=True
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
				if event.key==pygame.K_RETURN:
					close=True
			
		pygame.display.update()
		ft.tick(fps)
	return pin
def get_new_pin(surface,wallpaper,pin,database_location):
	mode="old"
	old=new=""
	get=True
	while get:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		get_old_surface=small_font.render("enter old pin:",False,blue)
		old_surface=small_font.render(old,False,blue)
		get_new_surface=small_font.render("enter new pin:",False,blue)
		new_surface=small_font.render(new,False,blue)
		surface.blit(get_old_surface,(200,150))
		surface.blit(old_surface,(300,200))
		surface.blit(get_new_surface,(200,250))
		surface.blit(new_surface,(300,300))
		temp=""
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					get=False
				if  event.key==pygame.K_LEFT:
					if mode=="old":
						if len(old)>0:
							temp_list=list(old)
							temp_list.pop()
							old=""
							for character in temp_list:
								old+=character
					if mode=="new":
						if len(new)>0:
							temp_list=list(new)
							temp_list.pop()
							new=""
							for character in temp_list:
								new+=character
				if event.key==pygame.K_1:temp="1"
				if event.key==pygame.K_2:temp="2"
				if event.key==pygame.K_3:temp="3"
				if event.key==pygame.K_4:temp="4"
				if event.key==pygame.K_5:temp="5"
				if event.key==pygame.K_6:temp="6"
				if event.key==pygame.K_7:temp="7"
				if event.key==pygame.K_8:temp="8"
				if event.key==pygame.K_9:temp="9"
				if event.key==pygame.K_0:temp="0"
				if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
					if mode=="old":mode="new"
					else:mode="old"
				if event.key==pygame.K_RETURN and old==str(pin):
					if mode=="new":
						get=False
		if len(temp)>0:
			if mode=="old":old+=temp
			else:new+=temp
		pygame.display.update()
		ft.tick(fps)
	return new
def check_mouse_pos(mouse_pos):
	if mouse_pos<1:mouse_pos=3
	if mouse_pos>3:mouse_pos=1
	return mouse_pos
def to_set_lock(surface,wallpaper,database_location):
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		pin=row[5]
	if pin==0:pin=get_pin(surface,wallpaper,database_location)
	else:pin=get_new_pin(surface,wallpaper,pin,database_location)
	cursor.execute("UPDATE settings SET lock=("+str(pin)+") WHERE wallpaper in (1,2,3,4,5,6);")
	conn.commit()
def to_check_reset(surface,wallpaper,database_location):
	confirmation=0
	confirmation_surface1=small_font.render("Do you want to reset completely..??",False,blue)
	confirmation_surface2=small_font.render("enter to reset..",False,blue)
	while confirmation==0:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		surface.blit(confirmation_surface1,(150,100))
		surface.blit(confirmation_surface2,(230,150))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					confirmation=2
				if event.key==pygame.K_RETURN:
					confirmation=1
		pygame.display.update()
		ft.tick(fps)
	if confirmation==1:
		conn=sqlite3.connect(database_location)
		cur=conn.cursor()
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			lock=row[5]
		if lock==0:
			reset_os(database_location,cursor,conn)
		else:
			pin=get_pin(surface,wallpaper,database_location)
			if pin==str(lock):
				reset_os(database_location,cursor,conn)
def draw_options(surface,mouse_pos,setting_surface,lock_surface,reset_surface,wallpaper_surface):
	surface.blit(setting_surface,(250,60))
	if mouse_pos==1:
		pygame.draw.rect(surface,blue,(190,205,250,45))
		pygame.draw.rect(surface,blue,(140,255,250,45))
		pygame.draw.rect(surface,blue,(140,305,250,45))
		surface.blit(wallpaper_surface,(200,200))
		surface.blit(lock_surface,(150,250))
		surface.blit(reset_surface,(150,300))
	if mouse_pos==2:
		pygame.draw.rect(surface,blue,(140,205,250,45))
		pygame.draw.rect(surface,blue,(190,255,250,45))
		pygame.draw.rect(surface,blue,(140,305,250,45))
		surface.blit(wallpaper_surface,(150,200))
		surface.blit(lock_surface,(200,250))
		surface.blit(reset_surface,(150,300))
	if mouse_pos==3:
		pygame.draw.rect(surface,blue,(140,205,250,45))
		pygame.draw.rect(surface,blue,(140,255,250,45))
		pygame.draw.rect(surface,blue,(190,305,250,45))
		surface.blit(wallpaper_surface,(150,200))
		surface.blit(lock_surface,(150,250))
		surface.blit(reset_surface,(200,300))
def change_wallpaper(surface,wallpaper,database_location,w):
	close=False
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		mouse_pos=row[9]
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
					conn.execute("UPDATE settings SET wallpaper_position=("+str(mouse_pos)+") WHERE wallpaper in (1,2,3,4,5,6);")
					wallpaper_id=mouse_pos
					wallpaper=set_wallpaper(mouse_pos,w)
					conn.commit()
					close=True
		draw_menu_for_wallpaper(surface,mouse_pos)
		pygame.display.update()
		ft.tick(fps)
def app4(surface,wallpaper,code,database_location,w):
	if code==336:
		close=False
		setting_surface=big_font.render("Settings",False,blue)
		wallpaper_surface=small_font.render("change wallpaper",False,white)
		lock_surface=small_font.render("Lock Screen",False,white)
		reset_surface=small_font.render("Reset OS",False,white)
		conn=sqlite3.connect(database_location)
		cur=conn.cursor()
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			mouse_pos=row[10]
	while close==False:
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		cursor=conn.execute("SELECT * from settings;")
		for row in cursor:
			wallpaper_id=row[0]
		wallpaper=set_wallpaper(wallpaper_id,w)
		pygame.draw.rect(surface,grey,(50,50,700,400))
		draw_options(surface,mouse_pos,setting_surface,lock_surface,reset_surface,wallpaper_surface)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
				if event.key==pygame.K_UP:
					mouse_pos-=1
				if event.key==pygame.K_DOWN:
					mouse_pos+=1
				if event.key==pygame.K_RETURN:
					if mouse_pos==1:change_wallpaper(surface,wallpaper,database_location,w)
					if mouse_pos==2:to_set_lock(surface,wallpaper,database_location)
					if mouse_pos==3:to_check_reset(surface,wallpaper,database_location)
		mouse_pos=check_mouse_pos(mouse_pos)
		pygame.display.update()
		ft.tick(fps)
	conn.execute("UPDATE settings SET setting_menu_mouse_pos=("+str(mouse_pos)+") WHERE wallpaper in (1,2,3,4,5,6);")
	conn.commit()
