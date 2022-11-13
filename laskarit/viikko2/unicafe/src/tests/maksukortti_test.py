import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        kortti = Maksukortti(500)

        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldon_lataaminen_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_saldo_vahenee_oikein(self):
        kortti = Maksukortti(400)
        kortti.ota_rahaa(400)
        
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        kortti = Maksukortti(400)

        kortti.ota_rahaa(400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

        kortti.lataa_rahaa(300)

        kortti.ota_rahaa(400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")

        if kortti.saldo < 400:
            return False

        else:
            return True

    