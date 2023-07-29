import pyautogui
import pytesseract
from PIL import Image
import time
import re
import logging
import datetime

def configure_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def log(message, level='debug'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if level == 'debug':
        logger.debug(message)
    elif level == 'verbose':
        logger.info(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.info(message)


def find_image_with_similarity(image_filename, similarity_threshold=0.9, region=None):
    image_location = pyautogui.locateOnScreen(image_filename, confidence=similarity_threshold, region=region)
    return image_location


def wait_for_image(image_filename, timeout=10):
    start_time = time.time()

    while time.time() - start_time < timeout:
        image_location = find_image_with_similarity(image_filename)
        if image_location is not None:
            log(image_filename + " found.")
            return image_location
    log(image_filename + " is not found.")
    return None


def tap(x, y):
    pyautogui.mouseDown(x, y)
    pyautogui.mouseUp(x, y)


def tap_image(image_path, screenshot=False, before=False, result_filename=None):
    image_location = find_image_with_similarity(image_path)
    if image_location is not None:
        center_x, center_y = find_image_center(image_location)
        if before and screenshot:
            save_screenshot()
        tap(center_x, center_y)
        if not before and screenshot:
            if result_filename is not None:
                wait_for_image(result_filename, 2)
            save_screenshot()
    else:
        log(image_path + " is not found.")


def wait_and_tap(image_path, timeout=10):
    wait_for_image(image_path, timeout)
    tap_image(image_path)


def wait_until_disappear(image_path, timeout=10):
    count = 0
    while count < timeout:
        if not is_found(image_path):
            break
        count += 1
        time.sleep(1)



def tap_util_found(image_path, util_found_image, interval=1):
    while True:
        tap_image(image_path)
        wait_for_image(util_found_image, timeout=interval)


def find_image_center(image_location):
    x, y, width, height = image_location
    center_x = x + (width/2)
    center_y = y + (height/2)
    return center_x, center_y


def tap_image_in_region(image_filename, region_filename):
    region = find_image_with_similarity(region_filename)
    image_location = find_image_with_similarity(image_filename, region=region)
    if image_location is not None:
        center_x, center_y = find_image_center(image_location)
        tap(center_x, center_y)
    else:
        log(image_filename + "was not found in the specified " + region_filename)


def save_screenshot():
    current_datetime = datetime.datetime.now()
    datetime_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/screenshot_{datetime_string}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)


def is_found(image_path):
    if find_image_with_similarity(image_path) is not None:
        return True
    else:
        return False
    

def hold_press(key, timeout=1):
    pyautogui.keyDown(key)
    time.sleep(timeout)
    pyautogui.keyUp(key)


def key_press(key):
    pyautogui.press(key)


def type(text):
    pyautogui.typewrite(text)


def get_text_from_image(image_filename, offset_x=100, offset_y=45):
    image_obj = find_image_with_similarity(image_filename)
    if image_obj is not None:
        x, y, width, height = image_obj
        screenshot = pyautogui.screenshot(region=((x + offset_x), (y + offset_y), (width - offset_x), height))
        gray_image = screenshot.convert('L')
        extracted_text = pytesseract.image_to_string(gray_image)
        
        print(extracted_text)
        screenshot.save('test.png')
        return extracted_text
    

def boss_remaining_time(image_filename, ignore_spawn=False):
    text = get_text_from_image(image_filename)
    pattern = r"([\d]+)[:-]([\d]+)"
    match_result = re.search(pattern, text)
    if not ignore_spawn and 'Spawned' in text:
        print('Spawned')
        return 0
    elif match_result:
        print(match_result.group(0))
        minute_str = match_result.group(1)
        second_str = match_result.group(2)
        minute = int(minute_str)
        second = int(second_str)
        result = ((minute*60)+second)
        return result
    else:
        return 9999


def drag_and_drop(source_x, source_y, destination_x, destination_y, duration=0.25):
    pyautogui.moveTo(source_x, source_y, duration=duration)
    pyautogui.mouseDown()
    pyautogui.moveTo(destination_x, destination_y, duration=duration)
    pyautogui.mouseUp()


def drag_up(image_path, offset_y=100):
    drag_icon = find_image_with_similarity(image_path)
    center_x, center_y = find_image_center(drag_icon)
    drag_and_drop(center_x, center_y, center_x, center_y - offset_y)


def drag_down(image_path, offset_y=100):
    drag_icon = find_image_with_similarity(image_path)
    center_x, center_y = find_image_center(drag_icon)
    drag_and_drop(center_x, center_y, center_x, center_y + offset_y)


def scroll_down_util_found(expected_image, drag_image, offset_y=100):
    scroll_until_found(expected_image, drag_image, offset_y=offset_y, is_drag_up=True)


def scroll_up_util_found(expected_image, drag_image, offset_y=100):
    scroll_until_found(expected_image, drag_image, offset_y=offset_y, is_drag_up=False)


def scroll_until_found(expected_image, drag_image, offset_y=100, is_drag_up=True):
    while True:
        if is_found(expected_image):
            break
        wait_for_image(drag_image)
        if is_drag_up:
            drag_up(drag_image, offset_y=offset_y)
        else:
            drag_down(drag_image, offset_y=offset_y)
        time.sleep(1)