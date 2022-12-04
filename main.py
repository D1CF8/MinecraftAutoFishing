import dxcam
import mss
import cv2
import numpy
import time
import pyautogui as bot
from time import sleep

x_list = [1000, 960, ]
def screen_record_efficient():
    mon = {'top': 600, 'left': 890, 'width': 100, 'height': 100}
    title = "Minecraft Auto Fishing"
    fps = 0
    sct = mss.mss()
    last_time = time.time()
    while True:
        img = numpy.asarray(sct.grab(mon))
        fps += 1
        cv2.imshow(title, img)
        img_arr = numpy.array(img)
        our_crd = [1, 1]
        our_color = (64, 50, 171)
        our_map = (our_color[2], our_color[1], our_color[0], 255)
        indexes = numpy.where(numpy.all(img_arr == our_map, axis=-1))
        our_crd = numpy.transpose(indexes)

        our_crd_2 = [1, 1]
        our_color_2 = (40, 28, 123)
        our_map_2 = (our_color_2[2], our_color_2[1], our_color_2[0], 255)
        indexes_2 = numpy.where(numpy.all(img_arr == our_map_2, axis=-1))
        our_crd_2 = numpy.transpose(indexes_2)

        our_crd_3 = [1, 1]
        our_color_3 = (12, 9, 34)
        our_map_3 = (our_color_3[2], our_color_3[1], our_color_3[0], 255)
        indexes_3 = numpy.where(numpy.all(img_arr == our_map_3, axis=-1))
        our_crd_3 = numpy.transpose(indexes_3)
        if cv2.waitKey(25) & 0xFF == ord('q') or cv2.waitKey(25) & 0xFF == ord('й'):
            break
        f = 0
        if len(our_crd) != 0 or len(our_crd_2) != 0 or len(our_crd_3) != 0:
            print('Рыба!')
            sleep(0.2)
            bot.rightClick()
            sleep(0.2)
            bot.rightClick()
            sleep(0.5)
    return fps
print("MSS:", screen_record_efficient())

# 207 41 41