def list_restaurants():
    for restaurante in Restaurant.restaurants:
        print(f'{restaurante.name} | {restaurante.category} | {restaurante.status}')


class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.status = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self.name} | {self.category}'


restaurant_Pizza = Restaurant("Pizza Hut", "Pizza")
restaurant_Sushi = Restaurant("Sushi Japex", "Sushi")

print(list_restaurants)
