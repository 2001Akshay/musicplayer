from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog


def addsongs():
        temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
        for s in temp_song:
          s=s.replace("/home/akshay/Downloads/Music/","")
          songs_list.insert(END,s)
        
            
def deletesong():
        curr_song=songs_list.curselection()
        songs_list.delete(curr_song[0])
    
    
def Play():
        song=songs_list.get(ACTIVE)
        song=f'/home/akshay/Downloads/Music/{song}'
        mixer.music.load(song)
        mixer.music.play()


def Pause():
        mixer.music.pause()


def Stop():
        mixer.music.stop()
        songs_list.selection_clear(ACTIVE)



def Resume():
        mixer.music.unpause()


def Previous():
    previous_one=songs_list.curselection()
    previous_one=previous_one[0]-1
    temp2=songs_list.get(previous_one)
    temp2=f'/home/akshay/Downloads/Music/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)

def Next():
    next_one=songs_list.curselection()
    next_one=next_one[0]+1 
    temp=songs_list.get(next_one)
    temp=f'/home/akshay/Downloads/Music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)


root=Tk()
root.title(' 𝓡𝓗𝓨𝓣𝓗𝓜 ') 
mixer.init()

songs_list=Listbox(root,selectmode=SINGLE,bg="white",fg="darkviolet",font=('arial',15),height=12,width=47,selectbackground="cyan",selectforeground="black")
songs_list.grid(columnspan=9)
 
defined_font = font.Font(family='RADIOLAND')

play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

previous_button=Button(root,text="Prev",width =7,command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

next_button=Button(root,text="Next",width =7,command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


mainloop()
