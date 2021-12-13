from random import randint
import requests


def get_hero_photo(url):
    """ get an image of randomly chosen superhero """
    id_hero = randint(1, 730)
    response = requests.get(f'{url}{id_hero}').json()
    with open('images/superhero.jpg', 'wb') as img_file:
        img_hero = requests.get(f"{response.get('image').get('url')}").content
        img_file.write(img_hero)
    return response.get('name')


if __name__ == "__main__":
    API_TOKEN = '2511827112282642'
    url_hero = f'https://superheroapi.com/api/{API_TOKEN}/'
    name = get_hero_photo(url_hero)
    print(f"You've downloaded an image of '{name}'")
