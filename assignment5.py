import numpy as np
import scipy.stats as stats
from scipy import fftpack, linalg, interpolate, signal, optimize
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Q1. NumPy array of random numbers and compute mean, median, variance
q1_array = np.random.rand(10)
q1_mean = np.mean(q1_array)
q1_median = np.median(q1_array)
q1_variance = np.var(q1_array)
print("Q1:\nArray:", q1_array, "\nMean:", q1_mean, "\nMedian:", q1_median, "\nVariance:", q1_variance)

# Q2. 2D array and discrete Fourier transform
q2_array = np.random.rand(4, 4)
q2_fft = fftpack.fft2(q2_array)
print("\nQ2:\n2D Array:\n", q2_array, "\nFFT2:\n", q2_fft)

# Q3. Linear algebra: determinant, inverse, eigenvalues
q3_matrix = np.array([[2, 1, 3], [1, 2, 1], [3, 0, 2]])
q3_det = np.linalg.det(q3_matrix)
q3_inv = np.linalg.inv(q3_matrix)
q3_eigvals, q3_eigvecs = np.linalg.eig(q3_matrix)
print("\nQ3:\nDeterminant:", q3_det, "\nInverse:\n", q3_inv, "\nEigenvalues:", q3_eigvals)

# Q4. Interpolation
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
f_interp = interpolate.interp1d(x, y, kind='cubic')
x_new = np.linspace(0, 5, 50)
y_new = f_interp(x_new)
print("\nQ4: Interpolated values at 50 points:\n", y_new)

# Q5. Time series data and filtering
t = np.linspace(0, 1, 500)
signal_data = np.sin(2 * np.pi * 5 * t) + 0.5*np.random.randn(500)
b, a = signal.butter(3, 0.05)
filtered_signal = signal.filtfilt(b, a, signal_data)
print("\nQ5: Filtered signal computed")

# Q6. Sales data analysis
sales = np.random.randint(50, 200, size=(12, 4))  # 12 months, 4 products
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
best_month = np.argmax(np.sum(sales, axis=1)) + 1
worst_month = np.argmin(np.sum(sales, axis=1)) + 1
print("\nQ6:\nSales data:\n", sales, "\nTotal:", total_sales, "Avg:", avg_sales,
      "Max:", max_sales, "Best month:", best_month, "Worst month:", worst_month)

# Q7. Student marks analysis
students = ['Arin', 'Aditya', 'Chirag', 'Gurleen', 'Kunal']
marks = np.array([[85, 78, 92, 88],
                  [79, 82, 74, 90],
                  [90, 85, 89, 92],
                  [66, 75, 80, 78],
                  [70, 68, 75, 85]])
total_marks = np.sum(marks, axis=1)
avg_marks = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)
top_student = students[np.argmax(total_marks)]
bottom_student = students[np.argmin(total_marks)]
passing_percentage = np.mean(marks >= 40) * 100
print("\nQ7:\nTotal Marks:", total_marks, "\nAverage Marks:", avg_marks,
      "\nSubject Average:", subject_avg, "\nTop Student:", top_student,
      "\nBottom Student:", bottom_student, "\nPassing %:", passing_percentage)

# Q8. Curve fitting quadratic function
time = np.array([0, 1, 2, 3, 4, 5])
velocity = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])
def quadratic(t, a, b, c):
    return a*t**2 + b*t + c
params, _ = optimize.curve_fit(quadratic, time, velocity)
print("\nQ8: Quadratic params a, b, c:", params)

# Q9. Student marks analysis with plots
plt.figure()
for i, student in enumerate(students):
    plt.plot(['Math', 'Physics', 'Chemistry', 'English'], marks[i], marker='o', label=student)
plt.title('Student Marks Analysis')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.show()

# Q10. Curve fitting plot
time_dense = np.linspace(0, 5, 100)
plt.figure()
plt.plot(time, velocity, 'ro', label='Original Data')
plt.plot(time_dense, quadratic(time_dense, *params), 'b-', label='Fitted Curve')
plt.title('Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.show()

# Q11. Population Pearson correlation and interpolation
years = np.array([2000, 2005, 2010, 2015, 2020])
population = np.array([50, 55, 70, 80, 90])
pearson_corr = np.corrcoef(years, population)[0, 1]
linear_interp = interpolate.interp1d(years, population)
pop_2008 = float(linear_interp(2008))
plt.figure()
plt.plot(years, population, 'bo', label='Data')
plt.plot(2008, pop_2008, 'ro', label='Estimated 2008')
plt.title("Population vs Year")
plt.xlabel("Year")
plt.ylabel("Population (thousands)")
plt.legend()
plt.show()
print("\nQ11: Pearson correlation:", pearson_corr, "Population 2008:", pop_2008)

# Q12. Polynomial roots and plot
p = np.array([3, -5, 2, -8])
roots = np.roots(p)
x_vals = np.linspace(-3, 3, 100)
y_vals = np.polyval(p, x_vals)
plt.figure()
plt.plot(x_vals, y_vals, label='Polynomial p(x)')
plt.plot(roots, np.zeros_like(roots), 'ro', label='Roots')
plt.title("Polynomial and Roots")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()
plt.show()
print("\nQ12: Roots of polynomial:", roots)

# Q13. Performance comparison for converting large files to uppercase
import time
file_sizes = [200, 400, 600, 800, 1000]  # MB
times = []
for size in file_sizes:
    text = np.random.choice(list('abcdefghijklmnopqrstuvwxyz '), size*1024*1024)
    text_str = ''.join(text)
    start = time.time()
    text_str.upper()
    end = time.time()
    times.append(end-start)
plt.figure()
plt.plot(file_sizes, times, marker='o')
plt.title("Time taken to convert text to uppercase")
plt.xlabel("File size (MB)")
plt.ylabel("Time (s)")
plt.show()

# Q14. Local minima of f(x) = x^4 - 3x^3 + 2
f = lambda x: x**4 - 3*x**3 + 2
min_result = optimize.fminbound(f, -2, 3)
x_vals = np.linspace(-2, 3, 100)
plt.figure()
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.plot(min_result, f(min_result), 'ro', label='Local Minima')
plt.title("Function f(x) and Local Minima")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
print("\nQ14: Local minima at x =", min_result, "f(x) =", f(min_result))

# Q15. Damped oscillatory system (robotic arm)
def damped_osc(y, t, b=0.2, k=1):
    theta, theta_dot = y
    dydt = [theta_dot, -b*theta_dot - k*theta]
    return dydt
t = np.linspace(0, 20, 500)
y0 = [1, 0]
sol = odeint(damped_osc, y0, t)
theta = sol[:, 0]
max_displacement = np.max(theta)
time_max = t[np.argmax(theta)]
plt.figure()
plt.plot(t, theta)
plt.title("Damped Oscillation of Robotic Arm")
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.show()
print("\nQ15: Maximum displacement:", max_displacement, "Time:", time_max)
print("Damping coefficient 0.2 implies gradual reduction in oscillation amplitude over time.")

