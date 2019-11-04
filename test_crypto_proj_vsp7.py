import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0xdec365f746455135daab34efd69081f3', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('brittany', password)
        self.assertEqual('david1', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0xa85e1a401b53b81', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0x37880bf5a8b35395441fda01cf8d34a60d3203b69f87a33f51415c1daaaf1b849b3f5f321c782c6e8f2d7d6d6b7da44f104b952dda22cfc431ee4533b780865418bb202f5074b8dd7ec384df2caa08d2ad13cae74973acaf60fc9179e145ed6ea54a9ad86c732630e23b629f243681f261ac5b197abcba37340d193eb69d3af1', d)
        self.assertEqual('ff20ad3738c570533558c0b07bf9146af522e2399f2f64eb79c4a07f', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('vsp7, they somehow managed to get every creep and freak in the universe onto this one plane.', msg)


if __name__ == '__main__':
    unittest.main()
