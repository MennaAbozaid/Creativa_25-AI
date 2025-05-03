import tkinter as tk
from tkinter import messagebox
import numpy as np

# --------------------------
# Linear Regression Class
# --------------------------
class SimpleLinearRegressor:
    def __init__(self, X, y, alpha=0.01, iterations=1000):
        self.X = np.array(X)
        self.y = np.array(y)
        self.alpha = alpha
        self.iterations = iterations
        self.theta_0 = 0
        self.theta_1 = 0

    def fit(self):
        for _ in range(self.iterations):
            y_pred = self.theta_0 + self.theta_1 * self.X
            d_theta_0 = 2 * np.sum(y_pred - self.y)
            d_theta_1 = 2 * np.sum((y_pred - self.y) * self.X)
            self.theta_0 -= self.alpha * d_theta_0
            self.theta_1 -= self.alpha * d_theta_1

    def predict(self, x):
        return self.theta_0 + self.theta_1 * x

# --------------------------
# GUI App
# --------------------------
class SalaryApp:
    def __init__(self, master):
        self.master = master
        master.title("AMIT - Machine Learning Diploma")
        master.geometry("700x400")
        master.configure(bg="#f8f0f0")

        # Sample training data
        X = [1, 2, 3, 4]
        y = [10000, 30000, 50000, 60000]
        self.model = SimpleLinearRegressor(X, y)
        self.model.fit()

        # Sidebar
        self.sidebar = tk.Frame(master, bg="#e6e6e6", width=120)
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT)

        for i, text in enumerate(["Linear Regression", "Project2", "Project3", "Project4", "Project5", "Project6", "Project7", "Project8", "Project9"]):
            tk.Label(self.sidebar, text=text, bg="#e6e6e6", anchor="w", padx=10).pack(fill=tk.X)

        # Header
        self.header = tk.Label(master, text="AMIT - Machine Learning Diploma", font=("Arial", 16, "bold"), bg="#f8bcbc", pady=10)
        self.header.pack(fill=tk.X)

        # Center content
        self.content_frame = tk.Frame(master, bg="#f8f0f0")
        self.content_frame.pack(pady=30)

        tk.Label(self.content_frame, text="Salary Prediction", font=("Arial", 14), bg="#f8f0f0").pack(pady=5)
        tk.Label(self.content_frame, text="Enter years of experience:", font=("Arial", 12), bg="#f8f0f0").pack()

        self.exp_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        self.exp_entry.pack(pady=5)

        self.execute_btn = tk.Button(self.content_frame, text="Execute", command=self.predict_salary, font=("Arial", 12), bg="#f8bcbc")
        self.execute_btn.pack(pady=5)

        self.result_label = tk.Label(self.content_frame, text="", font=("Arial", 12), fg="black", bg="#f8f0f0")
        self.result_label.pack()

        self.review_label = tk.Label(self.content_frame, text="Reviewed by: Menna Abozaid", font=("Arial", 12, "bold"), bg="#f8f0f0")
        self.review_label.pack(pady=15)

    def predict_salary(self):
        try:
            exp = float(self.exp_entry.get())
            salary = self.model.predict(exp)
            self.result_label.config(text=f"Your Expected Salary is: {int(salary)}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for experience.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryApp(root)
    root.mainloop()
