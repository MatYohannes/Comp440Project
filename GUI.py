from tkinter import *

# Create the main frame
# root is the master frame
root = Tk()
root.title("Login")
# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("350x300")
root.geometry("+{}+{}".format(positionRight-150, positionDown-150))
# Setting Grid Dimensions
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
# Project Name
businessName = "<Insert Name>"


# Sign-Up Window
def signUp():
    root.destroy()
    signUpWindow = Tk()
    signUpWindow.title("Sign Up")
    # The dimensions of the window
    signUpWindow.geometry("450x250+510+100")
    # Centering the Sign Up Window
    signUpWindow.geometry("+{}+{}".format(positionRight - 150, positionDown - 150))

    # Create Global Variables for text box names
    # Variables are global for use with functions
    global userName
    global password
    global firstName
    global lastName
    global email

    # Sign Up Header
    Label(signUpWindow, text="Please fill the following fields").grid(row=0, column=0)

    # Create Text Boxes
    userName = Entry(signUpWindow, width=30).grid(row=1, column=1, padx=20, pady=(10, 0))
    password = Entry(signUpWindow, width=30).grid(row=2, column=1)
    firstName = Entry(signUpWindow, width=30).grid(row=3, column=1)
    lastName = Entry(signUpWindow, width=30).grid(row=4, column=1)
    email = Entry(signUpWindow, width=30).grid(row=5, column=1)

    # Create text box labels
    userNameLabel = Label(signUpWindow, text="First Name").grid(row=1, column=0, pady=(10, 0))
    l_name_label_editor = Label(signUpWindow, text="Last Name").grid(row=2, column=0)
    address_label_editor = Label(signUpWindow, text="Address").grid(row=3, column=0)
    city_label_editor = Label(signUpWindow, text="City").grid(row=4, column=0)
    state_label_editor = Label(signUpWindow, text="State").grid(row=5, column=0)

    # Create a Save Button to Save edited Record
    signUp = Button(signUpWindow, text="Submit user Account", ).grid(row=7, column=0, columnspan=2, padx=5, pady=5, ipadx=75)
    quitProgram = Button(signUpWindow, text="Exit Program").grid(row=8, column=0, columnspan=2, padx=5, pady=10, ipadx=100)


# Login Page
# Header
Label(root, text="Welcome to " + businessName, borderwidth=2, background="pink",
      relief="groove").grid(row=0, column=1, columnspan=2, padx=10, pady=20, sticky="S")
# user_name
Label(root, text="Username").grid(row=1, column=0, padx=20, pady=10)
# user_password
Label(root, text="Password").grid(row=2, column=0, padx=20)
# login_button
Button(root, text="Login", height=2, width=8).grid(row=3, column=0, columnspan=2)
# Signup_button
Button(root, text="Sign Up", height=2, width=8, command=signUp).grid(row=3, column=2)
# input field for username
Entry(root, width=30).grid(row=1, column=1, columnspan=2)
# input field for password
Entry(root, width=30).grid(row=2, column=1, columnspan=2)

root.mainloop()
