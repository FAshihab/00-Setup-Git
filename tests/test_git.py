
import unittest

from today import *

class TestGit(unittest.TestCase):
    def test_hi_my_name_is(self):
        self.assertGreater(len(my_name_is()), 1)

    def test_my_age_is(self):
        self.assertGreater(len(my_age_is()), 1)
