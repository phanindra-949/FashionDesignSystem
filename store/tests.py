import pytest
from django.test import TestCase
from store.models import *
class DesignerTestCase(TestCase):
    def setUp(self) -> None:
        Designer.objects.create(DesignerId=1,name="phani",contactnumber='7989332540',designeremailid='phanindramadala949@gmail.com',password='sai@31191')
        Designer.objects.create(DesignerId=2, name="jainendra", contactnumber='9848336247',
                                designeremailid='jainendrasai@gmail.com', password='fucker')
        Designer.objects.create(DesignerId=3,name="gupta",contactnumber='7989332540',designeremailid='phanindramadala949@gmail.com',password='password')

    def test_designers2(self):
        ID = Designer.objects.get(DesignerId=1)
        ID = str(ID)
        self.assertEqual(ID, 'Designer object (1)')
    def test_2_desginers2(self):
        ID = Designer.objects.get(DesignerId=2)
        ID = str(ID)
        self.assertEqual(ID, 'Designer object (2)')
    def test_3_desginers3(self):
        ID = Designer.objects.get(DesignerId=3)
        ID = str(ID)
        self.assertEqual(ID, 'Designer object (3)')
