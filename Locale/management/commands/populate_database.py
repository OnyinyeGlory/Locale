from django.core.management import BaseCommand
import requests

from Locale.models import Region, State, LGA, City


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        help = """
        This function runs at project initialization.
        It populates the database with the data from the external API.
        """

        if Region.objects.all().count() > 0:
            self.stdout.write(self.style.SUCCESS('Database already populated'))
            return

        try:
            # Populate States
            print("Getting states...")
            url = "https://api.facts.ng/v1/states"
            response = requests.get(url)
            states = response.json()

            for state in states:
                print(f"=======================Populating {state['name']}=======================")
                region = Region.objects.filter(name=state['region']).first()
                if not region:
                    region = Region.objects.create(name=state['region'])
                state = State.objects.create(id=state['id'], name=state['name'], capital=state['capital'], slogan=state['slogan'], region=region)

                # Populate LGAs and Cities
                url = f"https://api.facts.ng/v1/states/{state.id}"
                response = requests.get(url)
                state_data = response.json()

                for lga in state_data['lgas']:
                    print(f"LGA {lga}...")
                    LGA.objects.create(name=lga, state=state)
                
                for city in state_data.get("towns", []):
                    print(f"City {city}...")
                    City.objects.create(name=city, state=state)

                print(f"======================={state.name} done=======================")

        except Exception as e:
            Region.objects.all().delete()
            self.stdout.write(self.style.ERROR(f'Error populating database: {e}'))
            return

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
