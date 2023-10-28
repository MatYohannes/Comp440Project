import os
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module


viewItemWindow = Tk()
viewItemWindow.rowconfigure(0, weight=1)
viewItemWindow.columnconfigure(0, weight=1)
viewItemWindow.state('zoomed')
viewItemWindow.resizable(0, 0)
viewItemWindow.title('View Items')

viewItemIcon = PhotoImage(file='Images/main user.png')
viewItemWindow.iconphoto(True, viewItemIcon)


def returnToPortal():
    viewItemWindow.destroy()
    os.system('python GUI2.py')

viewPage = Frame(viewItemWindow)
viewPage.grid(row=0, column=0, sticky='nsew')

designFrame1 = Listbox(viewPage, bg='#0c71b9', width=260, height=50, highlightthickness=0, borderwidth=0)
designFrame1.place(x=0, y=0)

designFrame2 = Listbox(viewPage, bg='#1e85d0', width=190, height=23, highlightthickness=0, borderwidth=0)
designFrame2.place(x=75, y=350)

itemNameReturnedValue = "Temp"

ItemNameLabel = Label(designFrame1, text=itemNameReturnedValue, font=('Arial', 30, 'bold'), bg='#2095e9')
ItemNameLabel.place(x=130, y=20)

categoryReturnedValue = ""
categoryLabel = Label(designFrame1, text='Category:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
categoryLabel.place(x=100, y=100)
categoryReturnLabel = Text(designFrame1, height=2, width=40)
categoryReturnLabel.insert(END, categoryReturnedValue)
categoryReturnLabel.place(x=100, y=140)

descriptionReturnedValue = ""
categoryLabel = Label(designFrame1, text='Description:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
categoryLabel.place(x=100, y=200)
categoryReturnLabel = Text(designFrame1, height=2, width=40)
categoryReturnLabel.insert(END, descriptionReturnedValue)
categoryReturnLabel.place(x=100, y=250)

priceReturnedValue = ""
priceLabel = Label(designFrame1, text='Price:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
priceLabel.place(x=500, y=100)
priceReturnedLabel = Text(designFrame1, height=2, width=40)
priceReturnedLabel.insert(END, priceReturnedValue)
priceReturnedLabel.place(x=500, y=140)

createDateReturnedValue = ""
createDateLabel = Label(designFrame1, text='Created Date:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
createDateLabel.place(x=500, y=200)
createDateReturnedLabel = Text(designFrame1, height=2, width=40)
createDateReturnedLabel.insert(END, createDateReturnedValue)
createDateReturnedLabel.place(x=500, y=250)

addReview = Button(designFrame1, text='Add Review', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=lambda: addReview())
addReview.place(x=100, y=740)

backButton = Button(designFrame1, text='Back to Portal', font=("yu gothic ui bold", 12),
                      bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                      cursor='hand2', height=2, width=20, command=returnToPortal)
backButton.place(x=1000, y=740)

reviewListLabel = Label(designFrame2, text="Reviews", font=('Arial', 30, 'bold'), bg='#2095e9')
reviewListLabel.place(x=130, y=20)

# ========= Top Right Side Picture =========
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((200, 200))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame1, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=1000, y=30)


# ========= PopUp to Add Review =========
def addReview():
    addReviewWindow = Toplevel()
    windowWidth = 800
    windowHeight = 500
    screenWidth = addReviewWindow.winfo_screenwidth()
    screenHeight = addReviewWindow.winfo_screenheight()
    positionTop = int(screenHeight / 4 - windowHeight / 4)
    positionRight = int(screenWidth / 2 - windowWidth / 2)
    addReviewWindow.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
    addReviewWindow.title('Search Item')
    addReviewWindow.iconbitmap('Images/show.png')  ######
    addReviewWindow.configure(background='#f8f8f8')
    addReviewWindow.resizable(0, 0)

    def cancelButton():
        addReviewWindow.destroy()

    designFrame3 = Listbox(addReviewWindow, bg='#1594ef', width=215, height=50, highlightthickness=0, borderwidth=0)
    designFrame3.place(x=0, y=0)

    addReviewTitle = Label(designFrame3, text='Add Review', font=('Arial', 25, 'bold'), bg='#2095e9')
    addReviewTitle.place(x=80, y=15)


    # Dropdown Rating Options
    ratings = [1, 2, 3, 4, 5]

    # Datatype of Rating Text
    clicked = StringVar()

    # Initial Dropdown Text
    clicked.set("1")

    # Dropdown Button
    ratingLabel = Label(addReviewWindow, text='Rating', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    ratingLabel.place(x=50, y=100)

    # Create Dropdown Menu
    drop = OptionMenu(addReviewWindow, clicked, *ratings,)
    drop.place(x=200, y=100)

    descriptionPopupLabel = Label(addReviewWindow, text='Description', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    descriptionPopupLabel.place(x=50, y=150)

    categoryReturnLabel = Text(addReviewWindow, height=10, width=80)
    categoryReturnLabel.place(x=50, y=200)


    submitReview = Button(designFrame3, text='Submit', font=("yu gothic ui bold", 12),
                        bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                        cursor='hand2', height=2, width=20, command=None)
    submitReview.place(x=50, y=420)


    cancelReviewPopUp = Button(designFrame3, text='Cancel', font=("yu gothic ui bold", 12),
                        bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                        cursor='hand2', height=2, width=20, command=lambda: cancelButton())
    cancelReviewPopUp.place(x=250, y=420)


viewItemWindow.mainloop()


