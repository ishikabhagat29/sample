#creating a dictionary
cities = ('Paris','Athens', 'Madrid')
continent = 'Europe'
my_dictionary = dict.fromkeys(cities,continent)
print(my_dictionary)

my_dictionary.pop("model")
print(my_dictionary)

