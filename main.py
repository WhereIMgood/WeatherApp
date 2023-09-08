import requests as re


def weather(Country, api_key):
	url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={Country}&aqi=no"

	r = re.get(url)
	if r.status_code == 200:
		print(f"Country: {Country}")
		data = r.json()
		print(f'Temperature in degrees Fahrenheit: {data.get("current")["temp_f"]}°F')
		print(f'Temperature in degrees Celsius: {data.get("current")["temp_c"]}°C')
	else:
		print("Error Sending the http request: ",r.status_code)

def get_country_name():
    try:
        response = re.get('https://ipinfo.io')
        data = response.json()

        country_name = data.get('timezone')

        return country_name

    except Exception as e:
        print(f"Error: {e}")
        return None

# Get and print the country name
country_name = get_country_name()
weather(country_name, "631e2a1e983546a9aa6113002230809")
