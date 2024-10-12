import time
import PIL
import webbrowser
import pyautogui
from collections import Counter

GAME_URL = "https://elgoog.im/dinosaur-game/"


def introduction():
    time.sleep(3)
    webbrowser.open(GAME_URL)
    time.sleep(3)
    pyautogui.press("space")  # starts the game


def take_screenshot():
    top_left_x = 330
    top_left_y = 555
    bottom_right_x = top_left_x + 75  # moving 75 pixels to the right
    bottom_right_y = top_left_y + 45  # moving 45 pixels down
    bbox = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    return PIL.ImageGrab.grab(bbox=bbox)


def screenshot_has_obstacle(image):
    image = image.convert("RGB")
    pixels = list(image.getdata())
    color_counter = Counter(pixels)
    top_colors = color_counter.most_common(2)

    if len(top_colors) != 1:
        return True


introduction()

cooldown = False
jump_cooldown_time = 0.25
time_since_obstacle = time.time()

while True:
    if not cooldown:
        img = take_screenshot()
        has_obstacle = screenshot_has_obstacle(img)

        # if an obstacle is detected, jump
        if has_obstacle:
            pyautogui.press("space")
            cooldown = True  # Avoid multiple jumps while in the air
            time_since_obstacle = time.time()  # Reset the timer

        # check if it's been more than 3 seconds since the last obstacle
        if time.time() - time_since_obstacle > 5:
            pyautogui.alert("Game over detected! Exiting...")
            break

    else:
        time.sleep(jump_cooldown_time)
        cooldown = False

    time.sleep(0.01)
