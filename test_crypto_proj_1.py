import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0x7c7b7bf5d91793041566747a01b0b3b7', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('silvia', password)
        self.assertEqual('melissa', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0xb702abf9fc41001', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0x178c7b170555657c35236e508a8f5c98ea7684d659d397a6a0221037b65f5365bb51e593a941b83befc3187e80ab8870f80c7b324989341cae005d46a890cd8648850f7dee2285d9fe14470abb913e85e6e4d6d267811ab43b7ff084ff3c09a213dc99e703e29b0337126b1dd017048e5fb32c77db5c1a1dc3987470a88782d1', d)
        self.assertEqual('b4834ed6948f6bd3a7de19f9d578480264020d562bb54a71914eb636', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('They are the egg men. I am the walrus. Goo goo g\'joob.', msg)


if __name__ == '__main__':
    unittest.main()
