import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "COVID_19_API.settings.local")
django.setup()

from bs4 import BeautifulSoup
import requests

from api.models import *


def main():
	url = 'https://www.worldometers.info/coronavirus/'
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	table = soup.find('table', id='main_table_countries_today')
	table_body = table.find('tbody')
	rows = table_body.find_all('tr')
	data = []
	
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		obj = CoronaCounrty.objects.get_or_create(
			country=cols[0],
		)
		CoronaCounrty.objects.filter(id=obj[0].id).update(
			total_cases=cols[1].replace(",", "").replace("+", ""),
			new_cases=cols[2].replace(",", "").replace("+", ""),
			total_deaths=cols[3].replace(",", "").replace("+", ""),
			new_deaths=cols[4].replace(",", "").replace("+", ""),
			total_recovered=cols[5].replace(",", "").replace("+", ""),
			active_cases=cols[6].replace(",", "").replace("+", ""),
			serious_cases=cols[7].replace(",", "").replace("+", ""),
			tot_cases=cols[8].replace(",", "").replace("+", "")
		)
		data.append(cols)
	
	print(data)


if __name__ == "__main__":
	main()
