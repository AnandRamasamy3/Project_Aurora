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
wallpaper_icon_big=pygame.image.load(curent_directory+"/source/package2/icons/contacts_big.png")
wallpaper_icon_small=pygame.image.load(curent_directory+"/source/package2/icons/contacts_small.png")
my_font=pygame.font.SysFont('segoe print',21,bold=True,italic=False)
big_font=pygame.font.SysFont('segoe print',26,bold=True,italic=False)
#button_big_font=pygame.font.SysFont('segoe print',49,bold=True,italic=False)
#button_small_font=pygame.font.SysFont('segoe print',36,bold=True,italic=False)
white=(255,255,255)
black=(0,0,0)
blue=(0,0,128)
grey=(128,128,128)
def add_new_contact(wallpaper,surface,name,phone,cursor,conn):
	mode="name_mode"
	new_name=""
	new_phone=""
	get=True
	while get:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		add_new_surface=big_font.render("Add new contact",False,blue)
		get_name_surface=my_font.render("enter name:",False,blue)
		name_surface=my_font.render(str(new_name),False,blue)
		get_phone_surface=my_font.render("enter phone:",False,blue)
		phone_surface=my_font.render(str(new_phone),False,blue)
		surface.blit(add_new_surface,(250,50))
		surface.blit(get_name_surface,(200,150))
		surface.blit(name_surface,(300,200))
		surface.blit(get_phone_surface,(200,250))
		surface.blit(phone_surface,(300,300))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					get=False
				if  event.key==pygame.K_LEFT:
					if mode=="name_mode":
						if len(new_name)>0:
							temp_list=list(new_name)
							temp_list.pop()
							new_name=""
							for character in temp_list:
								new_name+=character
					if mode=="phone_mode":
						if len(new_phone)>0:
							temp_list=list(new_phone)
							temp_list.pop()
							new_phone=""
							for character in temp_list:
								new_phone+=character
				if event.key==pygame.K_a:new_name+="a"
				if event.key==pygame.K_b:new_name+="b"
				if event.key==pygame.K_c:new_name+="c"
				if event.key==pygame.K_d:new_name+="d"
				if event.key==pygame.K_e:new_name+="e"
				if event.key==pygame.K_f:new_name+="f"
				if event.key==pygame.K_g:new_name+="g"
				if event.key==pygame.K_h:new_name+="h"
				if event.key==pygame.K_i:new_name+="i"
				if event.key==pygame.K_j:new_name+="j"
				if event.key==pygame.K_k:new_name+="k"
				if event.key==pygame.K_l:new_name+="l"
				if event.key==pygame.K_m:new_name+="m"
				if event.key==pygame.K_n:new_name+="n"
				if event.key==pygame.K_o:new_name+="o"
				if event.key==pygame.K_p:new_name+="p"
				if event.key==pygame.K_q:new_name+="q"
				if event.key==pygame.K_r:new_name+="r"
				if event.key==pygame.K_s:new_name+="s"
				if event.key==pygame.K_t:new_name+="t"
				if event.key==pygame.K_u:new_name+="u"
				if event.key==pygame.K_v:new_name+="v"
				if event.key==pygame.K_w:new_name+="w"
				if event.key==pygame.K_x:new_name+="x"
				if event.key==pygame.K_y:new_name+="y"
				if event.key==pygame.K_z:new_name+="z"
				if event.key==pygame.K_1:new_phone+="1"
				if event.key==pygame.K_2:new_phone+="2"
				if event.key==pygame.K_3:new_phone+="3"
				if event.key==pygame.K_4:new_phone+="4"
				if event.key==pygame.K_5:new_phone+="5"
				if event.key==pygame.K_6:new_phone+="6"
				if event.key==pygame.K_7:new_phone+="7"
				if event.key==pygame.K_8:new_phone+="8"
				if event.key==pygame.K_9:new_phone+="9"
				if event.key==pygame.K_0:new_phone+="0"
				if event.key==pygame.K_DOWN:
					if mode=="name_mode":
						mode="phone_mode"
					elif mode=="phone_mode":
						mode="add_mode"
					else:
						mode="name_mode"
				if event.key==pygame.K_UP:
					if mode=="name_mode":
						mode="add_mode"
					elif mode=="phone_mode":
						mode="name_mode"
					else:
						mode="phone_mode"
				if event.key==pygame.K_RETURN:
					if mode=="add_mode":
						get=False
		pygame.display.update()
		ft.tick(fps)
		
	cursor.execute("INSERT into contacts values(?,?);",(str(new_name),new_phone))
	name=[]
	phone=[]
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		name.append(row[0])
		phone.append(row[1])
	conn.commit()
	return name,phone
