import constanst as const
import img
import func


def card_weapon(size, element, tribe):
    if size == const.medium:
        card_objects = [func.card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                    func.card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
    elif size == const.large:
        card_objects = [func.card_change_object(img.card_minorous, img.card_minorous_current, img.card_minorous_touse),
                    func.card_change_object(img.card_minorous, img.card_minorous_current, img.card_minorous_touse)]
    elif element == const.fire:
        card_objects = [func.card_change_object(img.card_vadon, img.card_vadon_current, img.card_vadon_touse),
                    func.card_change_object(img.card_vadon, img.card_vadon_current, img.card_vadon_touse)]
    elif element == const.wind:
        card_objects = [func.card_change_object(img.card_mandragora, img.card_mandragora_current, img.card_mandragora_touse),
                    func.card_change_object(img.card_mandragora, img.card_mandragora_current, img.card_mandragora_touse)]
    elif element == const.water:
        card_objects = [func.card_change_object(img.card_drainliar, img.card_drainliar_current, img.card_drainliar_touse),
                    func.card_change_object(img.card_drainliar, img.card_drainliar_current, img.card_drainliar_touse)]
    elif tribe == const.demon:
        card_objects = [func.card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse),
                    func.card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse)]
    elif tribe == const.brute:
        card_objects = [func.card_change_object(img.card_goblin, img.card_goblin_current, img.card_goblin_touse),
                    func.card_change_object(img.card_goblin, img.card_goblin_current, img.card_goblin_touse)]
    elif tribe == const.formless:
        card_objects = [func.card_change_object(img.card_peco_egg, img.card_peco_egg_current, img.card_peco_egg_touse),
                    func.card_change_object(img.card_peco_egg, img.card_peco_egg_current, img.card_peco_egg_touse)]
    elif element == const.shadow:
        card_objects = [func.card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse),
                    func.card_change_object(img.card_strouf, img.card_strouf_current, img.card_strouf_touse)]
    else:
        card_objects = [func.card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse),
                    func.card_change_object(img.card_skeleton_worker, img.card_skeleton_worker_current, img.card_skeleton_worker_touse)]
        
    return card_objects


def card_armor(tribe, boss_level, element):
    if tribe == const.human:
        card_objects = [func.card_change_object(img.card_dokebi, img.card_dokebi_current, img.card_dokebi_touse)]
    elif boss_level > 0 and boss_level < 100:
        card_objects = [func.card_change_object(img.card_peco_peco, img.card_peco_peco_current, img.card_peco_peco_touse)]
    elif element == const.earth:
        card_objects = [func.card_change_object(img.card_sandman, img.card_sandman_current, img.card_sandman_touse)]
    elif element == const.fire:
        card_objects = [func.card_change_object(img.card_pasana, img.card_pasana_current, img.card_pasana_touse)]
    elif element == const.water:
        card_objects = [func.card_change_object(img.card_swordfish, img.card_swordfish_current, img.card_swordfish_touse)]
    elif element == const.wind:
        card_objects = [func.card_change_object(img.card_dokebi, img.card_dokebi_current, img.card_dokebi_touse)]
    elif element == const.shadow or element == const.undead:
        card_objects = [func.card_change_object(img.card_argiope, img.card_argiope_current, img.card_argiope_touse)]
    else:
        card_objects = [func.card_change_object(img.card_peco_peco, img.card_peco_peco_current, img.card_peco_peco_touse)]

    return card_objects


def card_shield(tribe, boss_level):
    if tribe == const.human:
        card_objects = [func.card_change_object(img.card_tirfing, img.card_tirfing_current, img.card_tirfing_touse)]
    elif boss_level > 0 and boss_level < 100:
        card_objects = [func.card_change_object(img.card_alice, img.card_alice_current, img.card_alice_touse)]
    else:
        card_objects = [func.card_change_object(img.card_alice, img.card_alice_current, img.card_alice_touse)]

    return card_objects


def card_cloak(tribe, element, boss_level):
    if tribe == const.human:
        card_objects = [func.card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse),
                        func.card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse)]
    elif boss_level > 0 and boss_level < 100:
        card_objects = [func.card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse),
                        func.card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    elif element == const.earth:
        card_objects = [func.card_change_object(img.card_hode, img.card_hode_current, img.card_hode_touse),
                        func.card_change_object(img.card_hode, img.card_hode_current, img.card_hode_touse)]
    elif element == const.fire:
        card_objects = [func.card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse),
                        func.card_change_object(img.card_jakk, img.card_jakk_current, img.card_jakk_touse)]
    elif element == const.water:
        card_objects = [func.card_change_object(img.card_marse, img.card_marse_current, img.card_marse_touse),
                        func.card_change_object(img.card_marse, img.card_marse_current, img.card_marse_touse)]
    elif element == const.wind:
        card_objects = [func.card_change_object(img.card_dustiness, img.card_dustiness_current, img.card_dustiness_touse),
                        func.card_change_object(img.card_dustiness, img.card_dustiness_current, img.card_dustiness_touse)]
    elif element == const.shadow:
        card_objects = [func.card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse),
                        func.card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse)]
    elif element == const.undead:
        card_objects = [func.card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse),
                        func.card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse)]
    elif element == const.poison:
        card_objects = [func.card_change_object(img.card_myst, img.card_myst_current, img.card_myst_touse),
                        func.card_change_object(img.card_myst, img.card_myst_current, img.card_myst_touse)]
    elif element == const.neutral:
        card_objects = [func.card_change_object(img.card_orc_baby, img.card_orc_baby_current, img.card_orc_baby_touse),
                        func.card_change_object(img.card_raydric, img.card_raydric_current, img.card_raydric_touse)]
    else:
        card_objects = [func.card_change_object(img.card_isis, img.card_isis_current, img.card_isis_touse),
                        func.card_change_object(img.card_orc_zombie, img.card_orc_zombie_current, img.card_orc_zombie_touse)]
        
    return card_objects
