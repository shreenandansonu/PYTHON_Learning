import tkinter as tk

root=tk.Tk()

def toggle_name():
    if(lable["text"]=="Shreenandan"):
        lable.config(text="Suraksha")
    else:
        lable.config(text="Shreenandan")
        
root.title("Shreenandan")
root.iconbitmap('GUI/heart.ico')
root.geometry('800x500')
lable=tk.Label(text="Shreenandan",font="courier",foreground="white",background="#000000")
lable.grid(row=1,column=1,columnspan=5)
bt1=tk.Button(root,text="blue",command=toggle_name)
bt1.grid(row=2,column=2)



root.mainloop()