def city_country(name, country):
    """Takes in name and country of a city"""
    city_info = f"{name.title()}, {country.title()}"
    return city_info

country = city_country('castries', 'st. lucia')
print(country)

country = city_country('kingstown', 'jamaica')
print(country)

country = city_country('london', 'england')
print(country)
