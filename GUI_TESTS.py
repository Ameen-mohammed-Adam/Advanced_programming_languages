from imported import *



main_window = Tk()
main_window.title("AIRPORT PARKING SYSTEM")
img = PhotoImage(file="ICON.png")
main_window.iconphoto(TRUE , img)
main_window.resizable(False,False)
main_window.geometry("450x450+400+150")
main_window.config(background="black")

header_label = Label(main_window , text="Welcome To OUR\nAIRPORT PARKING SYSTEM" , font=('', 15 , 'bold') ,
                      foreground="white" , width=37 , height=6 , background="black" , pady=40)
New_Account = Button(main_window , text="NEW USER" , background="#007bff" , foreground="WHITE" )
Old_Account = Button(main_window , text="OLD USER" , background="#007bff")
Employee = Button(main_window , text="Employees Only", background="#007bff")
close = Button(main_window , text="EXIT" , width=10 , height=1 , background="CYAN" , command=exit)


header_label.place(x = 0 , y = 0)
New_Account.place(x = 300 , y = 300)
close.place(x = 40 , y = 400)
Employee.place(x = 40 , y = 400)
main_window.mainloop()

if __name__ == "__main__":
    pass