def edit_contact(wallpaper,surface,name,phone,position,cursor,conn):
	mode="name_mode"
	new_name=name[position]
	new_phone=str(phone[position])
	get=True
	while get:
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		add_new_surface=big_font.render("Edit contact",False,blue)
		get_name_surface=my_font.render("enter name:",False,blue)
		name_surface=my_font.render(str(new_name),False,blue)
		get_phone_surface=my_font.render("enter phone:",False,blue)
		phone_surface=my_font.render(str(new_phone),False,blue)
		surface.blit(add_new_surface,(250,50))
		surface.blit(get_name_surface,(200,150))
		surface.blit(name_surface,(300,200))
		surface.blit(get_phone_surface,(200,250))
		surface.blit(phone_surface,(300,300))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE:
					get=False
				if  event.key==pygame.K_LEFT:
					if mode=="name_mode":
						if len(new_name)>0:
							temp_list=list(new_name)
							temp_list.pop()
							new_name=""
							for character in temp_list:
								new_name+=character
					if mode=="phone_mode":
						if len(new_phone)>0:
							temp_list=list(new_phone)
							temp_list.pop()
							new_phone=""
							for character in temp_list:
								new_phone+=character
				if event.key==pygame.K_a:new_name+="a"
				if event.key==pygame.K_b:new_name+="b"
				if event.key==pygame.K_c:new_name+="c"
				if event.key==pygame.K_d:new_name+="d"
				if event.key==pygame.K_e:new_name+="e"
				if event.key==pygame.K_f:new_name+="f"
				if event.key==pygame.K_g:new_name+="g"
				if event.key==pygame.K_h:new_name+="h"
				if event.key==pygame.K_i:new_name+="i"
				if event.key==pygame.K_j:new_name+="j"
				if event.key==pygame.K_k:new_name+="k"
				if event.key==pygame.K_l:new_name+="l"
				if event.key==pygame.K_m:new_name+="m"
				if event.key==pygame.K_n:new_name+="n"
				if event.key==pygame.K_o:new_name+="o"
				if event.key==pygame.K_p:new_name+="p"
				if event.key==pygame.K_q:new_name+="q"
				if event.key==pygame.K_r:new_name+="r"
				if event.key==pygame.K_s:new_name+="s"
				if event.key==pygame.K_t:new_name+="t"
				if event.key==pygame.K_u:new_name+="u"
				if event.key==pygame.K_v:new_name+="v"
				if event.key==pygame.K_w:new_name+="w"
				if event.key==pygame.K_x:new_name+="x"
				if event.key==pygame.K_y:new_name+="y"
				if event.key==pygame.K_z:new_name+="z"
				if event.key==pygame.K_1:new_phone+="1"
				if event.key==pygame.K_2:new_phone+="2"
				if event.key==pygame.K_3:new_phone+="3"
				if event.key==pygame.K_4:new_phone+="4"
				if event.key==pygame.K_5:new_phone+="5"
				if event.key==pygame.K_6:new_phone+="6"
				if event.key==pygame.K_7:new_phone+="7"
				if event.key==pygame.K_8:new_phone+="8"
				if event.key==pygame.K_9:new_phone+="9"
				if event.key==pygame.K_0:new_phone+="0"
				if event.key==pygame.K_DOWN:
					if mode=="name_mode":
						mode="phone_mode"
					elif mode=="phone_mode":
						mode="add_mode"
					else:
						mode="name_mode"
				if event.key==pygame.K_UP:
					if mode=="name_mode":
						mode="add_mode"
					elif mode=="phone_mode":
						mode="name_mode"
					else:
						mode="phone_mode"
				if event.key==pygame.K_RETURN:
					if mode=="add_mode":
						get=False
		pygame.display.update()
		ft.tick(fps)
	
	#print("position==",position)
	#print("lists",name,phone)
	cursor.execute("DELETE from contacts where name=(?) and phone=(?);",(name[position],phone[position]))
	cursor.execute("INSERT into contacts values(?,?);",(str(new_name),int(new_phone)))
	name=[]
	phone=[]
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		name.append(row[0])
		phone.append(row[1])
	conn.commit()
	return name,phone
