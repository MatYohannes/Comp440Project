import os
from calendar import Calendar
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
from tkinter import Button, messagebox, ttk
# from argon2 import Parameters
import mysql.connector
import re
import datetime

# Define your MySQL database connection parameters
host = "localhost"
database = "comp440_database_project"
user = "root"
password = ""  # enter password
date = datetime.datetime.now()
listingDate = date.strftime("%Y-%m-%d")


class reviewedObject:
    def __init__(self, reviewProductID, reviewProductName, reviewProductDescription,
                 reviewProductCategory, reviewProductPrice, reviewCreator, reviewCreatedDate):
        self.reviewProductID = reviewProductID
        self.reviewProductName = reviewProductName
        self.reviewProductDescription = reviewProductDescription
        self.reviewProductCategory = reviewProductCategory
        self.reviewProductPrice = reviewProductPrice
        self.reviewCreator = reviewCreator
        self.reviewCreatedDate = reviewCreatedDate

    def getReviewProductID(self):
        return self.reviewProductID

    def getReviewProductName(self):
        return self.reviewProductName

    def getReviewProductionDescription(self):
        return self.reviewProductDescription

    def getReviewProductCategory(self):
        return self.reviewProductCategory

    def getReviewProductPrice(self):
        return self.reviewProductPrice

    def getReviewCreator(self):
        return self.reviewCreator

    def getReviewCreatedDate(self):
        return self.reviewCreatedDate

    ##
    def setReviewProductID(self, value):
        self.reviewProductID = value

    def setReviewProductName(self, value):
        self.reviewProductName = value

    def setReviewProductionDescription(self, value):
        self.reviewProductDescription = value

    def setReviewProductCategory(self, value):
        self.reviewProductCategory = value

    def setReviewProductPrice(self, value):
        self.reviewProductPrice = value

    def setReviewCreator(self, value):
        self.reviewCreator = value

    def setReviewCreatedDate(self, value):
        self.reviewCreatedDate = value


def initializeDB():
    conn = create_db_connection()
    outResult = None

    if conn:
        try:
            # Define the stored procedure name
            procedure_name = "initialize_baseTables"

            # Create a tuple containing the input parameters for the stored procedure
            params = (outResult,)

            query = procedure_name
            returned_result = execute_query(conn, query, params)

            print(returned_result)
            returned_result_str = " ".join(returned_result[0])

            if returned_result_str == "Database Initialized":
                messagebox.showinfo(
                    title="Success", message="Database initialized!"
                )
        finally:
            conn.close()


