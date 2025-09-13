import tkinter as tk

root=tk.Tk()
root.title("Test App")



mainframe=tk.LabelFrame(root,text="Main Frame")
mainframe.grid(row=2,column=0)
lbl=tk.Label(mainframe,text="Hello")
lbl.grid(row=0,column=0)
but=tk.Button(mainframe,text="Click Me")
but.grid(row=1,column=0)
lv=tk.Listbox

root.mainloop()