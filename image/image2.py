from tkinter import *
import random

#전역 변수
btnList = [None] * 9
fnameList = [
    "cat1.gif", "cat2.gif", "cat3.gif",
    "cat4.gif", "cat5.gif", "cat6.gif",
    "cat7.gif", "cat8.gif", "cat9.gif"
]

random.shuffle(fnameList)  

photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

#메인 코드
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:\\Users\\mmssj\\OneDrive\\바탕 화면\\cat/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
