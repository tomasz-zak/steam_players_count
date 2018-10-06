#!/usr/bin/python
import datetime


def save_current_app_list_to_csv(csv_name):
    import requests, json, csv

    all_apps_url = "https://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    current_players_per_app = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid='

    response = requests.get(all_apps_url)
    json_response = json.loads(response.text)
    with open('json_resp.json', 'w') as f:
		f.write(response.text.encode('utf-8'))

    applist = json_response['applist']['apps']['app']

    with open(csv_name, 'wb') as f:
        g = csv.writer(f)
        g.writerow(['AppId', 'AppName'])
        for app in applist:
            g.writerow([app['appid'], app['name'].encode('utf-8')])


def read_key_from_file():
    with open('steamKey.txt', 'r') as f:
        steam_key = f.readline()
    return steam_key

def main():
    save_current_app_list_to_csv(str(datetime.datetime.now()).replace(":", "-")+'.csv')

if __name__ == '__main__':
    main()

