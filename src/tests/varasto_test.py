""" Unittests module """
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """ Unit tests for Varasto """
    def setUp(self):
        self.varasto = Varasto(10)

    # Konstruktoritestit
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_tilavuus_lt_0(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_alkusaldo_lt_0(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_alkusaldo_ok(self):
        self.varasto = Varasto(10, 5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_konstruktori_alkusaldo_gt_tilavuus(self):
        self.varasto = Varasto(10, 11)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    # lisaa_varastoon testit

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaa_liian_vahan(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.saldo)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    # ota_varastosta testit

    def test_ottaminen_lt_0(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_gt_saldo(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # __str__

    def test_tostring(self):
        self.assertEqual("saldo = 0, vielä tilaa 10", str(self.varasto))
