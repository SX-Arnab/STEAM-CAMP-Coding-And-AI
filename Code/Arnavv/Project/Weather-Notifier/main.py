import time
import schedule
import requests
import json
from plyer import notification




def rain_notifier():
    lat = 27.429
    lon = 85.030
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=precipitation_probability_max&timezone=auto'
    data = requests.get(url).json()

    rain_prob = data['daily']['precipitation_probability_max'][0]

    with open('data.json', 'w') as f:
        json.dump(data,f, indent = 2)
        
    # if rain_prob >=25:
    notification.notify(
        title='Rain Probability',
        message='Carry an umbrella',
        app_name='Weather Notifier',
        app_icon=r"C:\Users\Students\Downloads\4092563-bell-mobile-ui-notification-ui-website_114040.ico",  # Path to a .ico or .png file depending on your OS
        timeout=10,      # Seconds the notification stays on screen
    )
schedule.every().day.at("10:00").do(rain_notifier)
while True:
    schedule.run_pending()
    time.sleep(60)