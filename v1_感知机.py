
import numpy as np
from matplotlib import pyplot as plt


class MyPerception:
    def __init__(self):
        self.w = None
        self.b = 0
        self.rate = 1
    def fit(self,  train_X,  train_Y):
        self.w = np.array([0,0])
        i = 0
        while i < train_X.shape[0]:
            x = train_X[i]
            y = train_Y[i]

            if y*(np.dot(self.w,x) + self.b) <=0:
                self.w += self.rate * np.dot(y,x)
                self.b += self.rate * y
                i = 0
            else:
                i += 1
def draw(X, w, b):
    X_new = np.array([[0],[6]])
    Y_new = -(b +w[0]*X_new)/w[1]

    plt.plot(X[:, 0],X[:, 1],"o")
    plt.plot(X_new, Y_new)
    plt.legend()
    plt.axis([0, 6, 0, 6])
    plt.show()


def main():
    train_X = np.array([[3,3],[4,3],[1,1],[2,1],[3,2]])
    train_Y = np.array([1,1,-1,-1,1])
    perception = MyPerception()
    perception.fit(train_X,train_Y)

    print(perception.w,perception.b)

    draw(train_X, perception.w, perception.b)

if __name__ == '__main__':
    main()