# while(1>0):
# 	f = open("angle.txt","r")
# 	print(f.readline())
# from tkinter import *

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.grid()
#         self.master.title("Grid Manager")
#         # self.pack(fill = BOTH, expand = True)

#         # for r in range(6):
#         #     self.master.rowconfigure(r, weight=1)    
#         # for c in range(5):
#         #     self.master.columnconfigure(c, weight=1)
            

#         Frame1 = Frame(master, bg="red")
#         Frame1.grid(row = 0, column = 0)
 
#         Frame2 = Frame(master, bg="blue")
#         Frame2.grid(row =0 , column = 1)

#         Frame3 = Frame(master, bg="green")
#         Frame3.grid(row = 0, column = 2)

# root = Tk()
# root.geometry("400x200")
# # root.pack(fill = BOTH, expand = True) 
# app = Application(master=root)
# app.mainloop()
from tkinter import *

my_window = Tk()

Frame1 = Frame(my_window,width="100",height="100",bg ="red")
Frame2 = Frame(my_window,width="100",height="100",bg ="blue")

Frame1.grid(row=0,column=0)
Frame2.grid(row=0,column=1)
def update_status():
	file = open("angle.txt","r")
	k= file.readline()
	Label11 = Label(Frame1,text="2-3-4\n"+k)
	Label11.place(x=50, y=50,anchor="center")
	
update_status()





# Label12 = Label(Frame1,text="Angle")
# Label12.grid(row=1,column=1)

Label21 = Label(Frame2,text="5-6-7")
Label21.place(x=50, y=50,anchor="center")

# Label22 = Label(Frame2,text="Angle")
# Label22.grid(row=1,column=1)
Frame1.grid_propagate(0)
Frame2.grid_propagate(0)
my_window.after(1, update_status())

my_window.mainloop()