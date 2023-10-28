import os
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module


portalPage = Tk()
portalPage.rowconfigure(0, weight=1)
portalPage.columnconfigure(0, weight=1)
portalPage.state('zoomed')
portalPage.resizable(0, 0)
portalPage.title('Portal')

# Portal Icon Photo
portalIcon = PhotoImage(file='Images/main user.png')
portalPage.iconphoto(True, portalIcon)


# When Insert Item is clicked, enter GUI3 (Insert Item Page)
def enterInsert():
    portalPage.destroy()
    os.system('python GUI3.py')


# When Search is clicked, enter GUI4 (Search Item Page)
def enterSearch():
    portalPage.destroy()
    os.system('python GUI4.py')


def closeProgram():
    portalPage.quit()


# ====================== PENDING =====================
# When Reports is clicked, enter TBD
def enderReports():
    portalPage.destroy()
    #os.system('python GUI4.py')


portal = Frame(portalPage)
portal.grid(row=0, column=0, sticky='nsew')

designFrame1 = Listbox(portal, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
designFrame1.place(x=0, y=0)
designFrame2 = Listbox(portal, bg='#1594ef', width=150, height=50, highlightthickness=0, borderwidth=0)
designFrame2.place(x=676, y=0)
designFrame3 = Listbox(portal, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame3.place(x=75, y=150)

welcomeLabel = Label(designFrame1, text='Portal', font=('Arial', 50, 'bold'), bg='#2095e9')
welcomeLabel.place(x=130, y=50)

insertItem = Button(portal, text='Insert Item', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=30, command=enterInsert)
insertItem.place(x=100, y=250)

searchButton = Button(portal, text='Search', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=30, command=enterSearch)
searchButton.place(x=100, y=350)

reportsButton = Button(portal, text='Reports', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=30, command=None)
reportsButton.place(x=100, y=450)

closeProgramButton = Button(portal, text='Close Program', font=("yu gothic ui bold", 12),
                      bg='#d32226', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=30, command=closeProgram)
closeProgramButton.place(x=100, y=700)

# ========= Right Side Picture =========
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((550, 550))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame2, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=75, y=150)


portalPage.mainloop()



