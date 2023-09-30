import alfheim
import anthem
import catpaw
import demon_treasure as dt
import guild_expedition as ge
import time_anomaly as ta
import feast as fe
import func
import preset
import schedule
import time
import ygg


def guild_expedition():
    ge.preset()
    ge.start()


def time_anomaly():
    ta.preset()
    ta.start()


def feast():
    fe.start()


def daily():
    func.use_items()
    preset.daily()
    func.leave_party()
    alfheim.alfheim_collect_item()
    dt.daily_demon_treasure()
    catpaw.daily_cat_paw()
    anthem.daily_anthem()
    anthem.daily_anthem()


def ygg_fight():
    ygg.ygg_fight()


# Schedule the function to be called daily at a specific time

# monday
schedule.every().monday.at("07:00").do(ygg_fight)
schedule.every().monday.at("20:00").do(feast)

# tuesday
schedule.every().monday.at("07:00").do(ygg_fight)
schedule.every().tuesday.at("20:00").do(feast)
schedule.every().tuesday.at("20:30").do(time_anomaly)

# wednesday
schedule.every().tuesday.at("20:00").do(feast)

# thursday
schedule.every().thursday.at("20:00").do(feast)
schedule.every().thursday.at("20:30").do(guild_expedition)

# friday
schedule.every().friday.at("20:00").do(feast)

# saturday
schedule.every().saturday.at("20:00").do(feast)
schedule.every().saturday.at("20:30").do(time_anomaly)

# sunday
schedule.every().sunday.at("20:30").do(guild_expedition)

# everyday
schedule.every().days.at("10:33").do(daily)

# Keep the program running to allow scheduling to work
while True:
    schedule.run_pending()
    time.sleep(1)
