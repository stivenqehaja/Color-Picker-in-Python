import pyautogui
import tkinter as tk

def update_label():
    x, y = pyautogui.position()
    pixel = pyautogui.screenshot().getpixel((x, y))
    rgb = f"RGB: {pixel[0]}, {pixel[1]}, {pixel[2]}"
    cmy = f"CMY: {255-pixel[0]}, {255-pixel[1]}, {255-pixel[2]}"
    position_label.config(text=f"Position: {x}, {y}")
    rgb_label.config(text=rgb)
    cmy_label.config(text=cmy)
    root.after(100, update_label)

root = tk.Tk()
root.geometry("300x100")

position_label = tk.Label(root, text="Position: ")
position_label.pack()

rgb_label = tk.Label(root, text="RGB: ")
rgb_label.pack()

cmy_label = tk.Label(root, text="CMY: ")
cmy_label.pack()

update_label()

root.mainloop()
