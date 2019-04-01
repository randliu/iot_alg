from django.test import TestCase

from data_index import utils
import numpy as np
import pandas as pd

class Series_List_Test_Case(TestCase):
    def setUp(self):
        self.l = [-3, 2, 32, 2, 12, 30]
        self.s = pd.Series(self.l)

    def test_lst_to_series(self):
        m = utils.lst_to_series(self.l)
        self.assertTrue(isinstance(m, pd.Series))

    def test_lst_to_series(self):
        m = utils.series_to_list(self.s)
        self.assertTrue(isinstance(m, list))


