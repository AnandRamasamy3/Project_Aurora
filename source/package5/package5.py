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
wallpaper_icon_big=pygame.image.load(current_directory+"/source/package5/icons/notes_big.png")
wallpaper_icon_small=pygame.image.load(current_directory+"/source/package5/icons/notes_small.png")
my_font=pygame.font.SysFont('segoe print',21,bold=True,italic=False)
big_font=pygame.font.SysFont('segoe print',32,bold=True,italic=False)
white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
blue=(0,0,128)
def get_app5_big_icon():
	return wallpaper_icon_big
def get_app5_small_icon():
	return wallpaper_icon_small
def decrypt_note(note,pin):
	pin=list(pin)
	notes=list(note)
	i=0
	j=0
	while i<=3 and j<len(notes):
		temp=notes[j]
		notes[j]=chr(ord(temp)-int(pin[i]))
		if i==3:
			i=0
		i+=1
		j+=1
	note=""
	for i in notes:
		note+=i
	return note
def encrypt_note(note,pin):
	pin=list(pin)
	notes=list(note)
	i=0
	j=0
	while i<=3 and j<len(notes):
		temp=notes[j]
		notes[j]=chr(ord(temp)+int(pin[i]))
		if i==3:
			i=0
		i+=1
		j+=1
	note=""
	for i in notes:
		note+=i
	return note
def get_pin(surface,wallpaper):
	close=False
	pin=""
	while close==False:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		if len(pin)>4:
			temp_list=list(pin)
			temp_list.pop()
			pin=""
			for character in temp_list:
				pin+=character
		get_pin_surface=my_font.render("Enter security key",False,blue)
		pin_surface=my_font.render(pin,False,blue)
		surface.blit(get_pin_surface,(200,150))
		surface.blit(pin_surface,(250,200))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					pin=""
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
				if event.key==pygame.K_RETURN and len(pin)==4:
					close=True
			
		pygame.display.update()
		ft.tick(fps)
	return pin
def display_notes(wallpaper,surface,title,note,pin):
	close=False
	note=decrypt_note(note,pin)
	#print(len(note))
	while close==False:
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		note_surface=my_font.render(str(note),False,blue)
		title_surface=big_font.render(str(title),False,blue)
		mouse=pygame.mouse.get_pos()
		#print(mouse)
		surface.blit(title_surface,(300,60))
		surface.blit(note_surface,(100,140))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
			
		pygame.display.update()
		ft.tick(fps)
def add_new_notes(wallpaper,surface,cursor,conn,pin):
	close=False
	note=title=temp=""
	mode="title_mode"
	note=""
	while close==False:
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		title_surface=big_font.render(str(title),False,blue)
		note_surface=my_font.render(str(note),False,blue)
		surface.blit(title_surface,(300,60))
		surface.blit(note_surface,(100,140))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
				if event.key==pygame.K_UP:
					mode="title_mode"
				if event.key==pygame.K_DOWN:
					mode="note_mode"
				if  event.key==pygame.K_LEFT:
					if mode=="title_mode":
						if len(title)>0:
							temp_list=list(title)
							temp_list.pop()
							title=""
							for character in temp_list:
								title+=character
					if mode=="note_mode":
						if len(note)>0:
							temp_list=list(note)
							temp_list.pop()
							note=""
							for character in temp_list:
								note+=character
				if event.key==pygame.K_a:temp="a"
				if event.key==pygame.K_b:temp="b"
				if event.key==pygame.K_c:temp="c"
				if event.key==pygame.K_d:temp="d"
				if event.key==pygame.K_e:temp="e"
				if event.key==pygame.K_f:temp="f"
				if event.key==pygame.K_g:temp="g"
				if event.key==pygame.K_h:temp="h"
				if event.key==pygame.K_i:temp="i"
				if event.key==pygame.K_j:temp="j"
				if event.key==pygame.K_k:temp="k"
				if event.key==pygame.K_l:temp="l"
				if event.key==pygame.K_m:temp="m"
				if event.key==pygame.K_n:temp="n"
				if event.key==pygame.K_o:temp="o"
				if event.key==pygame.K_p:temp="p"
				if event.key==pygame.K_q:temp="q"
				if event.key==pygame.K_r:temp="r"
				if event.key==pygame.K_s:temp="s"
				if event.key==pygame.K_t:temp="t"
				if event.key==pygame.K_u:temp="u"
				if event.key==pygame.K_v:temp="v"
				if event.key==pygame.K_w:temp="w"
				if event.key==pygame.K_x:temp="x"
				if event.key==pygame.K_y:temp="y"
				if event.key==pygame.K_z:temp="z"
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
				if event.key==pygame.K_SPACE:temp=" "
		if len(temp)>0:
			if mode=="title_mode":
				title+=temp
			if mode=="note_mode":
				note+=temp
			temp=""
		pygame.display.update()
		ft.tick(fps)
	note=encrypt_note(note,pin)
	cursor.execute("INSERT into notes values(?,?);",(note,title))
	conn.commit()
def display_titles(surface,note_titles,position):
	i=50
	j=0
	note_titles.append("add new note")
	while j<len(note_titles):
		if j==len(note_titles)-1:
			note_number_surface=big_font.render("+",False,grey)
		else:
			note_number_surface=my_font.render(str(j+1),False,grey)
		note_title_surface=my_font.render(str(note_titles[j]),False,grey)
		if position==j:
			pygame.draw.rect(surface,blue,(140,i+5,80,45))
			pygame.draw.rect(surface,blue,(240,i+5,300,45))
			surface.blit(note_number_surface,(150,i+5))
			surface.blit(note_title_surface,(250,i+5))
		else:
			pygame.draw.rect(surface,blue,(90,i+5,80,45))
			pygame.draw.rect(surface,blue,(190,i+5,300,45))
			surface.blit(note_number_surface,(100,i+5))
			surface.blit(note_title_surface,(200,i+5))
		j+=1
		i+=50
def app5(surface,wallpaper,code,database_location):
	if code==337:
		close=False
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		position=row[8]
	while close==False:
		notes=[]
		note_titles=[]
		cursor=conn.execute("SELECT * from notes;")
		for row in cursor:
			notes.append(row[0])
			note_titles.append(row[1])
		surface.fill(white)
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					close=True
				if event.key==pygame.K_DOWN:
					position+=1
				if event.key==pygame.K_UP:
					position-=1
				if event.key==pygame.K_RETURN:
					if position<len(notes):
						pin=get_pin(surface,wallpaper)
						if len(pin)==4:
							display_notes(wallpaper,surface,note_titles[position],notes[position],pin)
					elif position==len(notes):
						pin=get_pin(surface,wallpaper)
						if len(pin)==4:
							add_new_notes(wallpaper,surface,cursor,conn,pin)
		if position>len(note_titles):position=len(note_titles)
		if position<0:position=0
		display_titles(surface,note_titles,position)
		pygame.display.update()
		ft.tick(fps)
