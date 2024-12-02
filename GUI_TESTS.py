from tkinter import *
import time 
def play():
        
    #================================= IMAGES ========================



    img = PhotoImage(file="ICON.PNG")



    #================================= WINDOWS ========================

    win = Tk()
    win.geometry("450x450")
    win.title("YOOOOOOOOOOOO")
    win.iconphoto(True,img)
    win.config(background="GREY") 



    #================================= LABELS ========================

    f = "HELLO WORLD"
    label1 = Label(win , text = "HELLO WORLD" ,font=('',40))








    #================================= START ========================

    label1.place(width=450 , height=450 , x=0 , y=0)
    win.mainloop()

    





if __name__ == "__main__":
    play()







































