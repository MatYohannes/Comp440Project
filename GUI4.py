import os
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module


searchWindow = Tk()
searchWindow.rowconfigure(0, weight=1)
searchWindow.columnconfigure(0, weight=1)
searchWindow.state('zoomed')
searchWindow.resizable(0, 0)
searchWindow.title('Portal')

searchIcon = PhotoImage(file='Images/main user.png')
searchWindow.iconphoto(True, searchIcon)


def returnToPortal():
    searchWindow.destroy()
    os.system('python GUI2.py')


searchPage = Frame(searchWindow)
searchPage.grid(row=0, column=0, sticky='nsew')

designFrame1 = Listbox(searchPage, bg='#1594ef', width=260, height=50, highlightthickness=0, borderwidth=0)
designFrame1.place(x=0, y=0)

designFrame2 = Listbox(searchPage, bg='#0c71b9', width=190, height=25, highlightthickness=0, borderwidth=0)
designFrame2.place(x=75, y=335)

searchTitleLabel = Label(designFrame1, text='Search Items by Category', font=('Arial', 30, 'bold'), bg='#2095e9')
searchTitleLabel.place(x=130, y=50)

categoryEntry = Entry(designFrame1, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
categoryEntry.place(x=250, y=150, width=256, height=34)
categoryLabel = Label(designFrame1, text='Category', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
categoryLabel.place(x=100, y=150)

searchButton = Button(designFrame1, text='Search Item', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=lambda: searchItem()) # add parameters
searchButton.place(x=600, y=150)

addItemButton = Button(designFrame1, text='Add Item', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=None) # add parameters
addItemButton.place(x=1000, y=270)

backButton = Button(designFrame1, text='Back to Portal', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=returnToPortal)
backButton.place(x=1000, y=740)

# ========= Top Right Side Picture =========
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((200, 200))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame1, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=1000, y=30)


def searchItem():
    searchWinPopup = Toplevel()
    windowWidth = 800
    windowHeight = 500
    screenWidth = searchWinPopup.winfo_screenwidth()
    screenHeight = searchWinPopup.winfo_screenheight()
    positionTop = int(screenHeight / 4 - windowHeight / 4)
    positionRight = int(screenWidth / 2 - windowWidth / 2)
    searchWinPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
    searchWinPopup.title('Search Item')
    searchWinPopup.iconbitmap('Images/show.png')  ######
    searchWinPopup.configure(background='#f8f8f8')
    searchWinPopup.resizable(0, 0)

    def exitButton():
        searchWinPopup.destroy()
        #searchWinPopup.update()

    designFrame3 = Listbox(searchWinPopup, bg='#1594ef', width=215, height=50, highlightthickness=0, borderwidth=0)
    designFrame3.place(x=0, y=0)

    designFrame4 = Listbox(searchWinPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0, borderwidth=0)
    designFrame4.place(x=0, y=75)

    SearchPopupTitle = Label(designFrame3, text='Items Found', font=('Arial', 25, 'bold'), bg='#2095e9')
    SearchPopupTitle.place(x=80, y=15)

    backButtonPopUp = Button(designFrame3, text='Back', font=("yu gothic ui bold", 12),
                        bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                        cursor='hand2', height=2, width=20, command=lambda: exitButton())
    backButtonPopUp.place(x=600, y=425)

searchWindow.mainloop()
