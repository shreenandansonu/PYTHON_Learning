import tkinter as tk

root = tk.Tk()
root.title("Layout Demo")
root.geometry("400x200")

# Top heading using pack
heading = tk.Label(root, text="Welcome!", font=("Arial", 20), bg="lightblue")
heading.pack(fill="x")

# Grid layout for form
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(frame).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(frame).grid(row=1, column=1, padx=5, pady=5)

# Submit button
tk.Button(root, text="Submit").pack(pady=10)

root.mainloop()
