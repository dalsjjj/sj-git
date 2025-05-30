from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    arrows = {
        37: '왼쪽 화살표',
        38: '위쪽 화살표',
        39: '오른쪽 화살표',
        40: '아래쪽 화살표'
    }
    messagebox.showinfo("키보드 이벤트", f"눌린 키 : Shift + {arrows[event.keycode]}")

window = Tk()

window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()
