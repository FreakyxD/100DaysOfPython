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
    pyautogui.press("space")  # Start the game


def take_screenshot():
    top_left_x = 330
    top_left_y = 555
    bottom_right_x = top_left_x + 75  # Moving 75 pixels to the right
    bottom_right_y = top_left_y + 45  # Moving 45 pixels down
    bbox = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)
    return PIL.ImageGrab.grab(bbox=bbox)


def screenshot_has_obstacle(image):
    image = image.convert("RGB")
    pixels = list(image.getdata())
    color_counter = Counter(pixels)
    top_colors = color_counter.most_common(2)

    if len(top_colors) != 1:
        return True, top_colors
    else:
        return False, top_colors


introduction()

cooldown = False
jump_cooldown_time = 0.25
last_state = None
unchanged_count = 0  # Counter to track how long the state has been unchanged

while True:
    if not cooldown:
        img = take_screenshot()
        has_obstacle, current_state = screenshot_has_obstacle(img)

        # If an obstacle is detected, jump
        if has_obstacle:
            pyautogui.press("space")
            cooldown = True  # Avoid multiple jumps while in the air

        # Check if the state has changed
        if current_state == last_state:
            unchanged_count += 1
        else:
            unchanged_count = 0  # Reset the counter if there's a change

        # If the state hasn't changed for 3 consecutive seconds (300 iterations), consider it "game over"
        if unchanged_count >= 300:  # 3 seconds of no change with 0.01s interval
            print("Game over detected! Exiting...")
            break

        last_state = current_state

    else:
        time.sleep(jump_cooldown_time)
        cooldown = False

    time.sleep(0.01)