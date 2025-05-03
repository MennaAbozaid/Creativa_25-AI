import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# --------------------------
# Linear Regression Class
# --------------------------
class SalaryModel:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.model = LinearRegression()
        self.train_model()

    def train_model(self):
        X = self.data[['YearsExperience']]
        y = self.data['Salary']
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=10)
        self.model.fit(X_train, y_train)

    def predict(self, years):
        return self.model.predict([[years]])[0]

# --------------------------
# GUI Class
# --------------------------
class SalaryApp:
    def __init__(self, master, model):
        self.master = master
        self.model = model
        master.title("AMIT - Machine Learning Diploma")
        master.geometry("700x400")
        master.configure(bg="#f8f0f0")

        # Sidebar
        self.sidebar = tk.Frame(master, bg="#e6e6e6", width=120)
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT)
        for text in ["Linear Regression", "Project2", "Project3", "Project4", "Project5", "Project6", "Project7", "Project8", "Project9"]:
            tk.Label(self.sidebar, text=text, bg="#e6e6e6", anchor="w", padx=10).pack(fill=tk.X)

        # Header
        self.header = tk.Label(master, text="AMIT - Machine Learning Diploma", font=("Arial", 16, "bold"), bg="#f8bcbc", pady=10)
        self.header.pack(fill=tk.X)

        # Content
        self.content_frame = tk.Frame(master, bg="#f8f0f0")
        self.content_frame.pack(pady=30)

        tk.Label(self.content_frame, text="Salary Prediction", font=("Arial", 14), bg="#f8f0f0").pack(pady=5)
        tk.Label(self.content_frame, text="Enter years of experience:", font=("Arial", 12), bg="#f8f0f0").pack()

        self.entry = tk.Entry(self.content_frame, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.execute_btn = tk.Button(self.content_frame, text="Execute", font=("Arial", 12), bg="#f8bcbc", command=self.predict_salary)
        self.execute_btn.pack(pady=5)

        self.result_label = tk.Label(self.content_frame, text="", font=("Arial", 12), fg="black", bg="#f8f0f0")
        self.result_label.pack()

        self.review_label = tk.Label(self.content_frame, text="Reviewed by: Menna Abozaid", font=("Arial", 12, "bold"), bg="#f8f0f0")
        self.review_label.pack(pady=15)

    def predict_salary(self):
        try:
            years = float(self.entry.get())
            salary = self.model.predict(years)
            self.result_label.config(text=f"Your Expected Salary is: {int(salary)}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

# --------------------------
# Run App
# --------------------------
if __name__ == "__main__":
    # Update the path to your actual CSV file
    model = SalaryModel(r"D:\AI & Machine Learning\Tasks\Salary_Data.csv")

    root = tk.Tk()
    app = SalaryApp(root, model)
    root.mainloop()
