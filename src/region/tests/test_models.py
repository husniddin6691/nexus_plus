from django.test import TestCase
from region.models import Region

class RegionModelTest(TestCase):
    def test_create_region(self):
        region = Region.objects.create(name='Tashkent', sorting=1)

        self.assertEqual(region.name, 'Tashkent')
        self.assertEqual(region.sorting, 1)

    def test_str_method(self):
        region = Region.objects.create(name='Samarkand', sorting=2)
        self.assertEqual(str(region), 'Samarkand')

    def test_sorting_unique_constraint(self):
        Region.objects.create(name='Bukhara', sorting=3)
        with self.assertRaises(Exception):
            Region.objects.create(name='Andijan', sorting=3)
