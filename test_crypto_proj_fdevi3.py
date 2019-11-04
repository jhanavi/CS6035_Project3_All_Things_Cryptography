import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0xf21fc32801cfdc28c024c1721fb37ef0', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('pantera', password)
        self.assertEqual('ashlee', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0xaab246b68273411', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0x2c1cf5e26dea32c45251fe25d7e3ad22e1dc0b7da6c13c9ab1080cf339d174ddffa7baeb4c63165145fdd7d3f7be8d6f79fc0f52cfcb21192c841a21ca493fe6aab78cb5bd38081925b486fae8f60eb13267281d05e0c8fb95d94f1e507d9d345c8a53f4141328edb1a1e189e88fef25ab186a08302c5df2b487fe45e595ce99', d)
        self.assertEqual('23dff6702ba0c21a351ab923775a745aa74b5bb04e4eecd5d1ac4101', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('fdevi3, how\'s it going? What, that? It\'s just a flesh wound.', msg)


if __name__ == '__main__':
    unittest.main()