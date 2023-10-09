import tkinter as tk
from tkinter import Button, messagebox
# from argon2 import Parameters
import mysql.connector
import re

# Define your MySQL database connection parameters
host = "localhost"
database = "comp440_database_project"
user = "root"
password = ""  # enter password


def onClose():
    root.destroy()
    root.mainloop()


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
def validate_user_details(username, password, email):
    conn = create_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.callproc("check_userDetails", (username, password, email, None))
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


# Create the main frame
root = tk.Tk()
root.title("Login")
# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("400x300")
root.geometry("+{}+{}".format(positionRight - 150, positionDown - 150))
# Setting Grid Dimensions
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
# Project Name
businessName = "COMP 440 Database Project - Group 5"


# Login Fucntion to enter system
def loginF(uEntry, pEntry):
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
    elif "User Password Mismatch." in returned_result_str:
        messagebox.showinfo(
            message="Password does not match. Try again"
        )
    else:
        messagebox.showinfo(title="Error", message="User Does Not Exist!")


# Sign-Up Window
def signUp():
    root.destroy()

    def signup_clicked():
        user_name = userName.get()
        user_password = userPassword.get()
        user_first_name = user_firstName.get()
        user_last_name = user_lastName.get()
        user_emailid = user_emailID.get()
        outResult = None

        if userPaswordConfirmation.get() != userPassword.get():
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
                elif "Injection" in returned_result_str:
                    messagebox.showinfo(
                        message=f"SQL {returned_result_str}. SignUp Unsuccessful. Please Re-Enter!"
                    )
                else:
                    messagebox.showinfo("SignUp Unsuccessful.")
            finally:
                conn.close()

        conn.close()

    signUpWindow = tk.Tk()
    signUpWindow.title("Sign Up")
    # The dimensions of the window
    signUpWindow.geometry("450x250+510+100")
    # Centering the Sign Up Window
    signUpWindow.geometry("+{}+{}".format(positionRight - 150, positionDown - 150))

    # Create Global Variables for text box names
    # Variables are global for use with functions
    global userName
    global userPassword
    global userPaswordConfirmation
    global user_firstName
    global user_lastName
    global user_emailID

    global userEntry
    global passwordEntry

    # Sign Up Header
    tk.Label(signUpWindow, text="Please fill the following fields to Sign Up").grid(
        row=0, column=0
    )

    # Create Text Boxes
    userName = tk.Entry(signUpWindow, width=30)
    userPassword = tk.Entry(signUpWindow, width=30)
    userPaswordConfirmation = tk.Entry(signUpWindow, width=30)
    user_firstName = tk.Entry(signUpWindow, width=30)
    user_lastName = tk.Entry(signUpWindow, width=30)
    user_emailID = tk.Entry(signUpWindow, width=30)

    userName.grid(row=1, column=1, padx=20, pady=(10, 0))
    userPassword.grid(row=2, column=1)
    userPaswordConfirmation.grid(row=3, column=1)
    user_firstName.grid(row=4, column=1)
    user_lastName.grid(row=5, column=1)
    user_emailID.grid(row=6, column=1)

    # Create text box labels
    tk.Label(signUpWindow, text="User Name").grid(row=1, column=0, pady=(10, 0))
    tk.Label(signUpWindow, text="Password").grid(row=2, column=0)
    tk.Label(signUpWindow, text="Confirm Password").grid(row=3, column=0)
    tk.Label(signUpWindow, text="First Name").grid(row=4, column=0)
    tk.Label(signUpWindow, text="Last Name").grid(row=5, column=0)
    tk.Label(signUpWindow, text="Email ID").grid(row=6, column=0)

    # Create a Save Button to Save edited Record
    tk.Button(signUpWindow, text="Submit user Account", command=signup_clicked).grid(
        row=7, column=0, columnspan=2, padx=5, pady=5, ipadx=75
    )
    # tk.Button(signUpWindow, text="Back", command=lambda: root.onClose()).grid(row=9, column=0)
    tk.Button(signUpWindow, text="Exit Program", command=signUpWindow.quit).grid(
        row=8, column=0, columnspan=2, padx=5, pady=10, ipadx=100
    )


# Login Page
# Header
tk.Label(
    root,
    text="Welcome to " + businessName,
    borderwidth=2,
    background="pink",
    relief="groove",
).grid(row=0, column=1, columnspan=2, padx=10, pady=20, sticky="S")
# user_name
tk.Label(root, text="Username").grid(row=1, column=0, padx=20, pady=10)
# user_password
tk.Label(root, text="Password").grid(row=2, column=0, padx=20)
# login_button
tk.Button(root, text="Login", height=2, width=8,
          command=lambda: loginF(userEntry.get(), passwordEntry.get())).grid(row=3, column=0, columnspan=2)
# Signup_button
tk.Button(root, text="Sign Up", height=2, width=8, command=signUp).grid(row=3, column=2)
# input field for username

userEntry = tk.Entry(root, width=30)
userEntry.grid(row=1, column=1, columnspan=2)
# input field for password
passwordEntry = tk.Entry(root, width=30)
passwordEntry.grid(row=2, column=1, columnspan=2)

# Add a button to trigger fetching and displaying user details
Button(
    root, text="Get User Details", height=2, width=15, command=display_user_details
).grid(row=4, column=0, columnspan=3)

root.mainloop()
