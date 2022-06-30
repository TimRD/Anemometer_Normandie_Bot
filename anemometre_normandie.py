#Import the following values from an access.py file to use the twitter API
#API_KEY =
#API_SECRET =
#ACCESS_TOKEN =
#ACCESS_TOKEN_SECRET =
from access import *
import tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import requests

def Villers_sur_Mer():
    r = requests.get('http://api.pioupiou.fr/v1/live/562')
    contenu=r.json()
    contenu2 = json.dumps(contenu)
    y = json.loads(contenu2)
    print("------")
    spot='Spot ' + y["data"]["meta"]["name"]+'\n'
    wind_speed ='Vitesse vent ' + repr(y["data"]["measurements"]["wind_speed_avg"]) +'nds \n'
    wind_heading='Wind direction ' + repr(y["data"]["measurements"]["wind_heading"]) +'° \n'
    spot = spot + wind_speed + wind_heading
    print(spot)
    try:
        api.update_status(spot)
    except:
        print("An exception occurred for Spot Villers_sur_Mer")

def berniere():
    options = Options()
    options.headless = True
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://www.windguru.cz/station/1147')
    time.sleep(1)
    wind = driver.find_element_by_css_selector('span.wgs_wind_avg_value').text
    name = driver.find_element_by_css_selector('span.wgs_station_name').text
    direction2 = driver.find_element_by_css_selector('div.wgs-data.wgs-wind.wgs-wind-dir-txt.wgs_wind_avg_color').text
    print("------")
    print("nom : ", name)
    print("Wind speed : ", wind, "nds")
    print("Wind direction : ", direction2)

    spot='Spot ' + name + '\n'
    wind_speed ='Wind speed ' + wind +'nds \n'
    wind_heading='Wind direction ' + direction2 +'\n'
    spot = spot + wind_speed + wind_heading
    try:
        api.update_status(spot)
    except:
        print("An exception occurred for Spot Berniere sur Mer")

def langrune():
    options = Options()
    options.headless = True
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://www.windguru.cz/station/1495')
    time.sleep(1)
    wind = driver.find_element_by_css_selector('span.wgs_wind_avg_value').text
    direction2 = driver.find_element_by_css_selector('div.wgs-data.wgs-wind.wgs-wind-dir-txt.wgs_wind_avg_color').text
    print("------")
    print("Spot = Langrune sur mer")
    print("vitesse vent : ", wind, "nds")
    print("orientation vent : ", direction2)

    spot='Spot Langrune sur Mer \n'
    wind_speed ='Wind speed ' + wind + 'nds \n'
    wind_heading='Wind direction ' + direction2 + '\n'
    spot = spot + wind_speed + wind_heading
    try:
        api.update_status(spot)
    except:
        print("An exception occurred for Spot Langrune sur Mer")



def ouistreham():
    r = requests.get('https://data.diabox.com/recentDataAverage.php?dbx_id=114&dataNameList%5B%5D=wind')
    name="Ouistreham"
    contenu = r.json()
    contenu2 = json.dumps(contenu)
    y = json.loads(contenu2)
    print("------")
    print("nom : ", name)
    print("Wind speed : ", y["wind"]["force_avg"], "nds (min ",
          y["wind"]["force_min"], "nds - max", y["wind"]["force_max"],
          "nds)")
    print("wind direction : ", y["wind"]["dir_avg"], "°")
    spot='Spot Ouistreham\n'
    speed=round(y["wind"]["force_avg"], 1)
    heading = round(y["wind"]["dir_avg"], 1)
    wind_speed ='Wind speed ' + repr(speed) +'nds \n'
    wind_heading='Wind direction ' + repr(heading) +'° \n'
    spot = spot + wind_speed + wind_heading
    try:
        api.update_status(spot)
    except:
        print("An exception occurred for Spot Ouistreham")

def kiter():
    options = Options()
    options.headless = True
    # options.add_argument("--window-size=1920,1200")
    DRIVER_PATH = '/Users/timotheemarguier/Downloads/chromedriver'
    driver2 = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver2.get('https://kite-r.com/meteo-webcam-merville-franceville')
    time.sleep(1)

    wind_value = driver2.find_element_by_css_selector('div.text-3xl.leading-tight').text
    wind_orientation = driver2.find_element_by_xpath('/html/body/div[1]/nav/div[1]/div[2]/div/div[2]/div[2]').text
    print("------")
    print('nom = Franceville-Merville KiteR Evolution')
    print("Wind speed : ", wind_value, "nds")
    print("Wind direction: ", wind_orientation)

    spot='Spot Franceville-Merville\n'
    wind_speed ='Wind speed ' + wind_value +'nds \n'
    wind_heading='Wind direction ' + wind_orientation +' \n'
    spot = spot + wind_speed + wind_heading

    try:
        api.update_status(spot)
    except:
        print("An exception occurred for Spot Franceville-Merville")



berniere()
langrune()
kiter()
#Ouitstreham anemometer is in maintenance for the moment
#ouistreham()
Villers_sur_Mer()