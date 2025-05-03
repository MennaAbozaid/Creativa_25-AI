import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
X = np.array([1, 2, 3, 4])
y = np.array([1, 2.8, 3.6, 4.5])

# Initialize parameters
theta_0 = 0 #bias
theta_1 = 0  #slope (weight)
alpha = 0.01  #learning rate
# Number of iterations for gradient descent
num_iterations = 20


# Store the SSE values for plotting
sse_values = []

# Gradient descent
for i in range(num_iterations):
    # Compute predictions
    y_pred = theta_0 + theta_1 * X
    
    # Compute gradients
    d_theta_0 = 2 * np.sum(y_pred - y)
    d_theta_1 = 2 * np.sum((y_pred - y) * X)
    
    # Update parameters
    theta_0 -= alpha * d_theta_0
    theta_1 -= alpha * d_theta_1

    # Compute SSE and store it
    sse = np.sum((y - y_pred) ** 2)
    sse_values.append(sse)
    
    # Debug: Print the SSE every 100 iterations
    if (i+1) % 100 == 0:
        print(f"Iteration {i+1}, SSE: {sse}")


# Plotting the SSE values to show convergence
plt.figure(figsize=(12, 5))

# SSE over iterations
plt.subplot(1, 2, 1)
plt.plot(range(num_iterations), sse_values, label='SSE')
plt.xlabel('Iteration')
plt.ylabel('SSE')
plt.title('SSE over Iterations')
plt.legend()

# Plotting the data points and the final regression line
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, theta_0 + theta_1 * X, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()

plt.tight_layout()
plt.show()

print(f"Optimized parameters: theta_0 = {theta_0}, theta_1 = {theta_1}")


y_pred = 0.4329 + 1.157 *3
y_pred