import unittest

from src.Lamp import Object, Lamp, Powder


class TestLamp(unittest.TestCase):
    def test_fill_should_fill_with_one_object(self):
        # GIVEN
        precious_object = Object(name='gem', count=1, weight=3, price=50)
        lamp = Lamp(100)

        # WHEN
        lamp.fill(objects=[precious_object], powders=[])

        # THEN
        self.assertEqual(lamp.powders, [])
        self.assertEqual(lamp.objects, [precious_object])

    def test_fill_should_fill_with_one_powder(self):
        # GIVEN
        powder = Powder(name='gold powder', quantity=8, price_per_gram=40)
        lamp = Lamp(100)

        # WHEN
        lamp.fill(objects=[], powders=[powder])

        # THEN
        self.assertEqual(lamp.powders, [powder])
        self.assertEqual(lamp.objects, [])

    def test_fill_should_not_take_everything(self):
        # GIVEN
        objects = [Object(name='gem', count=12, weight=3, price=12),
                   Object(name='gold piece', count=4503, weight=2, price=5)]
        powders = [Powder(name='gold powder', quantity=8, price_per_gram=40),
                   Powder(name='spice', quantity=50, price_per_gram=3)]
        lamp = Lamp(100)

        # WHEN
        lamp.fill(objects=objects, powders=powders)

        # THEN
        self.assertTrue(Object(name='gem', count=12, weight=3, price=12) in lamp.objects)
        self.assertTrue(Object(name='gold piece', count=3, weight=2, price=5) in lamp.objects)
        self.assertTrue(Powder(name='gold powder', quantity=8, price_per_gram=40) in lamp.powders)
        self.assertTrue(Powder(name='spice', quantity=50, price_per_gram=3) in lamp.powders)

    def test_fill_should_not_simply_take_biggest_first(self):
        # GIVEN
        objects = [Object(name='gem', count=1, weight=3, price=50)]
        powders = [Powder(name='gold powder', quantity=3, price_per_gram=20)]
        lamp = Lamp(4)

        # WHEN
        lamp.fill(objects=objects, powders=powders)

        # THEN
        self.assertTrue(Object(name='gem', count=12, weight=3, price=12) in lamp.objects)
        self.assertTrue(Powder(name='gold powder', quantity=1, price_per_gram=20) in lamp.powders)
