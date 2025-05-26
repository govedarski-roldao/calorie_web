import requests
from bs4 import BeautifulSoup
from selectorlib import Extractor


class Temperature:
    """Represents a temperature value extracted from the timeanddate.com/weather webpage
    """
    base_url = "https://www.timeanddate.com/weather/"
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    yml_path = "temperature.yaml"

    def __init__(self, country, city):
        self.city = city.lower().replace(" ", "-")
        self.country = country.lower().replace(" ", "-")

    def build_url(self):


    def get(self):
        url = f"{self.base_url}{self.country}/{self.city}"
        response = requests.get(url, headers=self.headers)
        #
        # if response.status_code != 200:
        #     raise Exception(f"Failed to fetch page. Status Code: {response.status_code}")
        #
        # soup = BeautifulSoup(response.text, "html.parser")
        # temp_element = soup.find("div", class_="h2")
        # if temp_element:
        #     return temp_element.text.strip()
        # else:
        #     raise Exception("Temperature Element not found on the page")
        # or
        if response.status_code != 200:
            raise Exception(f"Failed to fetch page. Status Code: {response.status_code}")

        extractor = Extractor.from_yaml_file(self.yml_path)
        result = extractor.extract(response.text)
        result = result["temp"].replace("\xa0°C", "")
        return result


if __name__ == "__main__":
    temperature = Temperature("Bulgaria", "Sofia")
    print(temperature.get())
