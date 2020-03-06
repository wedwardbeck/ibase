from django.test import TestCase
from model_bakery import baker
from itembase.core.models import Vendor


class VendorTestModel(TestCase):
    """
    Class to test Vendor Model
    """

    def test_setUp(self):
        self.vendor = baker.make(Vendor)


vendors = baker.make(Vendor, _quantity=100000)
assert len(vendors) == 100000
