import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    actual = getDataPoint(quotes[0])
    expected = (
      quotes[0]["stock"],
      quotes[0]["top_bid"]["price"],
      quotes[0]["top_ask"]["price"],
      (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2
    )
    self.assertEqual(actual, expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(price, (quotes[0]["top_bid"]["price"] + quotes[0]["top_ask"]["price"]) / 2)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    priceABC = 1; priceDEF = 2
    ratio = getRatio(priceABC, priceDEF)
    self.assertEqual(ratio, priceABC / priceDEF)

  def test_getRatio_zeroDivisor(self):
    priceABC = 1; priceDEF = 0
    self.assertIsNone(getRatio(priceABC, priceDEF))

  def test_getRatio_zeroDividend(self):
    priceABC = 0; priceDEF = 1
    self.assertIsNotNone(getRatio(priceABC, priceDEF))



if __name__ == '__main__':
    unittest.main()
