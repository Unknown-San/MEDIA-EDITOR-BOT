import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5581489100:AAExAud0mvPt7ep-7c706ciXMq7Ipm3teDA")

    APP_ID = int(os.environ.get("APP_ID", 4665778))

    API_HASH = os.environ.get("API_HASH", "10e3ed833b0d09699973420d45359409")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1943966786").split())
  
    