def delete_contact(wallpaper,surface,name,phone,position,cursor,conn):
	cursor.execute("DELETE from contacts where name=(?) and phone=(?);",(name[position],phone[position]))
	name=[]
	phone=[]
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		name.append(row[0])
		phone.append(row[1])
	conn.commit()
	return name,phone
def draw_options(wallpaper,surface,pointer,position,option_position):
	#print("oooops")
	#pygame.draw.line(surface,blue,(590,(pointer+1)*50+10),(600,(pointer+1)*50+25),3)
	#pygame.draw.line(surface,blue,(590,(pointer+1)*50+40),(600,(pointer+1)*50+25),3)
	surface_add_new=my_font.render("Add new",False,grey)
	surface_edit=my_font.render("Edit",False,grey)
	surface_delete=my_font.render("Delete",False,grey)
	if 0<=pointer<=3:
		pygame.draw.rect(surface,blue,(610,50,150,200))
		if option_position==1:
			surface.blit(surface_add_new,(630,60))
			surface.blit(surface_edit,(615,110))
			surface.blit(surface_delete,(615,160))
		if option_position==2:
			surface.blit(surface_add_new,(615,60))
			surface.blit(surface_edit,(630,110))
			surface.blit(surface_delete,(615,160))
		if option_position==3:
			surface.blit(surface_add_new,(615,60))
			surface.blit(surface_edit,(615,110))
			surface.blit(surface_delete,(630,160))
	if 4<=pointer<=7:
		pygame.draw.rect(surface,blue,(610,250,50,50))
		if option_position==1:
			surface.blit(surface_add_new,(630,260))
			surface.blit(surface_edit,(615,310))
			surface.blit(surface_delete,(615,360))
		if option_position==2:
			surface.blit(surface_add_new,(615,260))
			surface.blit(surface_edit,(630,310))
			surface.blit(surface_delete,(615,360))
		if option_position==3:
			surface.blit(surface_add_new,(615,260))
			surface.blit(surface_edit,(615,310))
			surface.blit(surface_delete,(630,360))
def get_app2_big_icon():
	return wallpaper_icon_big
def get_app2_small_icon():
	return wallpaper_icon_small
def display(surface,pointer,position,current_base,current_top,name_surface,phone_surface):
	i=50
	while current_top<=current_base and i<=400 and current_top<len(name_surface):
		number_surface=my_font.render(str(current_top+1),False,(white))
		if current_top==position:
			pygame.draw.rect(surface,blue,(110,i+5,90,45))
			pygame.draw.rect(surface,blue,(210,i+5,190,45))
			pygame.draw.rect(surface,blue,(410,i+5,190,45))
			surface.blit(number_surface,(120,i))
			surface.blit(name_surface[current_top],(220,i))
			surface.blit(phone_surface[current_top],(420,i))
		if current_top!=position:
			pygame.draw.rect(surface,blue,(90,i+5,90,45))
			pygame.draw.rect(surface,blue,(190,i+5,190,45))
			pygame.draw.rect(surface,blue,(390,i+5,190,45))
			surface.blit(number_surface,(100,i))
			#print(current_top)
			surface.blit(name_surface[current_top],(200,i))
			surface.blit(phone_surface[current_top],(400,i))
		current_top+=1
		i+=50
