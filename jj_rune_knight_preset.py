import constanst as const
import img
import func
import utils


def change_skill_auto():
    utils.scroll_down_util_found(img.preset_skill_dragon_breath_water_touse, img.preset_skill_drag_icon_damage_skills, offset_y=200)
    func.ensure_use_support_skill(img.preset_skill_dragon_howling, img.preset_skill_dragon_howling_touse)
    # func.ensure_use_support_skill(img.preset_skill_dragon_breath_fire, img.preset_skill_dragon_breath_fire_touse)
    func.ensure_use_support_skill(img.preset_skill_dragon_breath_water, img.preset_skill_dragon_breath_water_touse)

    if not utils.is_found(img.preset_skill_drag_icon_support_skill) and utils.is_found(img.preset_skill_drag_icon_damage_skills):
        utils.scroll_down_util_found(img.preset_skill_full_throttle_touse, img.preset_skill_drag_icon_damage_skills, offset_y=200)
    utils.scroll_down_util_found(img.preset_skill_full_throttle_touse, img.preset_skill_drag_icon_support_skill, offset_y=200)
    func.ensure_use_support_skill(img.preset_skill_enchant_blade, img.preset_skill_enchant_blade_touse)
    func.ensure_use_support_skill(img.preset_skill_full_throttle, img.preset_skill_full_throttle_touse)

