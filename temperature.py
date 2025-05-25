import requests
from bs4 import BeautifulSoup


class Temperature:
    """Represents a temperature value extracted from the timeanddate.com/weather webpage
    """
    base_url = "https://www.timeanddate.com/weather/"

    def __init__(self, country, city):
        self.city = city.lower().replace(" ", "-")
        self.country = country.lower().replace(" ", "-")

    def get(self):
        url = f"{self.base_url}{self.country}/{self.city}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch page. Status Code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        temp_element = soup.find("div", class_="h2")
        if temp_element:
            return temp_element.text.strip()
        else:
            raise Exception("Temperature Element not found on the page")

print(Temperature("Bulgaria", "Sofia").get())