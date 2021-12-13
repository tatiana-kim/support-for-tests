from random import choice, randrange
from string import ascii_uppercase as asciiup
import json
from faker import Faker

fake = Faker()


class Article:
    """ create a json-file with N randomly generated articles """

    def __init__(self, id_num):
        self.id_num = id_num
        self.category = choice(["outerwear", "shirt", "socks"])
        self.categ_choices = {"outerwear": [randrange(1000, 10001), choice(['coat', 'jacket', 'windbreaker'])],
                              "shirt": [randrange(100, 2001), choice(['casual', 'dress', 'loosefit'])],
                              "socks": [randrange(10, 301), None]}
        self.weight = self.categ_choices[self.category][0]
        self.cloth_type = self.categ_choices[self.category][1]
        self.code_letter = "".join(choice(asciiup) for _ in range(2))
        self.code_num = "".join(str(randrange(10)) for _ in range(2))
        self.art = f'OZON_{self.category}_{self.code_letter}{self.code_num}'

    def generate_textile(self):
        """ create a nested dict containing info about
            textile: name and percentage of material """
        percents = [p for p in range(10, 101, 10)]
        materials = ["cotton", "silk", "polyester", "viscose", "acrylic"]

        ind, textile = 0, list()
        percent = choice(percents)
        while ind + percent < 100 and len(textile) < 5:
            material = choice(materials)
            textile.append({"material": material, "percent": percent})
            ind += percent
            materials.remove(material)
            percent = choice(percents)
        textile.append({"material": choice(materials), "percent": 100 - ind})
        return textile

    def generate_article(self):
        """ generate an article with random params """
        article = dict()
        for _i in range(8):
            article["id"] = self.id_num
            article["article"] = self.art
            article["category"] = self.category
            article["weight"] = self.weight
            if self.category != "socks":
                article["type"] = self.cloth_type
            article["colour"] = fake.color_name()
            article["textile"] = self.generate_textile()
            article["description"] = fake.text()
        return article


if __name__ == "__main__":
    result = list()
    num = int(input("How many articles do you want to create?\nNumber of articles: "))
    for i in range(num):
        result.append(Article(i+1).generate_article())
    art_json = json.dumps(result, indent=4)
    print(art_json)
