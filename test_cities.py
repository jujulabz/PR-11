def test_city_country():
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5000000'