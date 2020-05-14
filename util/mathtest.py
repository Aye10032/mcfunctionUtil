import matplotlib.pyplot as plt
import numpy as np


def star():
    r = 2.0

    theta = np.arange(0, 2 * np.pi, 0.01)
    x = r * np.power(np.cos(theta), 3)
    y = r * np.power(np.sin(theta), 3)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)

    axes.axis('equal')
    plt.title("circle")

    plt.show()


def luoxuan():
    theta_np = np.arange(0, 2, 0.01)
    theta = theta_np * np.pi
    a = 1
    b = 1

    r = a + b * theta
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)

    axes.axis('equal')
    plt.title("luoxuan")

    plt.show()


def xietuoyuan():
    theta_np = np.arange(-0.7, 0.9, 0.01)
    theta = theta_np * np.pi
    a = 1
    b = 1

    x = 4 * np.sin(theta)
    y = 4 * np.cos(theta)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)

    axes.axis('equal')
    plt.title("xietuoyuan")

    plt.show()


def circle_3d(x1, y1, x2, y2):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    r = np.abs(y1 - y2) / 2

    theta_np = np.arange(-0.5, 0.5, 0.01)
    theta = theta_np * np.pi

    y = y1 + r + r * np.sin(theta)
    z = r * np.cos(theta)

    x = x1 + np.abs(x2-x1)*y

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 绘制图形
    ax.plot(x, y, z, label='parametric curve')

    # 显示图例
    ax.legend()

    # 显示图形
    plt.show()


circle_3d(-1, -1, 2, 3)
