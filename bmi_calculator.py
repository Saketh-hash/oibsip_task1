import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
def init_database():
    conn = sqlite3.connect("bmi_data.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL,
            height REAL,
            bmi REAL, 
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()
def save_to_db(weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO bmi_records (weight, height, bmi, category, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (weight, height, bmi, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def loaddata():
    conn = sqlite3.connect('bmi_data.db')
    df = pd.read_sql_query("SELECT * FROM bmi_records", conn)
    conn.close()
    return df

def showtrend():
    df = loaddata()
    if df.empty:
        messagebox.showinfo("No Data", "No historical data available.")
        return
    plt.figure(figsize=(10,5))
    plt.plot(pd.to_datetime(df['date']), df['bmi'], marker = 'o')
    plt.title('BMI Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.grid(True)
    plt.show()
def cal_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")
        bmi = weight / (height ** 2)
        result_label.config(text = f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            category = "UnderWeight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight"
        elif 25 <= bmi < 29.9:
            category = "OverWeight"

        else:
            category = "Obesity"
        category_label.config(text = f"Category: {category}")
        save_to_db(weight, height, bmi, category)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid Input: {e}")

root = tk.Tk()
root.title("Advanced BMI Calculator")
weight_label = tk.Label(root, text = "Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text = "Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text = "Calculate BMI", command= cal_bmi)
calculate_button.pack()

result_label = tk.Label(root, text = "BMI:")
result_label.pack()

category_label = tk.Label(root, text = "Category:")
category_label.pack()

trend_button = tk.Button(root, text = "Show BMI Trend", command= showtrend)
trend_button.pack()
init_database()
root.mainloop()


