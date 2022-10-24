import cv2
import asciify
from tkinter import *
import tkinter as tk


def show_ascii():
    # setting up video capture
    cam = cv2.VideoCapture(0)
    # setting up tkinter window
    root = Tk()
    root.title("Ascii.py")
    # setting up text widget
    T = Text(root, height=120, width=320, font=('Monocode', 5), bg="black", fg="white")
    T.pack()
    # translating the numpy array returned by the read() funtion to ascii and showing
    # it in the window
    while True:
        ret_val, img = cam.read()
        ascii = asciify.convert_image(img, 4)
        T.delete("0.0","end")
        T.insert(tk.END, ascii)
        root.update()
    root.mainloop()


def main():
    show_ascii()


if __name__=="__main__":
    main()