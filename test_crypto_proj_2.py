import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0xe761e7031c2a0f5b136de8f3e89a8afc', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('amelia', password)
        self.assertEqual('carebear', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x803370c3c0ee601', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0xa425275dcda3a997aa6b6e528109c394a15042df9cbd70208a8f7e1bff888d1f4396a34aee5ebe6d27e443f12f1070338275758aa44b03738ff9f46862d109b917c8fd4261d099c83fb7db09e7dc480f8fa0af7be7bad8ddf47a46d35264758dfd1024145833bf9c382d9d1f17c09e8a9e0c2c55d044ac4f34b5ec3283759661', d)
        self.assertEqual('fcf192423940a40e182b2dfefd9c1d1cb37a00885d3c2a1e19147e63', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('I am the Lizard King, I can do anything!', msg)


if __name__ == '__main__':
    unittest.main()
