import tkinter as tk

window = tk.Tk()
window.title("One")
window.geometry("400x400")

def handle_button_press():
    window.destroy()

button = tk.Button(text="Button", command = handle_button_press)
button.pack()

window.mainloop()
