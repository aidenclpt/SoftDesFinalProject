# Browses to an image file and then opens a Viewer object to allow for location,
# distance, and area measurements

from ui import Viewer
from tkinter import *
from tkinter.filedialog import askopenfilename


if __name__ == "__main__":
# Creat a tkinter root
    root = Tk()
    root.title("Draw Some Points!")

# Open file browser
    File = askopenfilename(parent=root, initialdir="../", title='Select an image')

# Initalize the view
    Viewer(root, File)

# Start tkinter event loop
    root.mainloop()
