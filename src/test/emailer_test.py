import unittest

from emailer import get_emails


class TestEmailer(unittest.TestCase):
    def test_get_emails(self):
        emails = get_emails()
        self.assertEqual(2, len(emails))

        keys = emails.keys()
        self.assertTrue("test1@gmail.com" in keys)
        self.assertEqual(emails["test1@gmail.com"], "Old Test")

        self.assertTrue("test2@gmail.com" in keys)
        self.assertEqual(emails["test2@gmail.com"], "New Test")


if __name__ == '__main__':
    unittest.main()
