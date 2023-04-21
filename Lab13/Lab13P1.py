# Myles Joubert
# 4/10/23

import tkinter as tk
from tkinter import messagebox

class GradeCalculator:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('260x125')
        
        self.tests_frame = tk.Frame(self.main_window)
        self.labs_frame = tk.Frame(self.main_window)
        self.exams_frame = tk.Frame(self.main_window)
        self.average_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)
        
        self.tests_label = tk.Label(self.tests_frame, text='Tests Grade:')
        self.tests_entry = tk.Entry(self.tests_frame, width=10)
        
        self.labs_label = tk.Label(self.labs_frame, text='Labs Grade:')
        self.labs_entry = tk.Entry(self.labs_frame, width=10)
        
        self.exams_label = tk.Label(self.exams_frame, text='Exams Grade:')
        self.exams_entry = tk.Entry(self.exams_frame, width=10)
        
        self.average_label = tk.Label(self.average_frame, text='Grade Average:')
        self.average_result = tk.Label(self.average_frame, text='----')
        
        self.calculate_button = tk.Button(self.button_frame, text='Calculate', command=self.calculate)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        
        self.tests_label.pack(side='left')
        self.tests_entry.pack(side='left')
        
        self.labs_label.pack(side='left')
        self.labs_entry.pack(side='left')
        
        self.exams_label.pack(side='left')
        self.exams_entry.pack(side='left')
        
        self.average_label.pack(side='left')
        self.average_result.pack(side='left')
        
        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.tests_frame.pack()
        self.labs_frame.pack()
        self.exams_frame.pack()
        self.average_frame.pack()
        self.button_frame.pack()
        
        tk.mainloop()
    
    def calculate(self):
        try:
            tests_grade = float(self.tests_entry.get())
            labs_grade = float(self.labs_entry.get())
            exams_grade = float(self.exams_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid grades.')
            return
        
        average_grade = (tests_grade * 0.2) + (labs_grade * 0.3) + (exams_grade * 0.5)
        
        self.average_result.config(text='{:.1f} ({})'.format(average_grade, self