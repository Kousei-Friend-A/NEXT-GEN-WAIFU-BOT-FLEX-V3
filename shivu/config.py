class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6649521395"
    sudo_users = ["5630057244", "2010819209", "5702598840", "6101457748", "6154972031", "1735664760", "7036005233", "6100011620", "7297953309", "6412447141", "7244871367", "5530116994", "6584789596", "949302414"]
    GROUP_ID = "-1002383369786"
    TOKEN = "7501936092:AAHdgIDKUwMKCffWehEAl1aZ6GiX1zADaUA"
    mongo_url = "mongodb://root:SzobqGSLSTsJH6fhoPAy4xIl7Sx2vxJX9ilCMflCU1gp2rPggyOfQ7Zsqa8EZ6yS@dsgkso48c4wkkg0cgc44cgco:27017/?directConnection=true"
    PHOTO_URL = ["https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg", "https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/32556c77847dff110577c.jpg", "https://telegra.ph//file/0650844fc5db4049959bc.jpg"]
    SUPPORT_CHAT = "Grabbing_Your_WH_Group"
    UPDATE_CHAT = "FLEX_BOTS_NEWS"
    BOT_USERNAME = "WaifuGachaX_Robot"
    CHARA_CHANNEL_ID = "-1002317637451"
    api_id = "12321125"
    api_hash = "6a34b69aa63177ec36f8d9b24c296f40"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
