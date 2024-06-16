import configparser
import pyautogui
import pytesseract
import time
import logging
import datetime
import search_screen
import windows_capture
import click
import cv2 as cv
import os
import sys
from PIL import Image

config = configparser.ConfigParser()
config_file_path = 'bot.ini'
config.read(config_file_path)
settings = config['SETTINGS']
new_capture = True
new_click = True
new_sendkey = True
new_drag_drop = True

debug=(False if settings['debug'] == 'False' else bool(settings['debug']))
print(f"debug: {debug}")
window_name = settings['window_name']
print(f"window name: {window_name}")
# window_name = 'LDPlayer-PP'

window = windows_capture.WindowCapture(window_name)
 ## check click hwid
myclick = click.Click(window_name)
# nox_hwids = myclick.get_nox_player_windows()
ld_hwid = myclick.gethwid()
ld_hwids = myclick.get_hwids("sub", level=2)

ld_offset_x = 47
ld_offset_y = 33

def configure_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def log(message, level='debug', enable=True):
    if not enable:
        return

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


def find_image_with_similarity(image_filename, similarity=0.9, region=None):
    image_location = None
    if new_capture:
        regtangles = search_image(image_filename, similarity)
        if len(regtangles):
            image_location = regtangles[0]
    else:
        image_location = pyautogui.locateOnScreen(image_filename, confidence=similarity, region=region)
    
    return image_location


def search_image(image_filename, similarity, screen=None):
    if screen is None:
        screen = window.screenshot()
    search = search_screen.Classbot(screen, image_filename, window_name=settings['window_name'])
    regtangles = search.search(debug=debug, image_path=image_filename, threshold=similarity)
    return regtangles


def find_all_image_with_similarity(image_filename, similarity=0.9, region=None):
    if new_capture:
        return search_image(image_filename, similarity)
    else:
        image_locations = pyautogui.locateAllOnScreen(image_filename, confidence=similarity, region=region)
        grouped = group_coordinate(image_locations)
        return grouped


def find_all_images(image_array, similarity=0.9):
    all_image_locations = []
    for image in image_array:
        image_locations = find_all_image_with_similarity(image, similarity)
        all_image_locations.extend(image_locations)
    return all_image_locations


def find_image_more_than_offset_coordinate(image_array, offset_x=0, offset_y=0, similarity=0.9):
    image_coordinates = find_all_images(image_array, similarity)
    tobe_return_coordinate = []
    for image_coordinate in image_coordinates:
        center_x, center_y = find_image_center(image_coordinate)
        if center_x > offset_x and center_y > offset_y:
            tobe_return_coordinate.append(image_coordinate)
    return tobe_return_coordinate


def find_most_left_coordinate(image_array):
    image_coordinates = find_all_images(image_array)
    least_x = 9999
    tobe_return_coordinate = list()
    for image_coordinate in image_coordinates:
        center_x, _ = find_image_center(image_coordinate)
        if center_x < least_x:
            least_x = center_x
            tobe_return_coordinate = image_coordinate
    return tobe_return_coordinate


def find_most_bottom_coordinate(image_array):
    image_coordinates = find_all_images(image_array)
    least_y = 0
    tobe_return_coordinate = list()
    for image_coordinate in image_coordinates:
        _, center_y = find_image_center(image_coordinate)
        print(center_y)
        if center_y > least_y:
            least_y = center_y
            tobe_return_coordinate = image_coordinate
    return tobe_return_coordinate


def find_most_top_coordinate(image_array):
    image_coordinates = find_all_images(image_array)
    max_y = 9999
    tobe_return_coordinate = list()
    for image_coordinate in image_coordinates:
        _, center_y = find_image_center(image_coordinate)
        print(center_y)
        if center_y < max_y:
            max_y = center_y
            tobe_return_coordinate = image_coordinate
    return tobe_return_coordinate


def group_coordinate(image_locations):
    image_array = []
    previous_left = 0
    for image in image_locations:
        diff = image.left - previous_left
        previous_left = image.left
        if diff > 10:
            image_location = (image.left, image.top, image.width, image.height)
            image_array.append(image_location)
    return image_array
        

