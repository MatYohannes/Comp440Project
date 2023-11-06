import os
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


def initializeDB():
    messagebox.showinfo(title="Success", message="Database initialized!")


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

    def closeProgram():
        portalPage.quit()

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
                           cursor='hand2', height=2, width=30, command=None)
    reportsButton.place(x=100, y=450)

    InitializeDB = Button(portal, text='Initialize DataBase', font=("yu gothic ui bold", 12),
                          bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                          cursor='hand2', height=2, width=30, command=initializeDB)
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
            print(returned_result)
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

    def addReview():
        searchWindow.destroy()
        GUI5()

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
    searchDisplay = ttk.Treeview(searchBoxDisplay)
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


    #def select_item(searchDisplay, event):


    #searchDisplay.bind('<ButtonRelease-1>', select_item)

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

    addReviewButton2 = Button(designFrame1, text='Add Review', font=("yu gothic ui bold", 12),
                              bg='#1b87d2', fg="#f8f8f8", borderwidth=1, activebackground='#1b87d2',
                              cursor='hand2', height=2, width=20, command=lambda: addReview())  # add parameters
    addReviewButton2.place(x=1000, y=270)

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
        categorySearchDisplay = ttk.Treeview(designFrame4)
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


def GUI5():
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
    categoryLabel = Label(designFrame1, text='Description:', fg="#f8f8f8", bg='#1e85d0',
                          font=("yu gothic ui", 14, 'bold'))
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
    createDateLabel = Label(designFrame1, text='Created Date:', fg="#f8f8f8", bg='#1e85d0',
                            font=("yu gothic ui", 14, 'bold'))
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
        ratingLabel = Label(addReviewWindow, text='Rating', fg="#f8f8f8", bg='#1e85d0',
                            font=("yu gothic ui", 14, 'bold'))
        ratingLabel.place(x=50, y=100)

        # Create Dropdown Menu
        drop = OptionMenu(addReviewWindow, clicked, *ratings, )
        drop.place(x=200, y=100)

        descriptionPopupLabel = Label(addReviewWindow, text='Description', fg="#f8f8f8", bg='#1e85d0',
                                      font=("yu gothic ui", 14, 'bold'))
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
