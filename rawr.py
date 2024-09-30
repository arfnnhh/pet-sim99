import threading
import time
from tkinter import *
from tkinter import ttk
from pynput import keyboard, mouse

auto_pressing = False
auto_clicking = False
keyboard_controller = keyboard.Controller()
mouse_controller = mouse.Controller()

def start_auto_pressing():
    global auto_pressing
    auto_pressing = True
    auto_pressing_var.set(True)  
    root.attributes('-topmost', True)  
    while auto_pressing:
        keyboard_controller.press('r')
        keyboard_controller.release('r')
        time.sleep(0.05)

def stop_auto_pressing():
    global auto_pressing
    auto_pressing = False
    auto_pressing_var.set(False)  
    check_topmost()  

def start_auto_clicking():
    global auto_clicking
    auto_clicking = True
    auto_clicking_var.set(True)  
    root.attributes('-topmost', True)  
    while auto_clicking:
        mouse_controller.click(mouse.Button.left)
        time.sleep(0.05)

def stop_auto_clicking():
    global auto_clicking
    auto_clicking = False
    auto_clicking_var.set(False)  
    check_topmost()  

def check_topmost():
    if not auto_pressing and not auto_clicking:
        root.attributes('-topmost', False)  

def toggle_auto_pressing():
    global auto_pressing
    if auto_pressing:
        stop_auto_pressing()
    else:
        threading.Thread(target=start_auto_pressing, daemon=True).start()

def toggle_auto_clicking():
    global auto_clicking
    if auto_clicking:
        stop_auto_clicking()
    else:
        threading.Thread(target=start_auto_clicking, daemon=True).start()

def quit_app(event=None):
    stop_auto_pressing()
    stop_auto_clicking()
    root.destroy()

# Initialize the Tkinter application
root = Tk()
root.title("PS99 Function")  
root.geometry("250x100")  
root.resizable(False, False)  

# Create a style for the widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#2b2b2b')
style.configure('TCheckbutton', background='#2b2b2b', foreground='#ffffff', font=('Helvetica', 12))
style.configure('TButton', background='#4b4b4b', foreground='#ffffff', font=('Helvetica', 12))
style.map('TButton', background=[('active', '#6b6b6b')])

frm = ttk.Frame(root, padding=10)
frm.grid(sticky='nsew')

icon_image = PhotoImage(file="images.png")
root.iconphoto(True, icon_image)

# Variables for the switch indicators
auto_pressing_var = BooleanVar(value=False)
auto_clicking_var = BooleanVar(value=False)

# Indicator for auto-pressing
ttk.Checkbutton(frm, text="Auto-Ultimate 'F6'", variable=auto_pressing_var, command=toggle_auto_pressing).grid(column=0, row=0, sticky="w", pady=10)

# Indicator for auto-clicking
ttk.Checkbutton(frm, text="Auto-click 'F7'", variable=auto_clicking_var, command=toggle_auto_clicking).grid(column=0, row=1, sticky="w", pady=10)

# Center the Quit button
ttk.Button(frm, text="Quit", command=quit_app).grid(column=0, row=2, pady=10, sticky='nsew')

# Configure row and column weights to center the button
frm.grid_rowconfigure(0, weight=1)  
frm.grid_rowconfigure(1, weight=1)  
frm.grid_rowconfigure(2, weight=1)  
frm.grid_columnconfigure(0, weight=1)  

root.configure(background='#2b2b2b')

def on_key_press(key):
    try:
        if key == keyboard.Key.f6:
            toggle_auto_pressing()
        elif key == keyboard.Key.f7:
            toggle_auto_clicking()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_key_press)
listener.start()

root.mainloop()