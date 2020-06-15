import requests




link = "http://api.ipstack.com/134.201.250.155"
link2 = "https://api.ipify.org?format=json"
link3 = "https://api.myip.com"

def get_location_info(pick_link):
	params1 = dict(access_key='ff3fe24a9b6a8b6f5822baaea8e66fc3')
	return requests.get(pick_link, dict(access_key='ff3fe24a9b6a8b6f5822baaea8e66fc3')	).json()
	
def get_location_info_ipify(pick_link):
	return requests.get(pick_link).json()

def get_location_myip(pick_link):
	return requests.get(pick_link).json






if __name__ == "__main__":
	dict = get_location_info(link)
	for i in dict.keys():
		print(i, dict[i])
	print("!!!!!',/n, '!!!!!', /n, '!!!!!")
	
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print(type(get_location_myip(link3)))
	
