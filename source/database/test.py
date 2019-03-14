import sqlite3
conn=sqlite3.connect('aos.db')
cursor=conn.execute("SELECT * from notes;")
for row in cursor:
	note=row[0]
'''
cur=conn.cursor()
print(name)
print(score)
d=[[0,0],[0,2],[1,0]]

d.append([2,1])

#print(d)
from random import *
print (randint(1,99))
name="anand"
list_name=list(name)
list_name.pop()
print(list_name)
namee=""
for c in list_name:
	namee+=c
print(namee)
bb=[[1,2,3,4,5],[3,4,6],[2,8,1],]
i=0;t=len(bb)
while i<t:
	print("\n\n",bb,"\n\n")
	if bb[i][1]==4:
		bb.remove(bb[i])
	i+=1
	t=len(bb)
print(bb)'''

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
note=encrypt_note(note,"9688")
cursor.execute("INSERT into notes values(?,?);",(note,"ram"))
conn.commit()