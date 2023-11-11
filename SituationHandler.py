
from tkinter import Tk, Label, Text, END, Frame
from PIL import Image, ImageTk

from tkinter import Scrollbar, Canvas
from PIL import Image, ImageTk
from tkinter.font import Font


class SituationHandler():
    def __init__(self):
        self.initCanvas()

    def initCanvas(self):
        self.root = Tk()
        self.root.title("Analysis Result")
        canvas = Canvas(self.root)
        scrollbar = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        self.scrollable_frame = Frame(canvas)

        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    def takeActionOnAnalysis(self, pairs):
        for image, analysis in pairs:
            self.AddImageAndAnalysis(image, analysis)
        self.root.mainloop()

    def AddImageAndAnalysis(self, image, analysis):
        # Create a new frame for the image and analysis
        frame = Frame(self.scrollable_frame)

        # Load and resize the image
        image = Image.open(image)
        max_size = (600, 600)
        image.thumbnail(max_size)
        photo = ImageTk.PhotoImage(image)

        # Create a label for the image and add it to the frame
        label = Label(frame, image=photo)
        label.image = photo
        label.pack()

        # Create a text widget for the analysis and add it to the frame
        my_font = Font(family="Helvetica", size=14, weight="bold")
        label_text = Label(frame, text=analysis, font=my_font, fg="red" if not "OK" in analysis else "black", wraplength=200)
        label_text.pack()

        # Add the frame to the scrollable frame
        frame.pack(pady=10)
