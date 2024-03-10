class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category} | Active: {self._active}'

    @property
    def active(self) -> str:
        return "The store is operational" if self._active else "The store is not operational"

    @classmethod
    def list_restaurants(cls):
        print(f'{'Nome do Restaurante'.ljust(25)}|{'Categoria'.ljust(25)}|{'Status'.ljust(25)}')
        print()
        for restaurante in Restaurant.restaurants:
            print(f'{restaurante._name.ljust(25)}|{restaurante._category.ljust(25)}|{restaurante.active.ljust(25)}')

    def alter_active(self):
        self._active = not self._active