def GUI2():
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
        GUI3()

    # When Search is clicked, enter GUI4 (Search Item Page)
    def enterSearch():
        portalPage.destroy()
        GUI4()

    def enterReports():
        portalPage.destroy()
        GUI6()

    def closeProgram():
        portalPage.destroy()

    # ====================== PENDING =====================
    # When Reports is clicked, enter TBD
    def enderReports():
        portalPage.destroy()
        GUI4()

    portal = Frame(portalPage)
    portal.grid(row=0, column=0, sticky='nsew')

    designFrame1 = Listbox(portal, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
    designFrame1.place(x=0, y=0)
    designFrame2 = Listbox(portal, bg='#1594ef', width=150, height=50, highlightthickness=0, borderwidth=0)
    designFrame2.place(x=676, y=0)
    designFrame3 = Listbox(portal, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
    designFrame3.place(x=75, y=150)

    welcomeLabel = Label(designFrame1, text=userNameGlobal + "'s Portal", font=('Arial', 50, 'bold'), bg='#2095e9')
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
                           cursor='hand2', height=2, width=30, command=enterReports)
    reportsButton.place(x=100, y=450)

    InitializeDB = Button(portal, text='Initialize DataBase', font=("yu gothic ui bold", 12),
                          bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                          cursor='hand2', height=2, width=30, command=lambda: initializeDB())
    InitializeDB.place(x=100, y=550)

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


def insertItemF(title, description, category, price):
    conn = create_db_connection()
    outResult = None
    if conn:
        try:
            # Define the stored procedure name
            procedure_name = "p_insert_new_item"

            # Create a tuple containing the input parameters for the stored procedure
            params = (
                userNameGlobal,
                title,
                description,
                category,
                price,
                listingDate,
                outResult,
            )

            query = procedure_name
            returned_result = execute_query(conn, query, params)
            # print(returned_result)
            returned_result_str = " ".join(returned_result[0])

            if returned_result_str == "Item Inserted":
                messagebox.showinfo(
                    title="Success", message="Insert has been add!"
                )

            elif "Injection" in returned_result_str:
                messagebox.showinfo(
                    title="Error",
                    message=f"SQL {returned_result_str}. SignUp Unsuccessful. Please Re-Enter!"
                )
            else:
                messagebox.showinfo("Could not insert item")
        finally:
            conn.close()


def GUI3():
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
        GUI2()

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
    descriptionEntry.place(x=250, y=150, width=256, height=75)
    descriptionLabel = Label(designFrame2, text='Description', fg="#f8f8f8", bg='#1e85d0',
                             font=("yu gothic ui", 14, 'bold'))
    descriptionLabel.place(x=100, y=150)

    categoryEntry = Entry(designFrame2, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    categoryEntry.place(x=250, y=250, width=256, height=34)
    categoryLabel = Label(designFrame2, text='Category', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    categoryLabel.place(x=100, y=250)

    priceEntry = Spinbox(designFrame2, from_=0.0, to=100000.00, increment=0.01,
                         justify=CENTER)  # Need to validate Entry to be Digit
    priceEntry.place(x=250, y=300, width=256, height=34)
    priceLabel = Label(designFrame2, text='Price', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    priceLabel.place(x=100, y=300)

    insertItemButton = Button(designFrame2, text='Insert Item', font=("yu gothic ui bold", 12),
                              bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                              cursor='hand2', height=2, width=15,
                              command=lambda: insertItemF(titleEntry.get(), descriptionEntry.get(),
                                                          categoryEntry.get(), float(priceEntry.get())))
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


def displayAllItems():
    conn = create_db_connection()
    if conn:
        try:
            # Define the stored procedure name
            procedure_name = "p_display_AllItemsPresent"
            params = ()
            returned_result = execute_query(conn, procedure_name, params)
            # Call the stored procedure using the call_stored_procedure function
            if returned_result:
                return returned_result
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            conn.close()


def GUI4():
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
        GUI2()

    def getSelectItem():
        selectedItem = searchDisplay.focus()
        details = searchDisplay.item(selectedItem)
        product = details.get("values")
        productId = product[0]
        productName = product[1]
        productDescription = product[2]
        productCategories = product[3]
        productPrice = product[4]
        productCreator = product[5]
        productDate = product[6]

        reviewObject = reviewedObject(productId, productName, productDescription, productCategories,
                                      productPrice, productCreator, productDate)
        searchWindow.destroy()
        GUI5(reviewObject)

    searchPage = Frame(searchWindow)
    searchPage.grid(row=0, column=0, sticky='nsew')

    designFrame1 = Listbox(searchPage, bg='#1594ef', width=260, height=50, highlightthickness=0, borderwidth=0)
    designFrame1.place(x=0, y=0)

    searchBoxDisplay = Listbox(searchPage, bg='#0c71b9', width=190, height=25, highlightthickness=0, borderwidth=0)
    searchBoxDisplay.place(x=75, y=335)

    # Displaying table in Search Window
    connect = create_db_connection()
    connSearchDisplay = connect.cursor()
    connSearchDisplay.execute("SELECT * FROM comp440_database_project.itemdetails;")
    searchDisplay = ttk.Treeview(searchBoxDisplay, selectmode=BROWSE)
    searchDisplay['show'] = 'headings'
    # Define number of columns
    searchDisplay['columns'] = (
        'ItemID', 'itemTitle', 'itemDescription', 'itemCategory', 'itemPrice', 'userName', 'DateofListing')

    # Assign dimensions
    searchDisplay.column("ItemID", width=120, minwidth=50, anchor=W)
    searchDisplay.column("itemTitle", width=120, minwidth=50, anchor=W)
    searchDisplay.column("itemDescription", width=120, minwidth=50, anchor=W)
    searchDisplay.column("itemCategory", width=120, minwidth=50, anchor=W)
    searchDisplay.column("itemPrice", width=120, minwidth=50, anchor=W)
    searchDisplay.column("userName", width=120, minwidth=50, anchor=W)
    searchDisplay.column("DateofListing", width=120, minwidth=50, anchor=W)

    # Assign headers to table columns
    searchDisplay.heading("ItemID", text="Item ID", anchor=W)
    searchDisplay.heading("itemTitle", text="Item Name", anchor=W)
    searchDisplay.heading("itemDescription", text="Description", anchor=W)
    searchDisplay.heading("itemCategory", text="Category", anchor=W)
    searchDisplay.heading("itemPrice", text="Price", anchor=W)
    searchDisplay.heading("userName", text="Added By", anchor=W)
    searchDisplay.heading("DateofListing", text="Created Date", anchor=W)

    i = 0
    for ro in connSearchDisplay:
        # print(ro)
        searchDisplay.insert("", i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
        i = i + 1

    searchDisplay.place(x=0, y=0)
    searchTitleLabel = Label(designFrame1, text='Search Items by Category', font=('Arial', 30, 'bold'), bg='#2095e9')
    searchTitleLabel.place(x=130, y=50)

    categoryEntry = Entry(designFrame1, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    categoryEntry.place(x=250, y=150, width=256, height=34)
    categoryLabel = Label(designFrame1, text='Category', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    categoryLabel.place(x=100, y=150)

    searchButton = Button(designFrame1, text='Search Item', font=("yu gothic ui bold", 12),
                          bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                          cursor='hand2', height=2, width=20,
                          command=lambda: searchItem(categoryEntry.get()))  # add parameters
    searchButton.place(x=600, y=150)

    reviewSelectedButton2 = Button(designFrame1, text='Review Item', font=("yu gothic ui bold", 12),
                                   bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                   cursor='hand2', height=2, width=20,
                                   command=lambda: getSelectItem())  # add parameters
    reviewSelectedButton2.place(x=800, y=270)

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

    def searchItem(cat):
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
            # searchWinPopup.update()

        designFrame3 = Listbox(searchWinPopup, bg='#1594ef', width=215, height=50, highlightthickness=0, borderwidth=0)
        designFrame3.place(x=0, y=0)

        designFrame4 = Listbox(searchWinPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0, borderwidth=0)
        designFrame4.place(x=0, y=75)

        SearchPopupTitle = Label(designFrame3, text='Categories: ' + cat.capitalize(), font=('Arial', 25, 'bold'),
                                 bg='#2095e9')
        SearchPopupTitle.place(x=80, y=15)

        backButtonPopUp = Button(designFrame3, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        # Displaying table in Category search window
        conn = create_db_connection()
        procedure_name = "search_by_Item_Category"
        categorySearchOutResult = None
        params = (cat, categorySearchOutResult)

        query = procedure_name
        returned_result = execute_query(conn, query, params)

        # Displaying table
        categorySearchDisplay = ttk.Treeview(designFrame4, selectmode=BROWSE)
        categorySearchDisplay['show'] = 'headings'
        # Define number of columns
        categorySearchDisplay['columns'] = ('itemCategory', 'itemTitle', 'itemDescription', 'itemPrice')

        # Assign Dimensions to search category table
        categorySearchDisplay.column('itemCategory', width=200, minwidth=200, anchor=W)
        categorySearchDisplay.column('itemTitle', width=200, minwidth=200, anchor=W)
        categorySearchDisplay.column('itemDescription', width=200, minwidth=200, anchor=W)
        categorySearchDisplay.column('itemPrice', width=200, minwidth=200, anchor=W)

        # Assign headers to table columns
        categorySearchDisplay.heading('itemCategory', text='Categories', anchor=W)
        categorySearchDisplay.heading('itemTitle', text='Title', anchor=W)
        categorySearchDisplay.heading('itemDescription', text='Description', anchor=W)
        categorySearchDisplay.heading('itemPrice', text='Price', anchor=W)

        j = 0
        for ro in returned_result:
            categorySearchDisplay.insert('', j, text='', values=(ro[0], ro[1], ro[2], ro[3]))
            j += 1
        categorySearchDisplay.place(x=0, y=0)

    searchWindow.mainloop()


def GUI5(object):
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
        GUI2()

    viewPage = Frame(viewItemWindow)
    viewPage.grid(row=0, column=0, sticky='nsew')

    designFrame1 = Listbox(viewPage, bg='#0c71b9', width=260, height=50, highlightthickness=0, borderwidth=0)
    designFrame1.place(x=0, y=0)

    designFrame2 = Listbox(viewPage, bg='#1e85d0', width=190, height=23, highlightthickness=0, borderwidth=0)
    designFrame2.place(x=75, y=350)

    selectedReviewProductID = object.getReviewProductID()
    selectedReviewProductName = object.getReviewProductName()
    selectedReviewProductDescription = object.getReviewProductionDescription()
    selectedReviewProductCategory = object.getReviewProductCategory()
    selectedReviewProductPrice = object.getReviewProductPrice()
    selectedReviewCreator = object.getReviewCreator()
    selectedReviewDate = object.getReviewCreatedDate()

    ItemNameLabel = Label(designFrame1, text=selectedReviewProductName, font=('Arial', 30, 'bold'), bg='#2095e9')
    ItemNameLabel.place(x=130, y=20)

    categoryLabel = Label(designFrame1, text='Category:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    categoryLabel.place(x=100, y=100)
    categoryReturnLabel = Text(designFrame1, height=2, width=40)
    categoryReturnLabel.insert(END, selectedReviewProductCategory)
    categoryReturnLabel.config(state=DISABLED)
    categoryReturnLabel.place(x=100, y=140)

    categoryLabel = Label(designFrame1, text='Description:', fg="#f8f8f8", bg='#1e85d0',
                          font=("yu gothic ui", 14, 'bold'))
    categoryLabel.place(x=100, y=200)
    categoryReturnLabel = Text(designFrame1, height=2, width=40)
    categoryReturnLabel.insert(END, selectedReviewProductDescription)
    categoryReturnLabel.config(state=DISABLED)
    categoryReturnLabel.place(x=100, y=250)

    priceLabel = Label(designFrame1, text='Price:', fg="#f8f8f8", bg='#1e85d0', font=("yu gothic ui", 14, 'bold'))
    priceLabel.place(x=500, y=100)
    priceReturnedLabel = Text(designFrame1, height=2, width=40)
    priceReturnedLabel.insert(END, selectedReviewProductPrice)
    priceReturnedLabel.config(state=DISABLED)
    priceReturnedLabel.place(x=500, y=140)

    createDateLabel = Label(designFrame1, text='Created Date:', fg="#f8f8f8", bg='#1e85d0',
                            font=("yu gothic ui", 14, 'bold'))
    createDateLabel.place(x=500, y=200)
    createDateReturnedLabel = Text(designFrame1, height=2, width=40)
    createDateReturnedLabel.insert(END, selectedReviewDate)
    createDateReturnedLabel.config(state=DISABLED)
    createDateReturnedLabel.place(x=500, y=250)

    addReview = Button(designFrame1, text='Add Review', font=("yu gothic ui bold", 12),
                       bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                       cursor='hand2', height=2, width=20, command=lambda: addReviewPop())
    addReview.place(x=100, y=740)

    backButton = Button(designFrame1, text='Back to Portal', font=("yu gothic ui bold", 12),
                        bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                        cursor='hand2', height=2, width=20, command=returnToPortal)
    backButton.place(x=1000, y=740)

    reviewListLabel = Label(designFrame1, text="Reviews", font=('Arial', 30, 'bold'), bg='#2095e9')
    reviewListLabel.place(x=130, y=290)

    # Display table in the Review Page
    connect = create_db_connection()
    connReviewDisplay = connect.cursor()
    tempQuery = "SELECT * FROM comp440_database_project.userreviews where itemID = %d;" % selectedReviewProductID
    # print(tempQuery)
    connReviewDisplay.execute(tempQuery)
    reviewDisplay = ttk.Treeview(designFrame2, selectmode=BROWSE)
    reviewDisplay['show'] = 'headings'
    # Define number of columns
    reviewDisplay['columns'] = ('ReviewID', 'ItemID', 'UserReview', 'UserReviewDescription', 'Username', 'DateofReview')

    # Assign dimensions
    reviewDisplay.column("ReviewID", width=120, minwidth=50, anchor=W)
    reviewDisplay.column("ItemID", width=120, minwidth=50, anchor=W)
    reviewDisplay.column("UserReview", width=120, minwidth=50, anchor=W)
    reviewDisplay.column("UserReviewDescription", width=350, minwidth=50, anchor=W)
    reviewDisplay.column("Username", width=120, minwidth=50, anchor=W)
    reviewDisplay.column("DateofReview", width=120, minwidth=50, anchor=W)

    # Assign headers to table columns
    reviewDisplay.heading("ReviewID", text="Review ID", anchor=W)
    reviewDisplay.heading("ItemID", text="Item ID", anchor=W)
    reviewDisplay.heading("UserReview", text="User Review", anchor=W)
    reviewDisplay.heading("UserReviewDescription", text="User Review Description", anchor=W)
    reviewDisplay.heading("Username", text="Username", anchor=W)
    reviewDisplay.heading("DateofReview", text="Date of Review", anchor=W)

    i = 0
    for ro in connReviewDisplay:
        # print(ro)
        reviewDisplay.insert("", i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
        i = i + 1

    reviewDisplay.place(x=0, y=0)

    # ========= Top Right Side Picture =========
    sideImage = Image.open('Images/left pic.png')
    sideImage = sideImage.resize((200, 200))
    photo = ImageTk.PhotoImage(sideImage)
    sideIconLabel = Label(designFrame1, image=photo, bg='#1e85d0')
    sideIconLabel.image = photo
    sideIconLabel.place(x=1000, y=30)

    # ========= PopUp to Add Review =========
    def addReviewPop():
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

        def submitReviewF(rating, descrip):
            selectedReviewItem = reviewDisplay.focus()
            details = reviewDisplay.item(selectedReviewItem)
            reviewProduct = details.get("values")
            userName = userNameGlobal.lower()
            DateofReview = listingDate

            # Insert new review to SQL table
            connect = create_db_connection()
            connAddReview = connect.cursor()
            procedure_name = "p_add_ItemReview"
            OutResult = None
            params = (
                object.getReviewProductName(), rating, descrip, DateofReview, userName, OutResult)

            returned_result = execute_query(connect, procedure_name, params)
            returned_result_str = " ".join(returned_result[0])
            print(returned_result_str)

            if returned_result_str == "Review Inserted Successfully":
                messagebox.showinfo(
                    title="Success", message="Review Inserted Successfully"
                )

            # addReviewQuery = "INSERT INTO comp440_database_project.userreviews(itemID,userReview,userReviewDescription,userName,DateofReview) VALUES(%d, %s, %s, %s, %s);" % (itemID, userReview, userReviewDescription, userName, DateofReview)

            # addReviewQuery = "INSERT INTO comp440_database_project.userreviews(`itemID`, `userReview`, `userReviewDescription`, `userName`, `DateofReview`) VALUES({id}, {uReview}, {des}, {name}, {dateN});".format(id=itemID, uReview=userReview, des=userReviewDescription, name=userName, dateN=DateofReview)
            # addReviewQuery = "INSERT INTO comp440_database_project.userreviews(`itemID`, `userReview`, `userReviewDescription`, `userName`, `DateofReview`) VALUES(%d, '%s', '%s', '%s', '%s');" % (itemID, userReview, userReviewDescription, userName, DateofReview)
            # connAddReview.execute(addReviewQuery)

            addReviewWindow.destroy()

        designFrame3 = Listbox(addReviewWindow, bg='#1594ef', width=215, height=50, highlightthickness=0, borderwidth=0)
        designFrame3.place(x=0, y=0)

        selectedAddReviewObjectName = object.getReviewProductName()
        addReviewTitle = Label(designFrame3, text=selectedAddReviewObjectName, font=('Arial', 25, 'bold'), bg='#2095e9')
        addReviewTitle.place(x=80, y=15)

        # Dropdown Rating Options
        ratings = ['Excellent', 'Good', 'Fair', 'Poor']
        # Datatype of Rating Text
        clicked = StringVar(addReviewWindow)

        # Initial Dropdown Text
        clicked.set("Excellent")

        # Dropdown Button
        ratingLabel = Label(addReviewWindow, text='Rating', fg="#f8f8f8", bg='#1e85d0',
                            font=("yu gothic ui", 14, 'bold'))
        ratingLabel.place(x=50, y=100)

        # Create Dropdown Menu
        drop = OptionMenu(addReviewWindow, clicked, *ratings, )
        drop.place(x=200, y=100)

        descriptionPopupLabel = Label(addReviewWindow, text='Description', fg="#f8f8f8", bg='#1e85d0',
                                      font=("yu gothic ui", 14, 'bold'))
        descriptionPopupLabel.place(x=50, y=150)

        descriptionTextEntry = Text(addReviewWindow, height=10, width=80)
        descriptionTextEntry.place(x=50, y=200)

        submitReview = Button(designFrame3, text='Submit', font=("yu gothic ui bold", 12),
                              bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                              cursor='hand2', height=2, width=20, command=lambda: submitReviewF(clicked.get(), descriptionTextEntry.get("1.0",END)))
        submitReview.place(x=50, y=420)

        cancelReviewPopUp = Button(designFrame3, text='Cancel', font=("yu gothic ui bold", 12),
                                   bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                   cursor='hand2', height=2, width=20, command=lambda: cancelButton())
        cancelReviewPopUp.place(x=250, y=420)

    viewItemWindow.mainloop()


def GUI6():
    reportsWindow = Tk()
    reportsWindow.rowconfigure(0, weight=1)
    reportsWindow.columnconfigure(0, weight=1)
    reportsWindow.state('zoomed')
    reportsWindow.resizable(0, 0)
    reportsWindow.title('Reports')

    reportIcon = PhotoImage(file='Images/main user.png')
    reportsWindow.iconphoto(True, reportIcon)

    question = Frame(reportsWindow)
    question.grid(row=0, column=0, sticky='nsew')

    # ============== Page Layout =====================

    reportsMainFrame = Listbox(question, bg='#0c71b9', width=500, height=60, highlightthickness=0, borderwidth=0)
    reportsMainFrame.place(x=0, y=0)

    reportsLabel = Label(question, text='Reports', font=('Arial', 40, 'bold'), bg='#0c71b9')
    reportsLabel.place(x=130, y=15)

    # Displaying Question One
    def questionOne():
        questionOnePopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionOnePopup.winfo_screenwidth()
        screenHeight = questionOnePopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionOnePopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionOnePopup.title('Question 1')
        questionOnePopup.iconbitmap('Images/show.png')  ######
        questionOnePopup.configure(background='#f8f8f8')
        questionOnePopup.resizable(0, 0)

        def exitButton():
            questionOnePopup.destroy()

        questionOneFrame = Listbox(questionOnePopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                   borderwidth=0)
        questionOneFrame.place(x=0, y=0)

        questionOneFrame2 = Listbox(questionOnePopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                    borderwidth=0)
        questionOneFrame2.place(x=0, y=75)

        QuestionOneTitle = Label(questionOneFrame, text="List the most expensive items in each category",
                                 font=('Arial', 20, 'bold'),
                                 bg='#2095e9')
        QuestionOneTitle.place(x=80, y=15)

        backButtonPopUp = Button(questionOneFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "List_Most_Expensive_Items"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionOneDisplay = ttk.Treeview(questionOneFrame2, selectmode=BROWSE)
        questionOneDisplay['show'] = 'headings'
        # Define number of columns
        questionOneDisplay['columns'] = (
            'ItemID', 'itemTitle', 'itemDescription', 'itemCategory', 'itemPrice'
        )
        questionOneDisplay.column("ItemID", width=120, minwidth=50, anchor=W)
        questionOneDisplay.column("itemTitle", width=120, minwidth=50, anchor=W)
        questionOneDisplay.column("itemDescription", width=120, minwidth=50, anchor=W)
        questionOneDisplay.column("itemCategory", width=120, minwidth=50, anchor=W)
        questionOneDisplay.column("itemPrice", width=120, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionOneDisplay.heading("ItemID", text="Item ID", anchor=W)
        questionOneDisplay.heading("itemTitle", text="Item Name", anchor=W)
        questionOneDisplay.heading("itemDescription", text="Description", anchor=W)
        questionOneDisplay.heading("itemCategory", text="Category", anchor=W)
        questionOneDisplay.heading("itemPrice", text="Price", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionOneDisplay.insert("", i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4]))
            i = i + 1
        questionOneDisplay.place(x=0, y=0)

    def questionTwo(cat1, cat2):
        questionTwoPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionTwoPopup.winfo_screenwidth()
        screenHeight = questionTwoPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionTwoPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionTwoPopup.title('Question 2')
        questionTwoPopup.iconbitmap('Images/show.png')  ######
        questionTwoPopup.configure(background='#f8f8f8')
        questionTwoPopup.resizable(0, 0)

        def exitButton():
            questionTwoPopup.destroy()

        questionTwoFrame = Listbox(questionTwoPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                   borderwidth=0)
        questionTwoFrame.place(x=0, y=0)

        questionTwoFrame2 = Listbox(questionTwoPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                    borderwidth=0)
        questionTwoFrame2.place(x=0, y=75)

        QuestionTwoTitle = Label(questionTwoFrame, text="List the users who posted at least two items that were posted"
                                                        " on the same day,\n one has a category of X, and another has "
                                                        "a category of Y.", font=('Arial', 12, 'bold'), bg='#2095e9')
        QuestionTwoTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionTwoFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Find_Users_With_Two_Items_Same_Day"
        params = (cat1, cat2)
        returned_result = execute_query(connect, procedure_name, params)
        questionTwoDisplay = ttk.Treeview(questionTwoFrame2, selectmode=BROWSE)
        questionTwoDisplay['show'] = 'headings'
        # Define number of columns
        questionTwoDisplay['columns'] = (
            'Category1UserName', 'itemCategory', 'ItemsPostedbyUserInCategory1', 'DateofListing', 'Category2UserName',
            'itemCategory', 'ItemsPostedbyUserInCategory2', 'DateofListing')

        # Assign dimensions
        questionTwoDisplay.column("Category1UserName", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("itemCategory", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("ItemsPostedbyUserInCategory1", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("DateofListing", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("Category2UserName", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("itemCategory", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("ItemsPostedbyUserInCategory2", width=50, minwidth=50, anchor=W)
        questionTwoDisplay.column("DateofListing", width=50, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionTwoDisplay.heading("Category1UserName", text="Category1UserName", anchor=W)
        questionTwoDisplay.heading("itemCategory", text="itemCategory", anchor=W)
        questionTwoDisplay.heading("ItemsPostedbyUserInCategory1", text="ItemsPostedbyUserInCategory1", anchor=W)
        questionTwoDisplay.heading("DateofListing", text="DateofListing", anchor=W)
        questionTwoDisplay.heading("Category2UserName", text="Category2UserName", anchor=W)
        questionTwoDisplay.heading("itemCategory", text="AitemCategory", anchor=W)
        questionTwoDisplay.heading("ItemsPostedbyUserInCategory2", text="ItemsPostedbyUserInCategory2", anchor=W)
        questionTwoDisplay.heading("DateofListing", text="DateofListing", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionTwoDisplay.insert("", i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
            i = i + 1

        questionTwoDisplay.place(x=0, y=0)

    def questionThree(usr):
        questionThreePopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionThreePopup.winfo_screenwidth()
        screenHeight = questionThreePopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionThreePopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionThreePopup.title('Question 3')
        questionThreePopup.iconbitmap('Images/show.png')  ######
        questionThreePopup.configure(background='#f8f8f8')
        questionThreePopup.resizable(0, 0)

        def exitButton():
            questionThreePopup.destroy()

        questionThreeFrame = Listbox(questionThreePopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                     borderwidth=0)
        questionThreeFrame.place(x=0, y=0)

        questionThreeFrame2 = Listbox(questionThreePopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                      borderwidth=0)
        questionThreeFrame2.place(x=0, y=75)

        QuestionThreeTitle = Label(questionThreeFrame, text="List all the items posted by user X, such that all the "
                                                            "comments are \"Excellent\" or \"good\" for these items",
                                   font=('Arial', 10, 'bold'),
                                   bg='#2095e9')
        QuestionThreeTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionThreeFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Find_Items_With_Positive_Comments"
        params = (usr,)
        returned_result = execute_query(connect, procedure_name, params)
        questionThreeDisplay = ttk.Treeview(questionThreeFrame2, selectmode=BROWSE)
        questionThreeDisplay['show'] = 'headings'
        # Define number of columns
        questionThreeDisplay['columns'] = (
            'ItemID', 'itemTitle', 'itemDescription', 'itemCategory', 'itemPrice', 'userName', 'DateofListing')

        # Assign dimensions
        questionThreeDisplay.column("ItemID", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("itemTitle", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("itemDescription", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("itemCategory", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("itemPrice", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("userName", width=100, minwidth=50, anchor=W)
        questionThreeDisplay.column("DateofListing", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionThreeDisplay.heading("ItemID", text="Item ID", anchor=W)
        questionThreeDisplay.heading("itemTitle", text="Item Name", anchor=W)
        questionThreeDisplay.heading("itemDescription", text="Description", anchor=W)
        questionThreeDisplay.heading("itemCategory", text="Category", anchor=W)
        questionThreeDisplay.heading("itemPrice", text="Price", anchor=W)
        questionThreeDisplay.heading("userName", text="Added By", anchor=W)
        questionThreeDisplay.heading("DateofListing", text="Created Date", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionThreeDisplay.insert("", i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
            i = i + 1

        questionThreeDisplay.place(x=0, y=0)

    def questionFour(dateSelected):
        questionFourPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionFourPopup.winfo_screenwidth()
        screenHeight = questionFourPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionFourPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionFourPopup.title('Question 4')
        questionFourPopup.iconbitmap('Images/show.png')  ######
        questionFourPopup.configure(background='#f8f8f8')
        questionFourPopup.resizable(0, 0)

        def exitButton():
            questionFourPopup.destroy()

        questionFourFrame = Listbox(questionFourPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                    borderwidth=0)
        questionFourFrame.place(x=0, y=0)

        questionFourFrame2 = Listbox(questionFourPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                     borderwidth=0)
        questionFourFrame2.place(x=0, y=75)

        QuestionFourTitle = Label(questionFourFrame, text="List the users who posted the most number of items on a specific date like 5/1/2023.",
                                  font=('Arial', 12, 'bold'),
                                  bg='#2095e9')
        QuestionFourTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionFourFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Find_Top_Users_On_Date"
        params = (dateSelected,)
        returned_result = execute_query(connect, procedure_name, params)
        questionFourDisplay = ttk.Treeview(questionFourFrame2, selectmode=BROWSE)
        questionFourDisplay['show'] = 'headings'
        # Define number of columns
        questionFourDisplay['columns'] = ('userName', 'DateofListing')

        # Assign dimensions
        questionFourDisplay.column("userName", width=100, minwidth=50, anchor=W)
        questionFourDisplay.column("DateofListing", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionFourDisplay.heading("userName", text="Added By", anchor=W)
        questionFourDisplay.heading("DateofListing", text="Created Date", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionFourDisplay.insert("", i, text="", values=(ro[0], ro[1]))
            i = i + 1

        questionFourDisplay.place(x=20, y=0)

    def questionFive(usr1, usr2):
        questionFIvePopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionFIvePopup.winfo_screenwidth()
        screenHeight = questionFIvePopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionFIvePopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionFIvePopup.title('Question 5')
        questionFIvePopup.iconbitmap('Images/show.png')  ######
        questionFIvePopup.configure(background='#f8f8f8')
        questionFIvePopup.resizable(0, 0)

        def exitButton():
            questionFIvePopup.destroy()

        questionFiveFrame = Listbox(questionFIvePopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                    borderwidth=0)
        questionFiveFrame.place(x=0, y=0)

        questionFiveFrame2 = Listbox(questionFIvePopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                     borderwidth=0)
        questionFiveFrame2.place(x=0, y=75)

        QuestionFiveTitle = Label(questionFiveFrame, text="List the other users who are favorited by both users X, and Y.",
                                  font=('Arial', 12, 'bold'),
                                  bg='#2095e9')
        QuestionFiveTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionFiveFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Get_Common_Favorites"
        params = (usr1, usr2)
        returned_result = execute_query(connect, procedure_name, params)
        questionFiveDisplay = ttk.Treeview(questionFiveFrame2, selectmode=BROWSE)
        questionFiveDisplay['show'] = 'headings'
        # Define number of columns
        questionFiveDisplay['columns'] = ('CommonFavorites')

        # Assign dimensions
        questionFiveDisplay.column("CommonFavorites", width=150, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionFiveDisplay.heading("CommonFavorites", text="Common Favorites", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionFiveDisplay.insert("", i, text="", values=(ro[0]))
            i = i + 1

        questionFiveDisplay.place(x=20, y=0)

    def questionSix():
        questionSixPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionSixPopup.winfo_screenwidth()
        screenHeight = questionSixPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionSixPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionSixPopup.title('Question 6')
        questionSixPopup.iconbitmap('Images/show.png')  ######
        questionSixPopup.configure(background='#f8f8f8')
        questionSixPopup.resizable(0, 0)

        def exitButton():
            questionSixPopup.destroy()

        questionSixFrame = Listbox(questionSixPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                   borderwidth=0)
        questionSixFrame.place(x=0, y=0)

        questionSixFrame2 = Listbox(questionSixPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                    borderwidth=0)
        questionSixFrame2.place(x=0, y=75)

        QuestionSixTitle = Label(questionSixFrame,
                                 text="Display all the users who never posted any \"excellent\" items",
                                 font=('Arial', 16, 'bold'), bg='#2095e9')
        QuestionSixTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionSixFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Users_With_No_Excellent_Items"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionSixDisplay = ttk.Treeview(questionSixFrame2, selectmode=BROWSE)
        questionSixDisplay['show'] = 'headings'
        # Define number of columns
        questionSixDisplay['columns'] = ('userName')

        # Assign dimensions
        questionSixDisplay.column("userName", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionSixDisplay.heading("userName", text="userName", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionSixDisplay.insert("", i, text="", values=(ro[0]))
            i = i + 1

        questionSixDisplay.place(x=20, y=0)

    def questionSeven():
        questionSevenPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionSevenPopup.winfo_screenwidth()
        screenHeight = questionSevenPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionSevenPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionSevenPopup.title('Question 7')
        questionSevenPopup.iconbitmap('Images/show.png')  ######
        questionSevenPopup.configure(background='#f8f8f8')
        questionSevenPopup.resizable(0, 0)

        def exitButton():
            questionSevenPopup.destroy()

        questionSevenFrame = Listbox(questionSevenPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                     borderwidth=0)
        questionSevenFrame.place(x=0, y=0)

        questionSevenFrame2 = Listbox(questionSevenPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                      borderwidth=0)
        questionSevenFrame2.place(x=0, y=75)

        QuestionSevenTitle = Label(questionSevenFrame,
                                   text="Display all the users who never posted a \"poor\" review.",
                                   font=('Arial', 16, 'bold'), bg='#2095e9')
        QuestionSevenTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionSevenFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Users_With_No_Poor_Reviews"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionSevenDisplay = ttk.Treeview(questionSevenFrame2, selectmode=BROWSE)
        questionSevenDisplay['show'] = 'headings'
        # Define number of columns
        questionSevenDisplay['columns'] = ('userName')

        # Assign dimensions
        questionSevenDisplay.column("userName", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionSevenDisplay.heading("userName", text="userName", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionSevenDisplay.insert("", i, text="", values=(ro[0]))
            i = i + 1

        questionSevenDisplay.place(x=20, y=0)

    def questionEight():
        questionEightPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionEightPopup.winfo_screenwidth()
        screenHeight = questionEightPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionEightPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionEightPopup.title('Question 8')
        questionEightPopup.iconbitmap('Images/show.png')  ######
        questionEightPopup.configure(background='#f8f8f8')
        questionEightPopup.resizable(0, 0)

        def exitButton():
            questionEightPopup.destroy()

        questionEightFrame = Listbox(questionEightPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                     borderwidth=0)
        questionEightFrame.place(x=0, y=0)

        questionEightFrame2 = Listbox(questionEightPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                      borderwidth=0)
        questionEightFrame2.place(x=0, y=75)

        QuestionEightTitle = Label(questionEightFrame, text="Display all the users who posted some reviews, but"
                                                            " each of them is \"poor\".", font=('Arial', 14, 'bold'),
                                   bg='#2095e9')
        QuestionEightTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionEightFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Users_With_Only_Poor_Reviews"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionEightDisplay = ttk.Treeview(questionEightFrame2, selectmode=BROWSE)
        questionEightDisplay['show'] = 'headings'
        # Define number of columns
        questionEightDisplay['columns'] = ('userName')

        # Assign dimensions
        questionEightDisplay.column("userName", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionEightDisplay.heading("userName", text="userName", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionEightDisplay.insert("", i, text="", values=(ro[0]))
            i = i + 1

        questionEightDisplay.place(x=20, y=0)

    def questionNine():
        questionNinePopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionNinePopup.winfo_screenwidth()
        screenHeight = questionNinePopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionNinePopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionNinePopup.title('Question 9')
        questionNinePopup.iconbitmap('Images/show.png')  ######
        questionNinePopup.configure(background='#f8f8f8')
        questionNinePopup.resizable(0, 0)

        def exitButton():
            questionNinePopup.destroy()

        questionNineFrame = Listbox(questionNinePopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                    borderwidth=0)
        questionNineFrame.place(x=0, y=0)

        questionNineFrame2 = Listbox(questionNinePopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                     borderwidth=0)
        questionNineFrame2.place(x=0, y=75)

        QuestionNineTitle = Label(questionNineFrame, text="Display those users such that each item they posted "
                                                          "so far never\n received any \"poor\" reviews.",
                                  font=('Arial', 14, 'bold'), bg='#2095e9')
        QuestionNineTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionNineFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Users_With_No_Poor_Items_Posted"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionNineDisplay = ttk.Treeview(questionNineFrame2, selectmode=BROWSE)
        questionNineDisplay['show'] = 'headings'
        # Define number of columns
        questionNineDisplay['columns'] = ('userName', 'poorItemsPosted')

        # Assign dimensions
        questionNineDisplay.column("userName", width=100, minwidth=50, anchor=W)
        questionNineDisplay.column("poorItemsPosted", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionNineDisplay.heading("userName", text="userName", anchor=W)
        questionNineDisplay.heading("poorItemsPosted", text="poorItemsPosted", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionNineDisplay.insert("", i, text="", values=(ro[0], ro[1]))
            i = i + 1

        questionNineDisplay.place(x=20, y=0)

    def questionTen():
        questionTenPopup = Toplevel()
        windowWidth = 800
        windowHeight = 500
        screenWidth = questionTenPopup.winfo_screenwidth()
        screenHeight = questionTenPopup.winfo_screenheight()
        positionTop = int(screenHeight / 4 - windowHeight / 4)
        positionRight = int(screenWidth / 2 - windowWidth / 2)
        questionTenPopup.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
        questionTenPopup.title('Question 10')
        questionTenPopup.iconbitmap('Images/show.png')  ######
        questionTenPopup.configure(background='#f8f8f8')
        questionTenPopup.resizable(0, 0)

        def exitButton():
            questionTenPopup.destroy()

        questionTenFrame = Listbox(questionTenPopup, bg='#1594ef', width=215, height=50, highlightthickness=0,
                                   borderwidth=0)
        questionTenFrame.place(x=0, y=0)

        questionTenFrame2 = Listbox(questionTenPopup, bg='#0c71b9', width=190, height=21, highlightthickness=0,
                                    borderwidth=0)
        questionTenFrame2.place(x=0, y=75)

        QuestionTenTitle = Label(questionTenFrame, text="List a user pair (A, B) such that they always gave each "
                                                        "other \"excellent\" reviews\n for every single item they posted.",
                                 font=('Arial', 14, 'bold'), bg='#2095e9')
        QuestionTenTitle.place(x=50, y=15)

        backButtonPopUp = Button(questionTenFrame, text='Back', font=("yu gothic ui bold", 12),
                                 bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                                 cursor='hand2', height=2, width=20, command=lambda: exitButton())
        backButtonPopUp.place(x=600, y=425)

        connect = create_db_connection()
        procedure_name = "Find_User_Pairs_With_Excellent_Reviews"
        params = ()
        returned_result = execute_query(connect, procedure_name, params)
        questionTenDisplay = ttk.Treeview(questionTenFrame2, selectmode=BROWSE)
        questionTenDisplay['show'] = 'headings'
        # Define number of columns
        questionTenDisplay['columns'] = ('User 1', 'User 2')

        # Assign dimensions
        questionTenDisplay.column("User 1", width=100, minwidth=50, anchor=W)
        questionTenDisplay.column("User 2", width=100, minwidth=50, anchor=W)

        # Assign headers to table columns
        questionTenDisplay.heading("User 1", text="User 1", anchor=W)
        questionTenDisplay.heading("User 2", text="User 2", anchor=W)

        i = 0
        for ro in returned_result:
            # print(ro)
            questionTenDisplay.insert("", i, text="", values=(ro[0], ro[1]))
            i = i + 1

        questionTenDisplay.place(x=20, y=0)

    # ============== TOP BUTTON LAYOUT ====================
    questionOneButton = Button(question, text='Question 1', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                               command=lambda: questionOne(), borderwidth=0, activebackground='#1b87d2',
                               cursor='hand2')
    questionOneButton.place(x=40, y=100)

    questionTwoLabel = Label(question, text="Category 1", fg="#a7a7a7",
                             font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionTwoLabel.place(x=140, y=150)
    questionTwoCategory1 = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionTwoCategory1.place(x=250, y=150)

    questionTwoLabel2 = Label(question, text="Category 2'", fg="#a7a7a7",
                              font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionTwoLabel2.place(x=525, y=150)
    questionTwoCategory2 = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionTwoCategory2.place(x=625, y=150)

    questionTwoButton = Button(question, text='Question 2', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                               command=lambda: questionTwo(questionTwoCategory1.get(), questionTwoCategory2.get()),
                               borderwidth=0, activebackground='#1b87d2',
                               cursor='hand2')
    questionTwoButton.place(x=40, y=150)

    questionThreeLabel = Label(question, text="User Name:'", fg="#a7a7a7", font=("yu gothic ui semibold", 12),
                               highlightthickness=2)
    questionThreeLabel.place(x=140, y=200)
    questionThreeDate = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionThreeDate.place(x=250, y=200)

    questionThreeButton = Button(question, text='Question 3', font=("yu gothic ui bold", 12), bg='#f8f8f8',
                                 fg="#89898b",
                                 command=lambda: questionThree(questionThreeDate.get()), borderwidth=0,
                                 activebackground='#1b87d2',
                                 cursor='hand2')
    questionThreeButton.place(x=40, y=200)

    questionFourButton = Button(question, text='Question 4', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: questionFour(questionFourDate.get()), borderwidth=0,
                                activebackground='#1b87d2',
                                cursor='hand2')
    questionFourButton.place(x=40, y=250)

    questionFourLabel = Label(question, text="Date format 'yyyy-mm-dd'", fg="#a7a7a7",
                              font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFourLabel.place(x=140, y=250)
    questionFourDate = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFourDate.place(x=350, y=250)

    questionFiveLabel = Label(question, text="User 1", fg="#a7a7a7",
                              font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFiveLabel.place(x=140, y=300)
    questionFiveUser1 = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFiveUser1.place(x=200, y=300)

    questionFiveLabel2 = Label(question, text="User 2'", fg="#a7a7a7",
                               font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFiveLabel2.place(x=400, y=300)
    questionFiveUser2 = Entry(question, fg="black", font=("yu gothic ui semibold", 12), highlightthickness=2)
    questionFiveUser2.place(x=480, y=300)

    questionFiveButton = Button(question, text='Question 5', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: questionFive(questionFiveUser1.get(), questionFiveUser2.get()),
                                borderwidth=0, activebackground='#1b87d2',
                                cursor='hand2')
    questionFiveButton.place(x=40, y=300)

    questionSixButton = Button(question, text='Question 6', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                               command=lambda: questionSix(), borderwidth=0, activebackground='#1b87d2',
                               cursor='hand2')
    questionSixButton.place(x=40, y=350)

    questionSevenButton = Button(question, text='Question 7', font=("yu gothic ui bold", 12), bg='#f8f8f8',
                                 fg="#89898b",
                                 command=lambda: questionSeven(), borderwidth=0, activebackground='#1b87d2',
                                 cursor='hand2')
    questionSevenButton.place(x=40, y=400)

    questionEightButton = Button(question, text='Question 8', font=("yu gothic ui bold", 12), bg='#f8f8f8',
                                 fg="#89898b",
                                 command=lambda: questionEight(), borderwidth=0, activebackground='#1b87d2',
                                 cursor='hand2')
    questionEightButton.place(x=40, y=450)

    questionNineButton = Button(question, text='Question 9', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                                command=lambda: questionNine(), borderwidth=0, activebackground='#1b87d2',
                                cursor='hand2')
    questionNineButton.place(x=40, y=500)

    questionTenButton = Button(question, text='Question 10', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                               command=lambda: questionTen(), borderwidth=0, activebackground='#1b87d2',
                               cursor='hand2')
    questionTenButton.place(x=40, y=550)

    def returnToPortal():
        reportsWindow.destroy()
        GUI2()

    backButtonPopUp = Button(question, text='Back to Portal', font=("yu gothic ui bold", 12),
                             bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                             cursor='hand2', height=2, width=20, command=lambda: returnToPortal())
    backButtonPopUp.place(x=1000, y=740)

    reportsWindow.mainloop()


# Function to create a database connection
def create_db_connection():
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        var_cursor = conn.cursor()

        # Check if the database already exists
        var_cursor.execute("SHOW DATABASES LIKE %s", (database,))
        result = var_cursor.fetchone()

        if result:
            print(f"The database '{database}' already exists.")
        else:
            # Create database if it doesn't exist
            var_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"The database '{database}' has been created successfully")

        conn.close()  # Close the connection before connecting to the specific database

        conn = mysql.connector.connect(
            host=host, database=database, user=user, password=password
        )
        return conn

    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None


# Function to execute SQL queries
def execute_query(conn, query, data=None) -> any:
    try:
        outResult = None

        var_cursor = conn.cursor()
        var_cursor.callproc(query, data)

        for result in var_cursor.stored_results():
            outResult = result.fetchall()

        # print(outResult)
        conn.commit()
        return outResult

    except mysql.connector.Error as err:
        if str(err).find('userdetails.PRIMARY'):
            messagebox.showinfo(title="Error", message="Please enter unique username and/or email address. Try again")
        # messagebox.showerror("Database Error", f"Error: {err}")
        return False


# Function to call the stored procedure for getting all user details
def get_all_user_details(conn) -> any:
    try:
        # Define the stored procedure name
        procedure_name = "get_alluserDetails"
        params = ()

        returned_result = execute_query(conn, procedure_name, params)
        # print(returned_result)

        # Call the stored procedure using the call_stored_procedure function
        if returned_result:
            return returned_result

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        conn.close()


# Function to display user details
def display_user_details():
    conn = create_db_connection()
    user_details = get_all_user_details(conn)
    if user_details:
        user_details_str = "\n".join(
            [
                f"Username: {row[0]} \n Full Name: {row[1]} \n Email ID: {row[2]} \n"
                for row in user_details
            ]
        )
        messagebox.showinfo("User Details", user_details_str)


# Function to call the validation procedure
def validate_user_details(username, passWd, email):
    conn = create_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.callproc("check_userDetails", (username, passWd, email, None))
            for result in cursor.stored_results():
                validation_result = result.fetchone()[0]
            return validation_result
        except mysql.connector.Error as err:
            messagebox.showerror(
                "Stored Procedure Error", f"Error calling stored procedure: {err}"
            )
            return None
        finally:
            conn.close()
    else:
        return None


# Function to check if input contains potentially harmful characters
def is_safe_input(input_str):
    # Use regular expressions to check for harmful characters
    pattern = re.compile(r'[;\'"\\]')
    return not pattern.search(input_str)


def enterPortal():
    startWindow.destroy()
    GUI2()


def loginF(uEntry, pEntry):
    global userNameGlobal
    userNameGlobal = uEntry
    conn = create_db_connection()
    p_name = "p_login_user"
    # print(a.get())
    OutResult = None
    params = (uEntry, pEntry, OutResult)
    # Check if username and password to login
    # Validate username and password
    returned_result = execute_query(conn, p_name, params)
    returned_result_str = " ".join(returned_result[0])

    if returned_result_str == "User Exists":
        messagebox.showinfo(
            message=f"Welcome {uEntry}!"
        )
        enterPortal()
    elif "User Password Mismatch." in returned_result_str:
        messagebox.showinfo(
            message="Password does not match. Try again"
        )
    else:
        messagebox.showinfo(title="Error", message="User Does Not Exist!")


# Sign-Up Window
startWindow = Tk()
startWindow.rowconfigure(0, weight=1)
startWindow.columnconfigure(0, weight=1)
startWindow.state('zoomed')
startWindow.resizable(0, 0)
startWindow.title('Login and Registration Page')

# Window Icon Photo
windowIcon = PhotoImage(file='Images/Hello.png')
startWindow.iconphoto(True, windowIcon)

LoginPage = Frame(startWindow)
RegistrationPage = Frame(startWindow)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)

# ==================== LOGIN PAGE ==============

designFrame1 = Listbox(LoginPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
designFrame1.place(x=0, y=0)

designFrame2 = Listbox(LoginPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
designFrame2.place(x=676, y=0)

designFrame3 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame3.place(x=75, y=106)

designFrame4 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame4.place(x=676, y=106)

# ====== Email ====================
userNameEntryL = Entry(designFrame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
userNameEntryL.place(x=134, y=170, width=256, height=34)
userNameEntryL.config(highlightbackground="black", highlightcolor="black")
emailLabel = Label(designFrame4, text='• Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
emailLabel.place(x=130, y=140)

# ==== Password ==================
passwordEntry1 = Entry(designFrame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
passwordEntry1.place(x=134, y=250, width=256, height=34)
passwordEntry1.config(highlightbackground="black", highlightcolor="black")
passwordLabel = Label(designFrame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
passwordLabel.place(x=130, y=220)


# function for show and hide password
def password_command():
    if passwordEntry1.cget('show') == '•':
        passwordEntry1.config(show='')
    else:
        passwordEntry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(designFrame4, bg='#f8f8f8', command=password_command, text='show password')
checkButton.place(x=140, y=288)

# ========= Buttons ===============
SignUpButton = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2',
                      cursor='hand2')
SignUpButton.place(x=1100, y=175)

# ===== Welcome Label ==============
welcomeLabel = Label(designFrame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcomeLabel.place(x=130, y=15)

# ======= top Login Button =========
loginButton = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                     borderwidth=0, activebackground='#1b87d2', cursor='hand2')
loginButton.place(x=845, y=175)

loginLine = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
loginLine.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = Button(designFrame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2',
                   command=lambda: loginF(userNameEntryL.get(), passwordEntry1.get()))
loginBtn1.place(x=133, y=340, width=256, height=50)

# ======= ICONS =================

# ===== Email icon =========
emailIcon = Image.open('Images/mail.png')
emailIcon = emailIcon.resize((20, 20))
photo = ImageTk.PhotoImage(emailIcon)
emailIconLabel = Label(designFrame4, image=photo, bg='#f8f8f8')
emailIconLabel.image = photo
emailIconLabel.place(x=105, y=174)

# ===== password icon =========
passwordIcon = Image.open('Images/password.png')
passwordIcon = passwordIcon.resize((20, 20))
photo = ImageTk.PhotoImage(passwordIcon)
passwordIconLabel = Label(designFrame4, image=photo, bg='#f8f8f8')
passwordIconLabel.image = photo
passwordIconLabel.place(x=105, y=254)

# ===== picture icon =========
pictureIcon = Image.open('Images/main user.png')
pictureIcon = pictureIcon.resize((60, 60))
photo = ImageTk.PhotoImage(pictureIcon)
pictureIconLabel = Label(designFrame4, image=photo, bg='#f8f8f8')
pictureIconLabel.image = photo
pictureIconLabel.place(x=280, y=5)

# ===== Left Side Picture ============
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((500, 500))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame3, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=50, y=10)


# === FORGOT PASSWORD  PAGE =========================================================================================

def forgot_password():
    win = Toplevel()
    windowWidth = 350
    windowHeight = 350
    screenWidth = win.winfo_screenwidth()
    screenHeight = win.winfo_screenheight()
    positionTop = int(screenHeight / 4 - windowHeight / 4)
    positionRight = int(screenWidth / 2 - windowWidth / 2)
    win.geometry(f'{windowWidth}x{windowHeight}+{positionRight}+{positionTop}')
    win.title('Forgot Password')
    win.iconbitmap('Images/show.png')  ######
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # ====== Email ====================
    emailEntry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    emailEntry2.place(x=40, y=30, width=256, height=34)
    emailEntry2.config(highlightbackground="black", highlightcolor="black")
    emailLabel2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                        font=("yu gothic ui", 11, 'bold'))
    emailLabel2.place(x=40, y=0)

    # ====  New Password ==================
    newPasswordEntry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    newPasswordEntry.place(x=40, y=110, width=256, height=34)
    newPasswordEntry.config(highlightbackground="black", highlightcolor="black")
    newPasswordLabel = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    newPasswordLabel.place(x=40, y=80)

    # ====  Confirm Password ==================
    confirmPasswordEntry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirmPasswordEntry.place(x=40, y=190, width=256, height=34)
    confirmPasswordEntry.config(highlightbackground="black", highlightcolor="black")
    confirmPasswordLabel = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                 font=("yu gothic ui", 11, 'bold'))
    confirmPasswordLabel.place(x=40, y=160)

    # ======= Update password Button ============
    updatePassword = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                            cursor='hand2', activebackground='#1b87d2')
    updatePassword.place(x=40, y=240, width=256, height=50)


forgotPassword = Button(designFrame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=290, y=290)


# ==================== REGISTRATION PAGE ==============================================================================

def signUpMember(uName, fName, lName, passW, conPass, eMail):
    user_name = uName
    user_password = passW
    user_first_name = fName
    user_last_name = lName
    user_emailid = eMail
    user_confirm_password = conPass
    outResult = None

    if user_confirm_password != user_password:
        messagebox.showwarning(title="Error", message="Passwords do not match. Try again")
        return

    # Validate the username and email for SQL injection
    if not is_safe_input(user_name) or not is_safe_input(user_emailid):
        messagebox.showerror(
            "Invalid Input", "Invalid characters in username or email."
        )
        return

    conn = create_db_connection()
    if conn:
        try:
            # Define the stored procedure name
            procedure_name = "save_userDetails"

            # Create a tuple containing the input parameters for the stored procedure
            params = (
                user_name,
                user_password,
                user_first_name,
                user_last_name,
                user_emailid,
                outResult,
            )

            query = procedure_name
            returned_result = execute_query(conn, query, params)
            returned_result_str = " ".join(returned_result[0])

            # Call the stored procedure using the execute_query function
            if returned_result_str == "Record Inserted":
                messagebox.showinfo(
                    "Signup Successful", "Signup successful! Record Inserted"
                )
                messagebox.showinfo(
                    "Signup Successful", "Please login"
                )
            elif "Injection" in returned_result_str:
                messagebox.showinfo(
                    message=f"SQL {returned_result_str}. SignUp Unsuccessful. Please Re-Enter!"
                )
            else:
                messagebox.showinfo("SignUp Unsuccessful.")
        finally:
            conn.close()

    conn.close()


designFrame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
designFrame5.place(x=0, y=0)

designFrame6 = Listbox(RegistrationPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
designFrame6.place(x=676, y=0)

designFrame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame7.place(x=75, y=106)

designFrame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame8.place(x=676, y=106)

# ==== User Name =============
userNameEntryR = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
userNameEntryR.place(x=50, y=150, width=200, height=34)
userNameEntryR.config(highlightbackground="black", highlightcolor="black")
userNameLabelR = Label(designFrame8, text='•Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
userNameLabelR.place(x=50, y=120)

# ==== First Name =======
firstNameEntryR = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
firstNameEntryR.place(x=284, y=150, width=286, height=34)
firstNameEntryR.config(highlightbackground="black", highlightcolor="black")
firstNameLabelR = Label(designFrame8, text='•First Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
firstNameLabelR.place(x=280, y=120)

# ==== First Name =======
lastNameEntryR = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
lastNameEntryR.place(x=284, y=220, width=286, height=34)
lastNameEntryR.config(highlightbackground="black", highlightcolor="black")
lastNameLabelR = Label(designFrame8, text='•Last Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
lastNameLabelR.place(x=280, y=190)

# ======= Email ===========
emailEntryR = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
emailEntryR.place(x=284, y=290, width=286, height=34)
emailEntryR.config(highlightbackground="black", highlightcolor="black")
emailLabel = Label(designFrame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
emailLabel.place(x=280, y=260)

# ====== Password =========
passwordEntry2 = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
passwordEntry2.place(x=284, y=365, width=286, height=34)
passwordEntry2.config(highlightbackground="black", highlightcolor="black")
passwordLabel2 = Label(designFrame8, text='• Password2', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
passwordLabel2.place(x=280, y=335)


def password_command2():
    if passwordEntry2.cget('show') == '•':
        passwordEntry2.config(show='')
    else:
        passwordEntry2.config(show='•')


checkButton = Checkbutton(designFrame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=450, y=400)

# ====== Confirm Password =============
confirmPasswordEntry2 = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•',
                              highlightthickness=2)
confirmPasswordEntry2.place(x=284, y=430, width=286, height=34)
confirmPasswordEntry2.config(highlightbackground="black", highlightcolor="black")
confirmPasswordLabel2 = Label(designFrame8, text='• Confirm Password2', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
confirmPasswordLabel2.place(x=280, y=400)

# ========= Top Label Change Buttons ====================
SignUpButton = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUpButton.place(x=1100, y=175)

signUpLine = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
signUpLine.place(x=1100, y=203)

# ===== Welcome Label ==================
welcomeLabel = Label(designFrame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcomeLabel.place(x=130, y=15)

# ========= Login Button =========
loginButton = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                     borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
loginButton.place(x=845, y=175)

# ==== SIGN UP down button ============
signUp2 = Button(designFrame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2',
                 command=lambda: signUpMember(userNameEntryR.get(), firstNameEntryR.get(),
                                              lastNameEntryR.get(), passwordEntry2.get(),
                                              confirmPasswordEntry2.get(), emailEntryR.get()))
signUp2.place(x=285, y=480, width=286, height=40)

# ===== password icon =========
passwordIcon = Image.open('Images/password.png')
passwordIcon = passwordIcon.resize((20, 20))
photo = ImageTk.PhotoImage(passwordIcon)
passwordIconLabel = Label(designFrame8, image=photo, bg='#f8f8f8')
passwordIconLabel.image = photo
passwordIconLabel.place(x=255, y=300)

# ===== confirm password icon =========
confirmPassword_icon = Image.open('Images/confirm password.png')
confirmPassword_icon = confirmPassword_icon.resize((20, 20))
photo = ImageTk.PhotoImage(confirmPassword_icon)
confirmPasswordIconLabel = Label(designFrame8, image=photo, bg='#f8f8f8')
confirmPasswordIconLabel.image = photo
confirmPasswordIconLabel.place(x=255, y=390)

# ===== Email icon =========
emailIcon = Image.open('Images/mail.png')
emailIcon = emailIcon.resize((20, 20))
photo = ImageTk.PhotoImage(emailIcon)
emailIconLabel = Label(designFrame8, image=photo, bg='#f8f8f8')
emailIconLabel.image = photo
emailIconLabel.place(x=255, y=225)

# ===== Full Name icon =========
nameIcon = Image.open('Images/name.png')
nameIcon = nameIcon.resize((20, 20))
photo = ImageTk.PhotoImage(nameIcon)
nameIconLabel = Label(designFrame8, image=photo, bg='#f8f8f8')
nameIconLabel.image = photo
nameIconLabel.place(x=252, y=153)

# ===== picture icon =========
pictureIcon = Image.open('Images/main user.png')
pictureIcon = pictureIcon.resize((60, 60))
photo = ImageTk.PhotoImage(pictureIcon)
pictureIconLabel = Label(designFrame8, image=photo, bg='#f8f8f8')
pictureIconLabel.image = photo
pictureIconLabel.place(x=280, y=5)

# ===== Left Side Picture ============
sideImage = Image.open('Images/left pic.png')
sideImage = sideImage.resize((500, 500))
photo = ImageTk.PhotoImage(sideImage)
sideIconLabel = Label(designFrame7, image=photo, bg='#1e85d0')
sideIconLabel.image = photo
sideIconLabel.place(x=50, y=10)

startWindow.mainloop()
