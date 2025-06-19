# main.py

import tkinter as tk
from tkinter import messagebox
from Students import StudentManager

manager = StudentManager()

# === GUI FUNCTIONS ===

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    roll = roll_entry.get()
    email = email_entry.get()
    dept = dept_entry.get()

    if name and age and roll and email and dept:
        manager.add_student(name, age, roll, email, dept)
        messagebox.showinfo("✅ Success", "Student added successfully!")
        clear_inputs()
        view_students()
    else:
        messagebox.showwarning("⚠️ Error", "All fields are required!")

def view_students():
    listbox.delete(0, tk.END)
    for s in manager.get_all_students():
        listbox.insert(tk.END, str(s))

def search_student():
    listbox.delete(0, tk.END)
    roll = roll_entry.get()
    found = manager.find_by_roll(roll)
    if found:
        for s in found:
            listbox.insert(tk.END, str(s))
    else:
        messagebox.showinfo("❌ Not Found", "No student with that roll number.")

def delete_student():
    roll = roll_entry.get()
    manager.delete_by_roll(roll)
    messagebox.showinfo("🗑️ Deleted", f"Student with Roll No {roll} deleted.")
    view_students()

def sort_by_name():
    manager.sort_by_name()
    view_students()

def sort_by_roll():
    manager.sort_by_roll()
    view_students()

def clear_inputs():
    for entry in [name_entry, age_entry, roll_entry, email_entry, dept_entry]:
        entry.delete(0, tk.END)

# === GUI WINDOW ===

window = tk.Tk()
window.title("🎓 Student Management System")
window.geometry("600x650")
window.config(bg="#f7f7f7")

# Input Labels + Fields
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Age").pack()
age_entry = tk.Entry(window)
age_entry.pack()

tk.Label(window, text="Roll No").pack()
roll_entry = tk.Entry(window)
roll_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window)
email_entry.pack()

tk.Label(window, text="Department").pack()
dept_entry = tk.Entry(window)
dept_entry.pack()

# Buttons
tk.Button(window, text="➕ Add Student", command=add_student, bg="#d0f0c0").pack(pady=5)
tk.Button(window, text="📋 View All Students", command=view_students).pack(pady=5)
tk.Button(window, text="🔍 Search by Roll", command=search_student).pack(pady=5)
tk.Button(window, text="🗑️ Delete by Roll", command=delete_student).pack(pady=5)
tk.Button(window, text="🔠 Sort by Name", command=sort_by_name).pack(pady=5)
tk.Button(window, text="🔢 Sort by Roll No", command=sort_by_roll).pack(pady=5)

# List Display
tk.Label(window, text="📚 Student Records").pack(pady=10)
listbox = tk.Listbox(window, width=70, height=12)
listbox.pack(pady=10)

window.mainloop()
