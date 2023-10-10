import img
import utils
import time
import numpy as np
from sklearn.cluster import DBSCAN

wait_images = [
        img.halfyear_match_card_doppel, 
        img.halfyear_match_card_dracular, 
        img.halfyear_match_card_hydra, 
        img.halfyear_match_card_moonlight,
        img.halfyear_match_card_osiris,
        img.halfyear_match_card_owl_baron,
        img.halfyear_match_card_pharaoh,
        img.halfyear_match_card_phreeoni,
        img.halfyear_match_card_poring_angel,
        img.halfyear_match_card_skeleton_worker,
        img.halfyear_match_card_bapho
    ]
mem = {}

def flipcard():
    # utils.wait_and_tap(img.halfyear_match_start_button)
    
    while True:
        back_cards = utils.find_all_image_with_similarity(img.halfyear_match_card_back, similarity=0.9)
        for i in range(0, len(back_cards), 2):
            first = back_cards[i]
            second = back_cards[i+1]
            print("First location:" + str(first))
            print("Second location:" + str(second))
            utils.tap_location(first)
            time.sleep(0.25)
            find_card_type(True)
            utils.tap_location(second)
            time.sleep(0.25)
            find_card_type(False)

        print(mem)

def find_card_type(is_first=True):
    poring_location = utils.find_image_with_similarity(img.halfyear_match_card_poring_angel)
    bapho_location = utils.find_image_with_similarity(img.halfyear_match_card_bapho)
    maya_location = utils.find_image_with_similarity(img.halfyear_match_card_maya)
    doppel_location = utils.find_image_with_similarity(img.halfyear_match_card_doppel)
    if not utils.is_empty(poring_location):
        print("found poring" + str(poring_location))
        check_match(img.halfyear_match_card_poring_angel, poring_location, is_first)
    if not utils.is_empty(bapho_location):
        print("found bapho" + str(bapho_location))
        check_match(img.halfyear_match_card_bapho, bapho_location, is_first)
    if not utils.is_empty(maya_location):
        print("found maya" + str(maya_location))
        check_match(img.halfyear_match_card_maya, maya_location, is_first)
    if not utils.is_empty(doppel_location):
        print("found maya" + str(doppel_location))
        check_match(img.halfyear_match_card_doppel, doppel_location, is_first)

def check_match(card_img, location, is_first=True):
    if card_img in mem:
        if not is_first:
            time.sleep(1)
            utils.tap_location(mem[card_img])
            utils.tap_location(location)
            return True
    else:
        mem[card_img] = location
    return False