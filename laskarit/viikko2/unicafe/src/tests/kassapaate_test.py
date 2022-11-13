import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(0)

    def test_luodun_kortin_saldo_on_oikea(self):
        
        self.assertEqual(self.kassa.kassassa_rahaa,100000 )
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateis_osto_toimii(self):

        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300),60)

        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500),100)

        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)

        #Epäonnistumiset

        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200),200)

        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)

        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300),300)

        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)

        
    def test_kortti_osto_toimii_oikein(self):
        self.kortti.lataa_rahaa(640)

        
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        
        self.assertEqual(self.kassa.edulliset, 1)

        self.assertEqual(self.kortti.saldo, 400)

        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

        self.assertEqual(self.kassa.maukkaat, 1)

        self.assertEqual(self.kortti.saldo, 0)

        #Epäonnistumiset

        self.kortti.lataa_rahaa(200)

        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)

        self.assertEqual(self.kortti.saldo, 200)

        self.assertEqual(self.kassa.edulliset, 1)

        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)

        self.assertEqual(self.kortti.saldo, 200)

        self.assertEqual(self.kassa.maukkaat, 1)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen(self):

        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)

        self.assertEqual(self.kortti.saldo, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

        #Negatiivisen summan lataaminen

        self.kassa.lataa_rahaa_kortille(self.kortti, -10000)

        self.assertEqual(self.kortti.saldo, 1000)

        self.assertEqual(self.kassa.kassassa_rahaa, 101000)




