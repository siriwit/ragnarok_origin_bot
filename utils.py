import pyautogui
import pytesseract
import time
import logging
import datetime

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
    image_location = pyautogui.locateOnScreen(image_filename, confidence=similarity, region=region)
    return image_location


def find_all_image_with_similarity(image_filename, similarity=0.9, region=None):
    image_locations = pyautogui.locateAllOnScreen(image_filename, confidence=similarity, region=region)
    grouped = group_coordinate(image_locations)
    return grouped


def find_all_images(image_array):
    all_image_locations = []
    for image in image_array:
        image_locations = find_all_image_with_similarity(image)
        all_image_locations.extend(image_locations)
    return all_image_locations


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
        

def count_image_on_screen(image_filename):
    images = find_all_image_with_similarity(image_filename)
    return len(images)


def count_all_image_on_screen(image_array):
    count = 0
    for image in image_array:
        images = find_all_image_with_similarity(image)
        count += len(images)
    return count


def wait_until_found_all_images(image_array, expected_number, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        count = count_all_image_on_screen(image_array)
        if count == expected_number:
            break
        time.sleep(1)


def wait_for_image(image_filename, timeout=10, enable_log=True):
    start_time = time.time()

    while time.time() - start_time < timeout:
        image_location = find_image_with_similarity(image_filename)
        if image_location is not None:
            log(image_filename + " found.", enable=enable_log)
            return image_location
    log(image_filename + " is not found.", enable=enable_log)
    return None


def wait_any_image(image_filenames, timeout=10):
    start_time = time.time()

    while time.time() - start_time < timeout:
        for image_filename in image_filenames:
            image_location = wait_for_image(image_filename, timeout=1, enable_log=False)
            if image_location is not None:
                log(image_filename + " found.")
                return image_location
    log(image_filename + " is not found.")
    return None


def tap(x, y):
    pyautogui.mouseDown(x, y)
    pyautogui.mouseUp(x, y)


def tap_image(image_path, screenshot=False, before=False, result_filename=None, similarity=0.9):
    image_location = find_image_with_similarity(image_path, similarity=similarity)
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


def tap_location(coordinate):
    center_x, center_y = find_image_center(coordinate)
    tap(center_x, center_y)


def tap_if_found(image_path):
    if is_found(image_path):
        tap_image(image_path)


def tap_all(images):
    for image in images:
        tap_if_found(image)


def tap_any(menu_images, similarity=0.9):
    for menu in menu_images:
        if is_found(menu, similarity):
            tap_image(menu, similarity)
            return


def wait_and_tap(image_path, timeout=10, similarity=0.9):
    wait_for_image(image_path, timeout)
    tap_image(image_path, similarity=similarity)


def wait_and_tap_any(image_paths, timeout=10, similarity=0.9):
    wait_any_image(image_paths, timeout)
    tap_any(image_paths, similarity=similarity)


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


def is_found(image_path, similarity=0.9):
    if find_image_with_similarity(image_path, similarity=similarity) is not None:
        return True
    else:
        return False


def is_found_any(images, threshold=0.90):
    for image in images:
        if is_found(image, threshold):
            return image
    return ''


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


def drag_and_drop_image(source_image, target_image):
    source_x, source_y = find_image_center(find_image_with_similarity(source_image))
    target_x, target_y = find_image_center(find_image_with_similarity(target_image))
    drag_and_drop(source_x, source_y, target_x, target_y)


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


def scroll_down_util_found(expected_image, drag_image, offset_y=100, similarity=0.9):
    print('scroll to find: ' + expected_image + ' with drag image:' + drag_image)
    scroll_until_found(expected_image, drag_image, offset_y=offset_y, is_drag_up=True, similarity=similarity)


def scroll_up_util_found(expected_image, drag_image, offset_y=100, similarity=0.9):
    scroll_until_found(expected_image, drag_image, offset_y=offset_y, is_drag_up=False, similarity=similarity)


def scroll_until_found(expected_image, drag_image, offset_y=100, is_drag_up=True, similarity=0.9):
    while True:
        if is_found(expected_image, similarity):
            break
        wait_for_image(drag_image)
        if is_drag_up:
            drag_up(drag_image, offset_y=offset_y)
        else:
            drag_down(drag_image, offset_y=offset_y)
        time.sleep(1)