import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0x30a839645f3af5d227ad4479152545b7', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('212121', password)
        self.assertEqual('monster', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x9c656c9789fd95', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0x3984f016152fdfbbe2a34c2fd695c764a5488280ab7c0b286ae22c21564afaf8d0018bb040ea39d7292c4266913223a60d6e598e5e8b1f4a1f5155289831d5a02be8664ce4906d5572e122ef388a2cf35cab4ccde39ef0ad37aa135bce5796489af5676cddd7d6ac19741f9954e26a949f737aa94e7aecf6cf9e1e562c31b711', d)
        self.assertEqual('997942c76ce787a76f8722612a46d5a1abc0abe936109fc32a0d787b', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('psubrahmanyam3, Whazazup? Lovely day for a walk don\'t you think?', msg)


if __name__ == '__main__':
    unittest.main()
