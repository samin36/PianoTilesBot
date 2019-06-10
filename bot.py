import pyautogui
import time
from mss import mss

def test_time():
    """ Compares times to take 100 screenshots using Pyautogui """
    t1 = time.time()
    for scrnshot in range(100):
        img = pyautogui.screenshot()
    t2 = time.time()
    return t2 - t1

def test_time_with_mss():
    """ Test time to take 100 screenshots using mss library """
    with mss() as sct:
        t1 = time.time()
        for scrnshot in range(100):
            img = sct.grab(sct.monitors[1])
        t2 = time.time()
        return t2 - t1


tile_width = 100
tile_height = 150
x_start = 750
y_start = 740
pos = [(x_start, -tile_height*count + y_start) for count in range(2)]

coords_x = [int(tile_width / 2 + step*tile_width) for step in range(4)]

def calc_area_box(x, y):
    """
    Calculates and returns a 4-tuple based on starting x and y
    """
    x, y = (x, y)
    return (x, y, x + 4 * tile_width, y + 1)

def check_img(img, coordinates):
    """ Returns True if there is a black pixel (RGB: (17, 17, 17)) at
        given coordinates else False
    """
    x, y = coordinates
    return img.pixel(x, y)[0] == 17

def start():
    with mss() as sct:
        while True:
            for i in range(len(pos)):
                x, y = pos[i]
                area_box = calc_area_box(x, y)
                img = sct.grab(area_box)
                for coord in coords_x:
                    if check_img(img, (coord, 0)):
                        x_real = x + coord
                        y_real = y
                        pyautogui.click(x_real, y_real)
                        break


start()
# pyautogui.displayMousePosition()
