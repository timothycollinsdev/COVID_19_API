import json
from django.core.management.base import BaseCommand
from api.models import *
from bs4 import BeautifulSoup
import requests

class Command(BaseCommand):
    help = 'adding data in database'

    def handle(self, *args, **kwargs):
        # Get all the orders that don't have item_data
        # NOTE: This command should be run before deleting items against orders
        url = 'https://www.worldometers.info/coronavirus/'
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        table = soup.find('table', id='main_table_countries_today')
        if table:
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
                    total_cases=cols[1],
                    new_cases=cols[2],
                    total_deaths=cols[3],
                    new_deaths=cols[4],
                    total_recovered=cols[5],
                    active_cases=cols[6],
                    serious_cases=cols[7],
                    tot_cases=cols[8]
                )
                if obj[0].track_it:
                    TrackCountry.objects.update_or_create(
                        country=cols[0],
                        total_cases=cols[1],
                        new_cases=cols[2],
                        total_deaths=cols[3],
                        new_deaths=cols[4],
                        total_recovered=cols[5],
                        active_cases=cols[6],
                        serious_cases=cols[7],
                        tot_cases=cols[8]
                    )
