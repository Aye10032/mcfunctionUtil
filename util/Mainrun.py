import numpy as np
from cv2 import cv2

lnum = 0.2
entityName = "entity_draw"


def get_colorful_img(img):
    f = open('../image.txt', 'a')

    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    for row in range(height):
        for col in range(width):
            (b, g, r) = img[row][col]
            R = r / 255
            G = g / 255
            B = b / 255
            mc_fun = 'execute at @e[name=' + entityName + '] run particle dust ' \
                     + str(R) + ' ' + str(G) + ' ' + str(B) \
                     + ' 1 ~' + str((width * lnum) - (col * lnum)) + ' ~' + str((height * lnum) - (row * lnum)) \
                     + ' ~ 0 0 0 0.0 1 force @p\n'
            f.write(mc_fun)
    f.close()
    cv2.imshow("done", img)


def get_gray_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (T, thresh) = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY)

    f = open('tian4.mcfunction', 'a')
    count = 0

    print(thresh.shape)
    height = thresh.shape[0]
    width = thresh.shape[1]
    for row in range(height):
        for col in range(width):
            if thresh[row][col] == 0:
                mc_fun = 'execute at @e[name=' + entityName + '] run particle end_rod' \
                         + ' ~' + str((width * lnum) - (col * lnum)) + ' ~' + str((height * lnum) - (row * lnum)) \
                         + ' ~ 0 0 0 0.0 1 force @p\n'
                f.write(mc_fun)
                count += 1
    f.close()

    print(count)
    cv2.imshow("gray", thresh)


def smaller_img(img):
    src_height = img.shape[0]
    src_width = img.shape[1]
    print(src_height, src_width)

    max_n = 160

    wx = 0
    hx = 0
    if wx >= hx:
        hx = max_n
        wx = src_width * (max_n / src_height)
    else:
        wx = max_n
        hx = src_height * (max_n / src_width)

    dst = cv2.resize(src, (int(wx), int(hx)), interpolation=cv2.INTER_CUBIC)
    return dst


def gcd(a, b):
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a % b
    return a


def getsize(w, h):
    if ((w * lnum) * (h * lnum)) <= 40000:
        return True
    else:
        return False


src = cv2.imread("../test4.jpg")  # 读取图像

get_gray_img(smaller_img(src))

cv2.waitKey(0)
cv2.destroyAllWindows()