def show_contacts(surface,wallpaper,name,phone,position,pointer,current_top,current_base,cursor,conn):
	show=True
	options=False
	option_position=1
	while show:
		name_surface=[]
		phone_surface=[]
		for i in range(0,len(name)):
			name_surface.append(my_font.render(str(name[i]),False,(white)))
			phone_surface.append(my_font.render(str(phone[i]),False,(white)))
		surface.blit(wallpaper,(0,0))
		pygame.draw.rect(surface,grey,(50,50,700,400))
		#mouse=pygame.mouse.get_pos()
		#print(mouse)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_BACKSPACE or event.key==pygame.K_LEFT:
					if options==False:
						show=False
					if options==True:
						options=False
						option_position=1
				if event.key==pygame.K_LEFT:
					options=False
					option_position=1
				if event.key==pygame.K_DOWN:
					if options==False:
						if pointer==7 and current_base<=len(name_surface)-2:
							position+=1
							current_base+=1
							current_top+=1
						else:
							pointer+=1
							position+=1
					if options==True:
						option_position+=1
				if event.key==pygame.K_UP:
					if options==False:
						pointer-=1
						position-=1
						if pointer<0:
							current_base-=1
							current_top-=1
					if options==True:
						option_position-=1
				if event.key==pygame.K_RETURN or event.key==pygame.K_RIGHT:
					if options==True:
						if option_position==1:
							name,phone=add_new_contact(wallpaper,surface,name,phone,cursor,conn)
						if option_position==2:
							name,phone=edit_contact(wallpaper,surface,name,phone,position,cursor,conn)
						if option_position==3:
							name,phone=delete_contact(wallpaper,surface,name,phone,position,cursor,conn)
					if options==False:
						options=True
				if event.key==pygame.K_q or event.key==pygame.K_x:
					pygame.quit()
					sys.exit()
		if options==True:
			draw_options(wallpaper,surface,pointer,position,option_position)
		if pointer<0:pointer=0
		if position<0:position=0
		if len(name_surface)>7:
			if pointer>7:pointer=7
		else:
			#print(len(name_surface))
			if pointer>len(name_surface):pointer=len(name_surface)
		if position>len(name_surface)-1:position=len(name_surface)-1
		if current_top<0:current_top=0
		if current_top>len(name_surface)-8 and len(name_surface)>7:
			#print("oooops")
			current_top=len(name_surface)-8
		if current_base<7:current_base=7
		if current_base>len(name_surface):current_base=len(name_surface)
		if option_position<1:option_position=1
		if option_position>3:option_position=3
		#print("oooops")
		#print("base_end==",len(name_surface), and current_base<=len(name_surface)-1)
		
		#print(current_top,pointer,position,current_base)
		display(surface,pointer,position,current_base,current_top,name_surface,phone_surface)
		
		pygame.display.update()
		ft.tick(fps)
	
	cursor.execute("UPDATE settings SET contact_pointer=("+str(pointer)+") WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_position=("+str(position)+") WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_current_top=("+str(current_top)+") WHERE wallpaper in (1,2,3,4,5,6);")
	cursor.execute("UPDATE settings SET contact_current_base=("+str(current_base)+") WHERE wallpaper in (1,2,3,4,5,6);")
	conn.commit()
def app2(surface,wallpaper,code,database_location):
	close=True
	if code==334:
		close=False
	name=[]
	phone=[]
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		#print(row)
		name.append(row[0])
		phone.append(row[1])
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		position=row[1]
		pointer=row[2]
		current_top=row[3]
		current_base=row[4]
	show_contacts(surface,wallpaper,name,phone,position,pointer,current_top,current_base,cursor,conn)
