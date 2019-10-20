from unittest import TestCase
import afm


class TestAfm(TestCase):
    def test_afm_invalid1(self):
        self.assertEqual(False, afm.is_afm(1))

    def test_afm_invalid2(self):
        self.assertEqual(False, afm.is_afm(int('012312312')))

    def test_afm_invalid_0(self):
        self.assertEqual(False, afm.is_afm('012312310'))

    def test_afm_invalid_1(self):
        self.assertEqual(False, afm.is_afm('012312311'))

    def test_afm_invalid_3(self):
        self.assertEqual(False, afm.is_afm('012312313'))

    def test_afm_invalid_4(self):
        self.assertEqual(False, afm.is_afm('012312314'))

    def test_afm_invalid_5(self):
        self.assertEqual(False, afm.is_afm('0123123145'))

    def test_afm_invalid_6(self):
        self.assertEqual(False, afm.is_afm('012312316'))

    def test_afm_invalid_7(self):
        self.assertEqual(False, afm.is_afm('012312317'))

    def test_afm_invalid_8(self):
        self.assertEqual(False, afm.is_afm('012312318'))

    def test_afm_invalid_9(self):
        self.assertEqual(False, afm.is_afm('012312319'))

    def test_afm_valid1(self):
        self.assertEqual(True, afm.is_afm('012312312'))
