from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import mysql.connector as sk
import os
from datetime import datetime
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import shutil

# Import your deep learning model module
import dr_model  # Make sure dr_model.py is in the same folder

# Load the model once at startup
model = dr_model.load_model()
print("Model loaded successfully")

# Database connection
connection = sk.connect(
    host="localhost",
    user="root",
    password="root",
    database="DRDD",
    charset="utf8"
)
sql = connection.cursor()

# Global variable to track logged-in user
logged_in_user_id = None

# Tkinter GUI root
root = Tk()
root.geometry('900x600')
root.title("Diabetic Retinopathy Early Detection System")

# Load and set the background image
bg_image_path = "C:/Users/prema/Downloads/eye_background.jpg"  # Replace with your image path
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((900, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label to hold the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Make the image fill the entire window

# Variables for user credentials
username_var = StringVar()
password_var = StringVar()

# Helper functions
def clear_frame():
    """Clears all widgets from the main frame."""
    for widget in root.winfo_children():
        widget.destroy()


# Navigation Screens
def show_login_screen():
    """Displays the login screen."""
    clear_frame()

    # Title
    Label(root, text="DR Early Detection System", font=('Arial', 28, 'bold'), bg='#f0f8ff', fg='#005b96').pack(pady=30)

    # Center Card for Form
    form_frame = Frame(root, bg='white', width=400, height=250)
    form_frame.pack(pady=20)
    form_frame.pack_propagate(False)

    # Username Entry
    Label(form_frame, text="Username:", font=('Arial', 14), bg='white', fg='#333').pack(pady=10, anchor=W, padx=20)
    username_entry = Entry(form_frame, textvariable=username_var, font=('Arial', 14), width=25, bd=2, relief="solid")
    username_entry.pack(pady=5, padx=20)

    # Password Entry
    Label(form_frame, text="Password:", font=('Arial', 14), bg='white', fg='#333').pack(pady=10, anchor=W, padx=20)
    password_entry = Entry(form_frame, textvariable=password_var, font=('Arial', 14), width=25, bd=2, relief="solid", show="*")
    password_entry.pack(pady=5, padx=20)

    # Buttons
    button_frame = Frame(form_frame, bg='white')
    button_frame.pack(pady=20)

    login_btn = Button(button_frame, text="Login", font=('Arial', 12, 'bold'), bg='#005b96', fg='white', command=login, width=12)
    login_btn.grid(row=0, column=0, padx=10)
    
    signup_btn = Button(button_frame, text="Signup", font=('Arial', 12, 'bold'), bg='#0077c2', fg='white', command=signup, width=12)
    signup_btn.grid(row=0, column=1, padx=10)


def show_dashboard():
    """Displays the dashboard screen after login."""
    clear_frame()

    Label(root, text=f"Welcome to the Dashboard", font=('Arial', 24, 'bold'), bg='#f0f8ff', fg='#005b96').pack(pady=30)

    # Dashboard options
    button_frame = Frame(root, bg='#f0f8ff')
    button_frame.pack(pady=20)

    Button(button_frame, text="Upload Image", font=('Arial', 14, 'bold'), bg='#005b96', fg='white', width=20, command=upload_image).pack(pady=15)
    Button(button_frame, text="Retrieve Report", font=('Arial', 14, 'bold'), bg='#0077c2', fg='white', width=20, command=retrieve_image).pack(pady=15)
    Button(button_frame, text="Logout", font=('Arial', 12), bg='#f44336', fg='white', width=15, command=show_login_screen).pack(pady=20)


# Core Functionalities
def login():
    """Handles user login."""
    global logged_in_user_id
    username = username_var.get().strip()
    password = password_var.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    try:
        query = "SELECT id FROM Users WHERE username = %s AND password = %s"
        sql.execute(query, (username, password))
        result = sql.fetchone()

        if result:
            logged_in_user_id = result[0]
            messagebox.showinfo("Success", f"Welcome, {username}!")
            show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def signup():
    """Handles user signup."""
    username = username_var.get().strip()
    password = password_var.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty!")
        return

    try:
        query_check = "SELECT * FROM Users WHERE username = %s"
        sql.execute(query_check, (username,))
        if sql.fetchone():
            messagebox.showerror("Error", "Username already exists! Please choose another one.")
            return

        query_insert = "INSERT INTO Users (username, password) VALUES (%s, %s)"
        sql.execute(query_insert, (username, password))
        connection.commit()
        messagebox.showinfo("Success", f"Account created for {username}! You can now log in.")
        show_login_screen()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def upload_image():
    """Handles image upload and analysis."""
    global logged_in_user_id
    if not logged_in_user_id:
        messagebox.showerror("Error", "Please log in first!")
        return

    image_path = askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        messagebox.showerror("Error", "No file selected.")
        return

    try:
        # Store image path in the database
        upload_dir = "uploaded_images"
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        file_name = os.path.basename(image_path)
        destination_path = os.path.join(upload_dir, file_name)
        
        # Copy the selected image to the upload directory
        shutil.copy(image_path, destination_path)

        query = "INSERT INTO UploadedImages (user_id, image_path, uploaded_at) VALUES (%s, %s, %s)"
        sql.execute(query, (logged_in_user_id, destination_path, datetime.now()))
        connection.commit()

        # Run the deep learning model inference and show results
        generate_report(destination_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def generate_report(image_path):
    """Runs the model on the image and displays prediction."""
    try:
        label_idx, class_label = dr_model.inference(model, image_path, dr_model.test_transforms, dr_model.classes)
        
        # Show image and prediction using matplotlib
        image = Image.open(image_path)
        plt.imshow(image)
        plt.title(f"Diagnosis: {class_label} (Label {label_idx})")
        plt.axis('off')
        plt.show()

        # Also show popup message with result
        messagebox.showinfo("Prediction Result", f"Predicted Severity: {class_label} (Label {label_idx})")

    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed: {e}")


def retrieve_image():
    """Retrieves the most recent uploaded image for the logged-in user."""
    global logged_in_user_id
    if not logged_in_user_id:
        messagebox.showerror("Error", "Please log in first!")
        return

    try:
        query = "SELECT image_path FROM UploadedImages WHERE user_id = %s ORDER BY uploaded_at DESC LIMIT 1"
        sql.execute(query, (logged_in_user_id,))
        result = sql.fetchone()

        if result:
            image_path = result[0]
            messagebox.showinfo("Success", f"Latest image retrieved: {image_path}")
        else:
            messagebox.showinfo("No Images", "No uploaded images found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Initialize the app with the login screen
show_login_screen()
root.mainloop()
