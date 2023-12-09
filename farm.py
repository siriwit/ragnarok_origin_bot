import func
import img
import utils

def farm():
    while True:
        func.wait_profile()
        func.ang_pao()
        func.use_items()
        func.wait(1)

        if utils.is_found(img.fatique_icon, similarity=0.85):
            utils.tap_until_notfound(img.fatique_close, img.fatique_close)
            func.butterfly_wing_morroc()
            break