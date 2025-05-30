from tkinter import *

window = Tk()
window.title("이미지")

# 첫 번째 이미지
photo1 = PhotoImage(file="C:\\Users\\mmssj\\OneDrive\\바탕 화면\\gif.gif")
label1 = Label(window, image=photo1)
label1.pack(side=LEFT)

# 두 번째 이미지
photo2 = PhotoImage(file="C:\\Users\\mmssj\\OneDrive\\바탕 화면\\gif2.gif")
label2 = Label(window, image=photo2)
label2.pack(side=LEFT)

window.mainloop()