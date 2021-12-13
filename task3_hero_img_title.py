from random import randrange
import requests


def get_hero(url):
    """ get an image of randomly chosen superhero
        and save give a convenient name to picture """
    id_hero = randrange(700)
    response = requests.get(f'{url}{id_hero}').json()
    img_name = response['biography']['full-name'].replace(' ', '_')
    with open(f"images/{img_name}.jpg", 'wb') as img_file:
        img_hero = requests.get(f"{response['image']['url']}").content
        img_file.write(img_hero)
    return img_name


if __name__ == "__main__":
    API_TOKEN = '2511827112282642'
    url_hero = f'https://superheroapi.com/api/{API_TOKEN}/'
    print(get_hero(url_hero))
