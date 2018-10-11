#!/usr/bin/python
import datetime
from steamAPINames import all_apps_url

def save_current_app_list_to_csv(csv_name):
    import requests, json, csv

    response = requests.get(all_apps_url())
    json_response = json.loads(response.text)
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

def save_current_players_count_to_csv(csv_name, app_id):
	import requests, json, csv
	from steamAPINames import current_players
	response = requests.get(current_players(app_id))
	json_response = json.loads(response.text)
	
	with open(csv_name, 'wb') as f:
		g = csv.writer(f)
		g.writerow(['AppId', 'PlayerCount','Date'])
		g.writerow([app_id, json_response['response']['player_count'],
		str(datetime.datetime.now())])

def main():
	pass
    #save_current_app_list_to_csv(str(datetime.datetime.now()).replace(":", "-")+'.csv')

if __name__ == '__main__':
    main()

