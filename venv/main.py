import tkinter as tk
from tkinter import *
from summarize import summarizetext
from summarize import nltkdownload

r = tk.Tk()
summaryLabel = Label(r, text = "If this is your first time running this program, please his the download NLTK Data button.", width = 100, wraplength = 400, justify = "left")
def summarizebuttonaction():
    summaryText = summarizetext(inputUrl.get())
    summaryLabel.config(text = summaryText)


r.title("Summarize Website")
inputUrl = tk.StringVar()
urlEntry = Entry(r, width=50, textvariable = inputUrl)
summarizeButton = Button(r, text='Summarize', width=25, command = lambda: summarizebuttonaction())
nltkDataButton = Button(r, text = "Download NLTK Data", command = lambda: nltkdownload())




urlEntry.pack()
summarizeButton.pack()
summaryLabel.pack()
nltkDataButton.pack(side = "bottom")
r.mainloop()