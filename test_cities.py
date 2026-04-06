from city_functions import city_country

def test_city_country():
    """Test basic city, country format."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'