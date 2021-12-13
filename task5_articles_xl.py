from random import choice, randrange
from string import ascii_uppercase as asciiup
from faker import Faker
from openpyxl import Workbook

f = Faker()


class Article:

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

    def textile_format_xl(self, textile):
        textile_xl = sorted([(i["percent"], i["material"]) for i in textile], reverse=True)
        textile_xl = ", ".join([f'{i[0]} % {i[1]}' for i in textile_xl])
        return textile_xl

    def generate_textile(self):
        """ create a nested dict containing info about
            textile: name and percentage of material """
        percents = [p for p in range(10, 101, 10)]
        materials = ["cotton", "silk", "polyester", "viscose", "acrylic"]

        i, textile = 0, list()
        percent = choice(percents)
        while i + percent < 100 and len(textile) < 5:
            material = choice(materials)
            textile.append({"material": material, "percent": percent})
            i += percent
            materials.remove(material)
            percent = choice(percents)
        textile.append({"material": choice(materials), "percent": 100 - i})

        textile = self.textile_format_xl(textile)
        return textile

    def generate_articles(self):
        """ generate an article with random params """
        article = {
            "id": self.id_num,
            "article": self.art,
            "category": self.category,
            "weight": self.weight,
            "type": self.cloth_type,
            "colour": f.color_name(),
            "textile": self.generate_textile(),
            "description": f.text()
        }
        return article


if __name__ == "__main__":
    # save into excel file:
    wb = Workbook()
    ws = wb.active

    num = int(input("How many articles do you want to create?\nNumber of articles: "))
    articles_list = [Article(i+1).generate_articles() for i in range(num)]
    # write names of columns:
    column_names = [i for i in articles_list[0]]
    ws.append(column_names)
    # write lines:
    for art in articles_list:
        line = [i for i in art.values()]
        ws.append(line)

    wb.save("task5_articles.xlsx")
