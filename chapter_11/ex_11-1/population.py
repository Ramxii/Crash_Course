def location(city, country, population=0):
    """Return a single string of the form City, Country"""
    long_version = f"{city.title()}, {country.title()} - population {str(population)}"
    short_version = f"{city.title()}, {country.title()}"
    if population:
        return long_version
    else:
        return short_version


