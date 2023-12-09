import boss
import constanst as const
import func
import utils
import img
import sys
import time


def event_boss_hunt(boss_name):
    func.wait_profile()
    utils.tap_all(const.picky_boss_menu_icon)
    utils.wait_and_tap(img.picky_boss_ultimate_clash)
    utils.wait_for_image(img.picky_boss_ultimate_clash_page, timeout=2)
    if utils.is_found(img.picky_boss_ultimate_clash_page):

        if utils.is_found(img.picky_boss_3_3, similarity=0.99):
            utils.tap_image(img.button_back)
            utils.tap_image(img.button_back)
            sys.exit(0)
        
        while True:
            found_image = utils.is_found_any(const.picky_boss_times, similarity=0.99)
            if found_image == img.picky_boss_1m:
                wing_boss(boss_name, 60)
                break
            elif found_image == img.picky_boss_2m:
                wing_boss(boss_name, 120)
                break
            elif found_image == img.picky_boss_3m:
                wing_boss(boss_name, 180)
                break
            elif found_image == img.picky_boss_19m or found_image == img.picky_boss_20m:
                utils.wait_for_image(img.picky_boss_map)
                wing_boss(boss_name, 0)
                break
            time.sleep(1)
            utils.tap_image(img.picky_boss_turn_in)


def wing_boss(boss_name, boss_coord_img, wait_time=60):
    func.wait_and_find_party(img.picky_mvp, f'{boss_name}', 'world', wait_time, True)
    boss.boss(timeout=240, boss_coord_img=boss_coord_img)


def awakening(boss_name):
    similarity = 0.97
    while True:
        func.close_any_panel()
        func.wait_profile()
        func.create_party_and_invite()
        utils.tap_any_offset(const.menu_guides, offset_x=-420)
        utils.tap_until_found(img.awakening_clash_of_chaos, img.awakening_boss_crash_of_chaos_page)

        func.wait(1)
        count3x3 = utils.count_image_on_screen(img.awakening_boss_3x3)
        if count3x3 == 2:
            print(f'finished 3/3')
            break

        while True:
            wait_time = 0
            utils.tap_if_found(img.awakening_boss_hero_challenge)

            if utils.is_found_any([img.awakening_boss_spawned], similarity=similarity):
                wait_time = 30
            elif utils.is_found_any([img.awakening_boss_1m_left, img.awakening_boss_1m_left2], similarity=similarity):
                wait_time = 60
            elif utils.is_found_any([img.awakening_boss_2m_left, img.awakening_boss_2m_left2], similarity=similarity):
                wait_time = 120
            elif utils.is_found_any([img.awakening_boss_3m_left, img.awakening_boss_3m_left2], similarity=similarity):
                wait_time = 180

            if wait_time > 0:
                boss_map_coords = None
                go_buttons = utils.find_all_image_with_similarity(img.awakening_boss_go, similarity)
                if boss_name == 'Hellhound' or boss_name == 'Twilight Bringer' or boss_name == 'Fallen Genesis':
                    utils.tap_location(go_buttons[0])
                    boss_map_coords = [img.chat_party_coord_ant_hell1, img.chat_party_coord_ant_hell2, img.chat_party_coord_ant_hell3]
                else:
                    utils.tap_location(go_buttons[1])
                    boss_map_coords = [img.chat_party_coord_payon_cave_1f1, img.chat_party_coord_payon_cave_1f2, img.chat_party_coord_payon_cave_1f3]
                wing_boss(boss_name, boss_map_coords, wait_time)
                break
