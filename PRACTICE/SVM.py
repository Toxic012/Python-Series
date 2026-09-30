import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# Generate a toy non-linear dataset (concentric circles)
X, y = make_circles(n_samples=200, factor=0.5, noise=0.05, random_state=42)

# Plot 1: Original dataset (linear separation attempt)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, s=30)
plt.title("Dataset: Non-linear (Concentric Circles)\nLinear separation impossible")
plt.xlabel("x1")
plt.ylabel("x2")

# Train SVM with RBF kernel
clf = SVC(kernel="rbf", C=1, gamma=1)
clf.fit(X, y)

# Create a mesh to plot decision boundary
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 300), np.linspace(-1.5, 1.5, 300))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot 2: Decision boundary with RBF kernel
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, s=30)
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="black")
plt.title("SVM with RBF Kernel\nNon-linear separation achieved")
plt.xlabel("x1")
plt.ylabel("x2")

plt.tight_layout()
plt.show()
