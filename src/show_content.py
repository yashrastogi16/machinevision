import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application




def male_content():
	window = tk.Tk()
	# Provide desired amount of time for which image to be displayed.
	window.after(10000, lambda: window.destroy()) # 10 seconds
	window.title("Male")
	window.geometry("500x500")
	window.configure(background='grey')
	
	path = "../images/male.jpg"

	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img = ImageTk.PhotoImage(Image.open(path))

	#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	panel = tk.Label(window, image = img)

	#The Pack geometry manager packs widgets in rows or columns.
	panel.pack(side = "bottom", fill = "both", expand = "yes")

	#Start the GUI
	window.mainloop()
	return True

def female_content():
	window = tk.Tk()
	# Provide desired amount of time for which image to be displayed.
	window.after(30000, lambda: window.destroy()) # 30 seconds
	window.title("Female")
	window.geometry("500x500")
	window.configure(background='grey')
	path = "../images/female.jpg"

	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img = ImageTk.PhotoImage(Image.open(path))

	#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	panel = tk.Label(window, image = img)

	#The Pack geometry manager packs widgets in rows or columns.
	panel.pack(side = "bottom", fill = "both", expand = "yes")

	#Start the GUI
	window.mainloop()
	return True
