import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-2)
        self.varasto3 = Varasto(10, -5)
        self.varasto4 = Varasto(10, 15)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisataan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_string(self):
        expected = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertEqual(str(self.varasto), expected)

    def test_otetaan_liikaa(self):
        alkuper_saldo = self.varasto.saldo
        otettu = self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(self.varasto.saldo, 0 and otettu, alkuper_saldo)

    def test_lisataan_negatiivinen_maara(self):
        varasto_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, varasto_saldo)

    def test_otetaan_negatiivinen_maara(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_negatiivinen_varasto(self):
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_alkusaldo_liian_suuri(self):
        self.assertAlmostEqual(self.varasto4.saldo, self.varasto4.tilavuus)

    

