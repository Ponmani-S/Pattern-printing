import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S')
    label.config(text=time_string)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=('Arial', 48), background='black', foreground='lime')
label.pack(anchor='center')
update_time()
root.mainloop()
