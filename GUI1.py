import os
from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module


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



def enterPortal():
    startWindow.destroy()
    os.system('python GUI2.py')



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
userNameEntry = Entry(designFrame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
userNameEntry.place(x=134, y=170, width=256, height=34)
userNameEntry.config(highlightbackground="black", highlightcolor="black")
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
                      command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
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
                   cursor='hand2', activebackground='#1b87d2', command=enterPortal)
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
    win.iconbitmap('Images/show.png') ######
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

designFrame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
designFrame5.place(x=0, y=0)

designFrame6 = Listbox(RegistrationPage, bg='#1e85d0', width=150, height=50, highlightthickness=0, borderwidth=0)
designFrame6.place(x=676, y=0)

designFrame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame7.place(x=75, y=106)

designFrame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
designFrame8.place(x=676, y=106)

# ==== Full Name =======
nameEntry = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
nameEntry.place(x=284, y=150, width=286, height=34)
nameEntry.config(highlightbackground="black", highlightcolor="black")
nameLabel = Label(designFrame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
nameLabel.place(x=280, y=120)

# ======= Email ===========
userNameEntry = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
userNameEntry.place(x=284, y=220, width=286, height=34)
userNameEntry.config(highlightbackground="black", highlightcolor="black")
emailLabel = Label(designFrame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
emailLabel.place(x=280, y=190)

# ====== Password =========
passwordEntry = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
passwordEntry.place(x=284, y=295, width=286, height=34)
passwordEntry.config(highlightbackground="black", highlightcolor="black")
passwordLabel = Label(designFrame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                      font=("yu gothic ui", 11, 'bold'))
passwordLabel.place(x=280, y=265)


def password_command2():
    if passwordEntry.cget('show') == '•':
        passwordEntry.config(show='')
    else:
        passwordEntry.config(show='•')



checkButton = Checkbutton(designFrame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)


# ====== Confirm Password =============
confirmPasswordEntry = Entry(designFrame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
confirmPasswordEntry.place(x=284, y=385, width=286, height=34)
confirmPasswordEntry.config(highlightbackground="black", highlightcolor="black")
confirmPasswordLabel = Label(designFrame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                             font=("yu gothic ui", 11, 'bold'))
confirmPasswordLabel.place(x=280, y=355)

# ========= Buttons ====================
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
                 cursor='hand2', activebackground='#1b87d2', command=enterPortal)
signUp2.place(x=285, y=435, width=286, height=50)

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