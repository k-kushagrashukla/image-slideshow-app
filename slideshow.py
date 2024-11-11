from itertools import cycle
from PIL import Image,ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("image slideshow viewer")

image_paths=[
    r"C:\Users\kusha\OneDrive\Pictures\Camera Roll\WIN_20230914_14_55_07_Pro.jpg",
    r"C:\Users\kusha\OneDrive\Pictures\Camera Roll\WIN_20230911_13_51_39_Pro.jpg",
    r"C:\Users\kusha\OneDrive\Pictures\Camera Roll\WIN_20230910_18_17_59_Pro.jpg",
]

image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button=tk.Button(root,text='play slideshow',command=start_slideshow)
play_button.pack()

root.mainloop()