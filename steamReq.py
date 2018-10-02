class SteamReq():
	def __init__(self, url):
		print("Init klasy nadrzednej")
		#<cr>main_url = "https://apiesteampowered.com/ISteamApps/" # GetAppList/v0001/":
		#<cr>API_version = 'v1'
		#<cr>my_url = url


	def print_count():
		print(requests_count)


	def increase_count():
		SteamReq.requests_count+=1
	
	def make_request():
		pass


class AllAppsReq(SteamReq):
	def __init__(self):
		super(AllAppsReq, self).__init__('mamma mia')
		print("Init klasy pochodnej")
