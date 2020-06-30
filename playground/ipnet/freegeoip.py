import requests



url = "https://freegeoip.app/json/"



headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)






#if __name__ == "__main__":
#	dict = get_location_info(link)
#	for i in dict.keys():
#		print(i, dict[i])
#	print("!!!!!',/n, '!!!!!', /n, '!!!!!")
#	
#	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#	print(type(get_location_myip(link3)))
	
