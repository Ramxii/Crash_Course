from population import location

def test_city_country():
    """Does single names work?"""
    testing_country = location('santiago', 'chile')
    assert testing_country == 'Santiago, Chile'
    return

def test_city_country_population():
    """Does the population argument work?"""
    testing_country = location('santiago', 'chile', 9000000)
    assert testing_country == 'Santiago, Chile - population 9000000'
    return

