from scrapy.item import Field, Item


class CulturalItem(Item):
    cidade = Field()
    artista = Field()
    dia = Field()
