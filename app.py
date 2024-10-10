from tkinter import filedialog
from tkinter import *
import pygame
import os

#attributing the creator of the icons
#<a href="https://www.flaticon.com/free-icons/play-button" title="play button icons">Play button icons created by Those Icons - Flaticon</a>
#<a href="https://www.flaticon.com/free-icons/pause-play" title="pause play icons">Pause play icons created by Eid Studio - Flaticon</a>
#<a href="https://www.flaticon.com/free-icons/previous" title="previous icons">Previous icons created by shohanur.rahman13 - Flaticon</a>
#<a href="https://www.flaticon.com/free-icons/next" title="next icons">Next icons created by shohanur.rahman13 - Flaticon</a>

root = Tk()
root.title('Soul Music Player')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
	global current_song
	root.directory = filedialog.askdirectory()

	for song in os.listdir(root.directory):
		name, ext = os.path.splitext(song)
		if ext == '.mp3':
			songs.append(song)

	for song in songs:
		songlist.insert("end", song)

	songlist.selection_set(0)
	current_song = songs[songlist.curselection()[0]]

def play_music():
	global current_song, paused

	if not paused:
		pygame.mixer.music.load(os.path.join(root.directory, current_song))
		pygame.mixer.music.play()
	else:
		pygame.mixer.music.unpause()
		paused=False

def pause_music():
	global pause
	pygame.mixer.music.pause()
	paused = True

def next_music():
	global current_song, paused

	try:
		songlist.selection_clear(0, END)
		songlist.selection_set(songs.index(current_song) + 1)
		current_song = songs[songlist.curselection()[0]]
		play_music()
	except:
		pass

def prev_music():
	global current_song, paused

	try:
		songlist.selection_clear(0, END)
		songlist.selection_set(songs.index(current_song) -1)
		current_song = songs[songlist.curselection()[0]]
		play_music()
	except:
		pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play-button.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next-button.png')
prev_btn_image = PhotoImage(file='back.png')

control_frame = Frame(root)
control_frame.pack()

play_button_smaller_image = play_btn_image.subsample(18, 18)
pause_button_smaller_image = pause_btn_image.subsample(18, 18)
next_button_smaller_image = next_btn_image.subsample(18, 18)
prev_button_smaller_image = prev_btn_image.subsample(18, 18)

play_btn = Button(control_frame, image=play_button_smaller_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_button_smaller_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_button_smaller_image, borderwidth=0, command=next_music)
prev_btn = Button(control_frame, image=prev_button_smaller_image, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()