print(len([794, 573, 1, 778, 468, 1, 718, 559, 1, 651, 568, 1, 682, 475, 1, 708, 574, 1, 683, 575, 1, 676, 466, 1, 672, 415, 2, 665, 359, 2, 766, 442, 1, 790, 455, 2, 727, 434, 2, 623, 444, 2, 629, 515, 1, 702, 463, 1]))

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()
