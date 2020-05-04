import tkinter as tk
from tkinter import *
from summarize import summarizetext

r = tk.Tk()
summaryLabel = Label(r, text = "Summarized Text will go here", width = 100, wraplength = 400, justify = "left")
def summarizebuttonaction():
    summaryText = summarizetext(inputUrl.get())
    summaryLabel.config(text = summaryText)


r.title("Summarize Website")
inputUrl = tk.StringVar()
urlEntry = Entry(r, width=50, textvariable = inputUrl)
summarizeButton = Button(r, text='Summarize', width=25, command = lambda: summarizebuttonaction())





urlEntry.pack()
summarizeButton.pack()
summaryLabel.pack()
r.mainloop()