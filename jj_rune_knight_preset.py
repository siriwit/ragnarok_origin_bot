import constanst as const
import img
import func
import utils


def change_skill_auto(preset=const.boss):
    scroll_to_damage_skill()
    utils.scroll_down_util_found(img.preset_skill_dragon_breath_water_touse, img.preset_skill_drag_icon_damage_skills)
    if preset == const.mr:
        func.remove_skill_if_needed(img.preset_skill_dragon_howling)
        func.remove_skill_if_needed(img.preset_skill_dragon_breath_fire)
        func.remove_skill_if_needed(img.preset_skill_dragon_breath_water)
        func.remove_skill_if_needed(img.preset_skill_enchant_blade)
    else:
        func.ensure_use_support_skill(img.preset_skill_dragon_howling, img.preset_skill_dragon_howling_touse)
        func.ensure_use_support_skill(img.preset_skill_dragon_breath_fire, img.preset_skill_dragon_breath_fire_touse)
        func.ensure_use_support_skill(img.preset_skill_dragon_breath_water, img.preset_skill_dragon_breath_water_touse)

        scroll_to_support_skill()
        func.ensure_use_support_skill(img.preset_skill_enchant_blade, img.preset_skill_enchant_blade_touse)
        func.ensure_use_support_skill(img.preset_skill_full_throttle, img.preset_skill_full_throttle_touse)


def change_skill_manual(preset=const.boss):
    if preset == const.boss:
        scroll_to_support_skill()
        func.ensure_replace_skill(img.preset_skill_provoke, img.preset_skill_touse_provoke, [img.preset_skill_rune_of_mercy])
    elif preset == const.pvp or preset == const.boss_event:
        scroll_to_support_skill()
        func.ensure_replace_skill(img.preset_skill_rune_of_mercy, img.preset_skill_touse_rune_of_mercy, [img.preset_skill_provoke])


def scroll_to_support_skill():
    scroll_to_damage_skill()
    utils.scroll_down_util_found(img.preset_skill_dragon_breath_water_touse, img.preset_skill_drag_icon_damage_skills)
    if not utils.is_found(img.preset_skill_drag_icon_support_skill) and utils.is_found(img.preset_skill_drag_icon_damage_skills):
        utils.scroll_down_util_found(img.preset_skill_full_throttle_touse, img.preset_skill_drag_icon_damage_skills)
    utils.scroll_down_util_found(img.preset_skill_full_throttle_touse, img.preset_skill_drag_icon_support_skill)


def scroll_to_damage_skill():
    if utils.is_found(img.preset_skill_drag_icon_statue_skill):
        utils.scroll_up_util_found(img.preset_skill_drag_icon_support_skill, img.preset_skill_drag_icon_statue_skill)
    if utils.is_found(img.preset_skill_drag_icon_support_skill):
        utils.scroll_up_util_found(img.preset_skill_drag_icon_damage_skills, img.preset_skill_drag_icon_support_skill)