def count_image_on_screen(image_filename, similarity=0.9):
    images = find_all_image_with_similarity(image_filename, similarity)
    return len(images)


def count_all_image_on_screen(image_array, similarity=0.9):
    if not isinstance(image_array, list):
        raise ValueError('object is not an array')

    count = 0
    for image in image_array:
        images = find_all_image_with_similarity(image, similarity)
        # print(f'Find image: {image} found: {len(images)}')
        count += len(images)
    return count


def wait_until_found_all_images(image_array, expected_number, similarity=0.9, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        count = count_all_image_on_screen(image_array, similarity)
        print(f'Found image: {count} with expected: {expected_number}')
        if count == expected_number:
            break
        time.sleep(1)


def wait_for_image(image_filename, timeout=10, enable_log=True, similarity=0.9):
    log('wait_for_image: ' + image_filename, enable=enable_log)
    start_time = time.time()

    while time.time() - start_time < timeout:
        image_location = find_image_with_similarity(image_filename, similarity)
        if image_location is not None:
            log(image_filename + " found.", enable=enable_log)
            return image_location
    log(image_filename + " is not found.", enable=enable_log)
    return None


def wait_any_image(image_filenames, timeout=10, similarity=0.9):
    start_time = time.time()

    while time.time() - start_time < timeout:
        for image_filename in image_filenames:
            image_location = wait_for_image(image_filename, timeout=1, enable_log=False, similarity=similarity)
            if image_location is not None:
                log(image_filename + " found.")
                return image_location
    log(image_filename + " is not found.")
    return None


def hilight(x, y):
    if debug:
        screen = window.screenshot()
        search = search_screen.Classbot(screen, window_name=settings['window_name'])
        search.draw_debug_rect("hilight", int(x-5), int(y-5), 10, 10, show_finding_image=True)


def hilight_image(image_path, offset_x=0, offset_y=0, similarity=0.9):
    image_location = find_image_with_similarity(image_path, similarity=similarity)
    if image_location is not None:
        center_x, center_y = find_image_center(image_location)
        hilight(center_x+offset_x, center_y+offset_y)


def tap(x, y):

    if debug:
        screen = window.screenshot()
        search = search_screen.Classbot(screen, window_name=settings['window_name'])
        search.draw_debug_rect("tap", int(x-5), int(y-5), 10, 10, show_finding_image=True)
    if new_click:
        
        x2 = int(x - ld_offset_x)
        y2 = int(y - ld_offset_y)

        myclick.click(ld_hwid, x2, y2)
    else:
        pyautogui.mouseDown(x, y)
        pyautogui.mouseUp(x, y)


def tap_image(image_path, screenshot=False, before=False, result_filename=None, similarity=0.9):
    image_location = find_image_with_similarity(image_path, similarity=similarity)
    if image_location is not None:
        center_x, center_y = find_image_center(image_location)
        # if before and screenshot:
            # save_screenshot()
        tap(center_x, center_y)
        if not before and screenshot:
            if result_filename is not None:
                wait_for_image(result_filename, 2)
            # save_screenshot()
        return image_location
    else:
        log(image_path + " is not found.")
        return None


def tap_image_offset(image_path, offset_x=0, offset_y=0, similarity=0.9):
    image = find_image_with_similarity(image_path, similarity=similarity)
    if not is_empty(image):
        tap_location(image, offset_x, offset_y)
    else:
        print(image_path + ' is not found')


def is_empty(obj):
    if obj is None:
        return True
    return False


def hilight_location(coordinate, offset_x=0, offset_y=0):
    center_x, center_y = find_image_center(coordinate)
    hilight(center_x + offset_x, center_y + offset_y)

def tap_location(coordinate, offset_x=0, offset_y=0):
    center_x, center_y = find_image_center(coordinate)
    tap(center_x + offset_x, center_y + offset_y)


def tap_location_until_found(location, expected_found_image, timeout=10, delay=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if wait_for_image(expected_found_image, timeout=delay) is not None:
            return True
        tap_location(location)
    return False

def tap_if_found(image_path):
    if is_found(image_path):
        return tap_image(image_path)
    return None


def tap_offset_if_found(image_path, offset_x=0, offset_y=0):
    if is_found(image_path):
        return tap_image_offset(image_path, offset_x, offset_y)
    return None


def tap_all(images):
    for image in images:
        tap_if_found(image)


def tap_any(menu_images, similarity=0.9):
    for menu in menu_images:
        if is_found(menu, similarity):
            return tap_image(menu, similarity)
    return None
        

def tap_any_until_found_offset(to_be_tap_images, expected_found_image, offset_x=0, offset_y=0, timeout=10, similarity=0.9):
    start_time = time.time()
    while time.time() - start_time < timeout:
        tap_any_offset(to_be_tap_images, offset_x, offset_y, similarity=similarity)
        wait_for_image(expected_found_image, timeout=1, similarity=similarity)
        if is_found(expected_found_image):
            return True
    return False


def tap_any_offset(images, offset_x=0, offset_y=0, similarity=0.9):
    for image in images:
        if is_found(image, similarity):
            tap_image_offset(image, offset_x, offset_y, similarity)
            return


def wait_and_tap(image_path, timeout=10, similarity=0.9):
    wait_for_image(image_path, timeout)
    return tap_image(image_path, similarity=similarity)


def wait_and_tap_any(image_paths, timeout=10, similarity=0.9):
    location = wait_any_image(image_paths, timeout, similarity)
    if location is not None:
        tap_location(location)


def wait_until_disappear(image_path, timeout=10, similarity=0.9):
    count = 0
    while count < timeout:
        if not is_found(image_path, similarity):
            return True
        count += 1
        time.sleep(1)
    return False



def tap_until_found(image_path, util_found_image, interval=1, timeout=10, similarity=0.9, delay=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(interval)
        tap_image(image_path, similarity)
        if wait_for_image(util_found_image, timeout=delay, similarity=similarity) is not None:
            return True
    return False

def tap_any_until_found(image_paths, util_found_image, interval=1, timeout=10, delay=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(interval)
        tap_any(image_paths)
        if wait_for_image(util_found_image, timeout=delay) is not None:
            break


def tap_any_until_notfound_any(image_paths, util_notfound_image, interval=1, timeout=10, delay=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(interval)
        tap_any(image_paths)
        if wait_any_image(util_notfound_image, timeout=delay) is None:
            break


def tap_any_until_found_any(image_paths, util_found_images, interval=1, timeout=10, delay=1):
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(interval)
        tap_any(image_paths)
        if wait_any_image(util_found_images, timeout=delay) is not None:
            break

def tap_until_notfound(image_path, util_notfound_image, interval=1, timeout=10, delay=0.25, similarity=0.9):
    start_time = time.time()
    while time.time() - start_time < timeout:
        time.sleep(interval)
        tap_image(image_path, similarity=similarity)
        time.sleep(delay)
        if wait_until_disappear(util_notfound_image, timeout=delay, similarity=similarity):
            return True
    return False

def tap_offset_until_found(image_path, util_found_image, delay=1, offset_x=0, offset_y=0, timeout=10, similarity=0.9):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if wait_for_image(util_found_image, timeout=delay, similarity=similarity) is not None:
            log(f'tap_offset_util_found: {image_path} until found: {util_found_image} - break')
            return True
        tap_image_offset(image_path, offset_x, offset_y, similarity=similarity)
    return False


def tap_offset_until_notfound(image_path, util_notfound_image, delay=1, offset_x=0, offset_y=0, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        tap_image_offset(image_path, offset_x, offset_y)
        if wait_until_disappear(util_notfound_image, timeout=delay):
            break


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
    folder_path = 'screenshots'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_name = f'screenshot_{datetime_string}.png'
    file_path = os.path.join(folder_path, file_name)
    
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)


def is_found(image_path, similarity=0.9):
    if find_image_with_similarity(image_path, similarity=similarity) is not None:
        log(f"{image_path} is found.")
        return True
    else:
        log(f"{image_path} is not found.")
        return False


def is_found_any(images, similarity=0.90):
    for image in images:
        if is_found(image, similarity):
            return image
    return None


def is_found_within_timeout(image_path, timeout=10, similarity=0.9):
    if wait_for_image(image_path, timeout, similarity) is not None:
        return True
    return False


def hold_press(key, timeout=1):
    if new_sendkey:
        for ld in ld_hwids:
            myclick.send_key(ld, key)
        myclick.send_key(ld_hwid, key)
    else:
        pyautogui.keyDown(key)
        time.sleep(timeout)
        pyautogui.keyUp(key)


def key_press(key):
    if new_sendkey:
        for ld in ld_hwids:
            myclick.send_key(ld, key)
        # myclick.send_key(ld_hwid, key)
    else:
        pyautogui.press(key)


def type(text):
    if new_sendkey:
        myclick.send_input(ld_hwid, text)
    else:
        pyautogui.typewrite(text)


def get_text_from_image(image_filename, offset_x=100, offset_y=45):
    image_obj = find_image_with_similarity(image_filename)
    if image_obj is not None:
        x, y, width, height = image_obj
        screenshot = None
        if new_capture:
            screenshot = window.screenshot()
            x1 = (x + offset_x)
            y1 = (y + offset_y)
            x2 = (x1 + width - offset_x)
            y2 = (y1 + height)
            roi = screenshot[y1:y2, x1:x2]
            screenshot = Image.fromarray(roi)
        else:
            screenshot = pyautogui.screenshot(region=((x + offset_x), (y + offset_y), (width - offset_x), height))
        gray_image = screenshot.convert('L')
        extracted_text = pytesseract.image_to_string(gray_image)
        
        print(extracted_text)
        screenshot.save('test.png')
        return extracted_text


def drag_and_drop_image(source_image, target_image):
    source_object = wait_for_image(source_image)
    target_object = wait_for_image(target_image)
    if source_object is not None and target_object is not None:
        source_x, source_y = find_image_center(source_object)
        target_x, target_y = find_image_center(target_object)
        drag_and_drop(source_x, source_y, target_x, target_y)


def drag_and_drop(source_x, source_y, destination_x, destination_y, duration=0.25, hold=0):
    if new_drag_drop:

        source_x = int(source_x - ld_offset_x)
        source_y = int(source_y - ld_offset_y)
        
        destination_x = int(destination_x - ld_offset_x)
        destination_y = int(destination_y - ld_offset_y)

        myclick.click_hold_and_move(ld_hwid, source_x, source_y, destination_x, destination_y, duration, hold)
    else:
        pyautogui.moveTo(source_x, source_y, duration=duration)
        pyautogui.mouseDown()
        pyautogui.moveTo(destination_x, destination_y, duration=duration)
        time.sleep(hold)
        pyautogui.mouseUp()


def drag_up(image_path, offset_y=100):
    drag_icon = find_image_with_similarity(image_path)
    center_x, center_y = find_image_center(drag_icon)
    drag_and_drop(center_x, center_y, center_x, center_y - offset_y)


def drag_down(image_path, offset_y=100):
    drag_icon = find_image_with_similarity(image_path)
    center_x, center_y = find_image_center(drag_icon)
    drag_and_drop(center_x, center_y, center_x, center_y + offset_y)


def drag_up_location(location, offset_y=100):
    center_x, center_y = find_image_center(location)
    drag_and_drop(center_x, center_y, center_x, center_y - offset_y)


def drag_down_location(location, offset_y=100):
    center_x, center_y = find_image_center(location)
    drag_and_drop(center_x, center_y, center_x, center_y + offset_y)


def scroll_down_util_found(expected_image, drag_image, offset_y=100, similarity=0.9, timeout=10):
    print('scroll to find: ' + expected_image + ' with drag image:' + drag_image)
    return scroll_until_found(expected_image, [drag_image], offset_y=offset_y, is_drag_up=True, similarity=similarity, timeout=timeout)


def scroll_up_util_found(expected_image, drag_image, offset_y=100, similarity=0.9, timeout=10):
    return scroll_until_found(expected_image, [drag_image], offset_y=offset_y, is_drag_up=False, similarity=similarity, timeout=timeout)


def scroll_down_util_found_any_drag_images(expected_image, drag_images, offset_y=100, similarity=0.9, timeout=10):
    return scroll_until_found(expected_image, drag_images, offset_y=offset_y, is_drag_up=True, similarity=similarity, timeout=timeout)


def scroll_up_util_found_any_drag_images(expected_image, drag_images, offset_y=100, similarity=0.9, timeout=10):
    return scroll_until_found(expected_image, drag_images, offset_y=offset_y, is_drag_up=False, similarity=similarity, timeout=timeout)


def scroll_until_found(expected_image, drag_images, offset_y=100, is_drag_up=True, similarity=0.9, timeout=10):
    end_time = time.time() + timeout
    while time.time() < end_time:
        if is_found(expected_image, similarity):
            return True
        
        location = wait_any_image(drag_images, timeout=2)
        if location is not None:
            if is_drag_up:
                drag_up_location(location, offset_y=offset_y)
            else:
                drag_down_location(location, offset_y=offset_y)
        else:
            return False
    return False


def scroll_down_util_not_found(not_expected_image, drag_image, offset_y=100, similarity=0.9, timeout=10):
    return scroll_until_not_found(not_expected_image, drag_image, offset_y=offset_y, is_drag_up=True, similarity=similarity, timeout=timeout)


def scroll_up_util_not_found(not_expected_image, drag_image, offset_y=100, similarity=0.9, timeout=10):
    return scroll_until_not_found(not_expected_image, drag_image, offset_y=offset_y, is_drag_up=False, similarity=similarity, timeout=timeout)


def scroll_until_not_found(not_expected_image, drag_image, offset_y=100, is_drag_up=True, similarity=0.9, timeout=10):
    end_time = time.time() + timeout
    while time.time() < end_time:
        if not is_found(not_expected_image, similarity):
            return True
        if not is_empty(wait_for_image(drag_image, timeout=2)):
            print('Found:' + drag_image + ' found')
            if is_drag_up:
                drag_up(drag_image, offset_y=offset_y)
            else:
                drag_down(drag_image, offset_y=offset_y)
        else:
            print('drag_image:' + drag_image + ' not found')
            return False
        time.sleep(1)
    return False


def write_to_file(file_name, text):
    with open(file_name + '.txt', 'w') as file:
        file.write(text)


def read_file(file_path, file_name):
    with open(file_path + "/" + file_name + '.txt', 'r') as file:
        content = file.read()
    return content

def execute_until_invalid_state(timeout, interval, function, *args):
    end_time = time.time() + timeout
    while time.time() < end_time:
        if not function(*args):
            break
        time.sleep(interval)


def find_target_time(hour, minute):
    target_time = create_target_time(hour, minute, False)
    target_nextday_time = create_target_time(hour, minute, True)
    duration = time_diff(target_time)
    if duration > 0:
        return target_time
    else:
        return target_nextday_time
    

def time_diff(target_time):
    current_time = datetime.datetime.now()
    time_difference = target_time - current_time
    duration = time_difference.total_seconds()
    return duration


def create_target_time(hour, minute, add1day=False):
    if add1day:
        current_date = datetime.datetime.now().date()
        target_time = datetime.datetime.combine(current_date + datetime.timedelta(days=1), datetime.time(hour, minute))
    else:
        target_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    return target_time


def exit_at_specific_time_or_invalid_state(hour, minute, function, *args):
    target_time = find_target_time(hour, minute)
    duration = time_diff(target_time)
    print(duration)
    while duration > 0:
        print(duration)
        if not function(*args):
            break
        duration = time_diff(target_time)


def execute_until_valid_state_with_timeout(timeout, interval, function, *args):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if function(*args):
            return True
        time.sleep(interval)
    return False
