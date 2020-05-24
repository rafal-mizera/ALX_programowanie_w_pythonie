from mathematica.geometry.figures import square_area, triangle_area



def test_square_area():
    assert square_area(5) == 25
    assert triangle_area(2,4) == 4