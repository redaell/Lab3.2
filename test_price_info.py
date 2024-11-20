import price_info as pi

def test_total_cost_shipping():
    expected = 46.75
    result = pi.total_cost_shopping()
    assert(expected==result)

def test_cost_of_fruit():
    fruit = "apple"
    quantity = 5
    expected = 6
    result = pi.cost_of_fruits('apple', quantity)
    assert(expected==result)