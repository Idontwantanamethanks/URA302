import numpy as np

# Q1
x = np.arange(5, 25).reshape(4, 5)
print("Q1 (x.size):", x.size)

x_2d = np.random.randint(10, 50, size=(3, 4))
print("Q1 (2D Array):\n", x_2d)

# Q2
print("Q2 (x.shape):", x.shape)
print("Q2 (x.size):", x.size)
print("Q2 (x.dtype):", x.dtype)

print("Q2 (x_2d.shape):", x_2d.shape)
print("Q2 (x_2d.size):", x_2d.size)
print("Q2 (x_2d.dtype):", x_2d.dtype)

# Q3
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([1, 3, 5, 7, 9])
print("Q3 (a1+a2):", a1 + a2)
print("Q3 (a1-a2):", a1 - a2)
print("Q3 (a1*a2):", a1 * a2)
print("Q3 (a1/a2):", a1 / a2)

# Q4
arr_2d = np.arange(1, 10).reshape(3, 3)
print("Q4 (arr_2d):\n", arr_2d)
print("Q4 (arr_2d*5):\n", arr_2d * 5)

# Q5
arr_2d = np.arange(10, 26).reshape(4, 4)
print("Q5 (arr_2d):\n", arr_2d)
print("Q5 (2nd row):", arr_2d[1, :])
print("Q5 (1st column):", arr_2d[:, 0])
arr_2d[0, :] = 0
print("Q5 (after setting 1st row to 0):\n", arr_2d)

# Q6
arr = np.random.randint(20, 40, size=(10))
print("Q6 (array):", arr)
mask = arr > 30
print("Q6 (mask):", mask)
print("Q6 (values > 30):", arr[mask])

# Q7
arr = np.arange(11, 23)
print("Q7 (array):", arr)
print("Q7 reshaped (3x4):\n", arr.reshape(3, 4))

# Q8
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Q8 (a*b):\n", a * b)
print("Q8 (Transpose of a):\n", a.T)

# Q9
arr = np.random.randint(10, 60, size=(15))
print("Q9 (array):", arr)
print("Q9 Mean:", np.mean(arr))
print("Q9 Median:", np.median(arr))
print("Q9 Standard Deviation:", np.std(arr))

# Q10
arr_3d = np.array([[2, 1, 3], [0, 5, 6], [7, 8, 9]])
print("Q10 (matrix):\n", arr_3d)

print("Q10 Determinant:", np.linalg.det(arr_3d))
print("Q10 Inverse:\n", np.linalg.inv(arr_3d))

eigvals, eigvectors = np.linalg.eig(arr_3d)
print("Q10 Eigenvalues:", eigvals)
print("Q10 Eigenvectors:\n", eigvectors)

# Q11
pos = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
print("Q11 (Euclidean distance between first and last point):",
      np.linalg.norm(pos[-1] - pos[0]))

diff = np.diff(pos, axis=0)
step_dist = np.linalg.norm(diff, axis=1)   # distance of each step
total_dist = np.sum(step_dist)             # total path length

print("Q11 (Step distances):", step_dist)
print("Q11 (Total distance):", total_dist)
