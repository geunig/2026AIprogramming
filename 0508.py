'''
from tkinter import *

btnList = [None] * 9
fnameList = ['surf.gif']
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0,0
num = 0

window = Tk()
window.geometry("700x400")

for i in range(0,9):
    photoList[i] = PhotoImage(file = "surf.gif")
    btnList[i] = Button(window, image = photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 220
    xPos = 0
    yPos += 114

window.mainloop()
'''

from tkinter import *
from tkinter import messagebox

def Enter(event):
    messagebox.showinfo('마우스','마우스 인식됨.')

window = Tk()
window.bind("<Enter>", Enter)

window.mainloop()
