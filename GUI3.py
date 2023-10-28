import os
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module


insertWindow = Tk()
insertWindow.rowconfigure(0, weight=1)
insertWindow.columnconfigure(0, weight=1)
insertWindow.state('zoomed')
insertWindow.resizable(0, 0)
insertWindow.title('Portal')

insertItemIcon = PhotoImage(file='Images/main user.png')
insertWindow.iconphoto(True, insertItemIcon)


def returnToPortal():
    insertWindow.destroy()
    os.system('python GUI2.py')


def clearEntries():
    titleEntry.delete(0, END)
    descriptionEntry.delete(0, END)
    categoryEntry.delete(0, END)
    priceEntry.delete(0, END)
    priceEntry.insert(0, "0.00")





insertPage = Frame(insertWindow)
insertPage.grid(row=0, column=0, sticky='nsew')

designFrame1 = Listbox(insertPage, bg='#0c71b9', width=260, height=50, highlightthickness=0, borderwidth=0)
designFrame1.place(x=0, y=0)

designFrame2 = Listbox(insertPage, bg='#1e85d0', width=100, height=40, highlightthickness=0, borderwidth=0)
designFrame2.place(x=75, y=115)

pageName = Label(designFrame1, text='Insert Item', font=('Arial', 50, 'bold'), bg='#2095e9')
pageName.place(x=130, y=20)

titleEntry = Entry(designFrame2, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
titleEntry.place(x=250, y=100, width=256, height=34)
titleLabel = Label(designFrame2, text='Title', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
titleLabel.place(x=100, y=100)

descriptionEntry = Entry(designFrame2, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
descriptionEntry.place(x=250, y=150, width=256, height=34)
descriptionLabel = Label(designFrame2, text='Description', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
descriptionLabel.place(x=100, y=150)

categoryEntry = Entry(designFrame2, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
categoryEntry.place(x=250, y=200, width=256, height=34)
categoryLabel = Label(designFrame2, text='Category', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
categoryLabel.place(x=100, y=200)

priceEntry = Spinbox(designFrame2, from_=0.0, to=100000.00, increment=0.01, justify=CENTER) # Need to validate Entry to be Digit
priceEntry.place(x=250, y=250, width=256, height=34)
priceLabel = Label(designFrame2, text='Price', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
priceLabel.place(x=100, y=250)

insertItemButton = Button(designFrame2, text='Insert Item', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=15, command=None)
insertItemButton.place(x=100, y=350)

clearButton = Button(designFrame2, text='Clear', font=("yu gothic ui bold", 12),
                     bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                     cursor='hand2', height=2, width=15, command=clearEntries)
clearButton.place(x=300, y=350)

backButton = Button(designFrame1, text='Back to Portal', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=returnToPortal)
backButton.place(x=1000, y=740)

# ========= Right Side Picture =========
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((550, 550))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame1, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=800, y=150)


insertPage.mainloop()

