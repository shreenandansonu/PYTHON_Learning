import tkinter as tk

root=tk.Tk()
root.title("Test App")

def add_item(event:None):
    text=entry.get()
    if text:
        lv.insert(tk.END,text)
        entry.delete(0,tk.END)

main=tk.LabelFrame(root,text="Mian Frame")
main.grid(row=0,column=0)

entry=tk.Entry(main)
entry.grid(row=0,column=0)

entry.bind("<Return>",add_item)

but=tk.Button(main,text="ADD",command=add_item)
but.grid(row=0,column=1)

lv=tk.Listbox(main)
lv.grid(row=1,column=0)

root.mainloop()


