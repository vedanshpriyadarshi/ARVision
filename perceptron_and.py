from nn.perceptron import Perceptron
import numpy as np

# construct the AND dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

# define our perceptron and train it
print("[INFO] training perceptron...")
p = Perceptron(X.shape[1], alpha=0.1)
p.fit(X, y, epochs=20)

# testing perceptron
print("[INFO] testing perceptron...")

# now we need to loop over data points
for (x, target) in zip(X, y):
    # make prediction based on data point
    # and display the output
    pred = p.predict(x)
    print("[INFO] data={}, ground-truth={}, pred={}".format(x, target[0], pred))

