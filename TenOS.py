import tkinter as tk
from tkinter import PhotoImage, messagebox
import subprocess
import time
import os
import base64

# Create main window
root = tk.Tk()
root.title("OS Simulator")
root.geometry("800x600")
root.resizable(False, False)

# Set wallpaper
wallpaper_path = r"C:\DeskWWW\r4.png"
if os.path.exists(wallpaper_path):
    bg_image = PhotoImage(file=wallpaper_path)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    root.configure(bg="lightblue")

# Start Menu Frame (initially hidden)
start_menu = tk.Frame(root, bg="gray", width=200, height=250)
start_menu.place(x=0, y=350)
start_menu.place_forget()

def toggle_start_menu():
    if start_menu.winfo_ismapped():
        start_menu.place_forget()
    else:
        start_menu.place(x=0, y=350)

# Taskbar
taskbar = tk.Frame(root, bg="black", height=30)
taskbar.pack(side="bottom", fill="x")

# Time and Date Label
time_label = tk.Label(taskbar, fg="white", bg="black", font=("Segoe UI", 10))
time_label.pack(side="right", padx=10)

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d-%b-%Y")
    time_label.config(text=f"{current_time} | {current_date}")
    root.after(1000, update_time)

update_time()

# Start Button
start_button = tk.Button(taskbar, text="Start", command=toggle_start_menu, bg="gray", fg="white")
start_button.pack(side="left", padx=5)

# App Launchers
def open_notepad():
    subprocess.Popen(["notepad.exe"])

def open_paint():
    subprocess.Popen(["mspaint.exe"])

def open_cmd():
    subprocess.Popen(["cmd.exe"])

def open_regedit():
    subprocess.Popen(["regedit.exe"])

def open_edge():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_path):
        subprocess.Popen([edge_path])
    else:
        messagebox.showerror("Error", "Edge not found!")

# Shutdown Function (in current window)
def shutdown_os():
    # Hide all widgets
    for widget in root.winfo_children():
        widget.place_forget()
        widget.pack_forget()

    # Load and show shutdown image
    shutdown_path = r"C:\DeskWWW\sd.png"
    if os.path.exists(shutdown_path):
        shutdown_image = PhotoImage(file=shutdown_path)
        shutdown_label = tk.Label(root, image=shutdown_image)
        shutdown_label.image = shutdown_image  # Keep reference
        shutdown_label.place(x=0, y=0, relwidth=1, relheight=1)
    else:
        shutdown_label = tk.Label(root, text="Shutting down...", font=("Segoe UI", 24), bg="black", fg="white")
        shutdown_label.place(relx=0.5, rely=0.5, anchor="center")

    # Delay and exit
    root.after(4000, root.destroy)

# Buttons in Start Menu
apps = [
    ("Notepad", open_notepad),
    ("Paint", open_paint),
    ("CMD", open_cmd),
    ("Registry Editor", open_regedit),
    ("Microsoft Edge", open_edge),
    ("Shutdown", shutdown_os)
]

for name, cmd in apps:
    btn = tk.Button(start_menu, text=name, command=cmd, width=25)
    btn.pack(pady=5)

# Run the app
root.mainloop()