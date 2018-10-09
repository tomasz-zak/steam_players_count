def all_apps_url():
    return "https://api.steampowered.com/ISteamApps/GetAppList/v0001/"

def current_players(app_id):
	return 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid={}'.format(app_id)

