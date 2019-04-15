from django.test import TestCase
import sys
import os
import csv
import numpy as np
import pandas as pd
from scipy.stats import kurtosis

# Create your tests here.
from data_index import index
from data_index.tests import alter_algorithm

import logging


cur_path = os.path.abspath(os.path.dirname(__file__))

acc_path = os.path.join(cur_path, "..", "..", "notebook", "acc.csv")

logging.getLogger("test").info("start test")

print("=="*65)
ds = "Using data source:%s"%str(acc_path)
sp = " "*int(((130-len(ds))/2)-1)
print("*%s%s%s*"%(sp, ds, sp))
print("=="*65)

acc = pd.read_csv(acc_path)


def get_acc_data():
    global acc

    return acc



def get_data_X():
    acc = get_acc_data()
    return acc['X']


def get_data_Y():
    acc = get_acc_data()
    return acc['Y']

def get_data_Z():
    acc = get_acc_data()
    return acc['Z']


class HelloWorldTestCase(TestCase):
    def setUp(self):
        #print("hello world!")
        pass

    def test_animals_can_speak(self):
        hw = index.hello_world()
        self.assertEqual(hw, 'hello world!')

    def tearDown(self):
        pass



class SimpleTest_Case(TestCase):
    def setUp(self):
        self.s = [-3, 2, 32, 2, 12, 30]

    def test_x_mean(self):
        x = get_data_X()
        m_x =index.mean(x)
        self.assertEqual(m_x,-0.39695625000000007)

    def test_y_mean(self):
        y = get_data_Y()
        m_y =np.mean(y)
        self.assertEqual(m_y,-0.033256249999999994)

    def test_z_mean(self):
        z = get_data_Z()
        m_z =np.mean(z)
        self.assertEqual(m_z,9.739487500000001)

    def test_s_mean(self):

        m_z =np.mean(self.s)
        self.assertEqual(m_z,12.5)

    def test_max(self):
        self.assertEqual(index.max(self.s),32)

    def test_min(self):
        self.assertEqual(index.min(self.s),-3)

    def tearDown(self):
        pass



class Average_Case(TestCase):
    def setUp(self):
        #self.x = get_data_X()
        pass


    def test_x_mean(self):
        #logging.getLogger("test").critical("bbssfda ")
        #logging.getLogger("test").info("fdadaf")
        #print("fuck")

        x = get_data_X()
        m_x =index.abs_mean(x)
        self.assertTrue(m_x > 0)


    def tearDown(self):
        pass



class kurtosisTest(TestCase):
    def test_x_kurtosis(self):
        kurtosis_scipy = kurtosis(get_data_X())
        kurtosis_index = alter_algorithm.kurtosis(get_data_X())
        self.assertEqual(kurtosis_scipy,kurtosis_index)


class peak_relative_Test(TestCase):

    def setUp(self):
        self.s=[-3,2,32,2,12,30]
        pass

    def test_peak_to_peak(self):
        pp = index.peak_to_peak(self.s)
        self.assertEqual(pp,35)

    def test_pp(self):
        p = index.peak(self.s)
        self.assertEqual(p, 32)


class IntegralTest(TestCase):

    def setUp(self):
        self.s=[-3,2,2,7,2,12,-4]
        #self.sum = np.sum(self.s)

    def test_acc_to_v_with_bonferroni(self):
        sum = np.sum(self.s)

        sum2 = np.cumsum(pd.Series(self.s))
        #print(sum2)
        self.assertEqual(sum,sum2[len(self.s)-1])


    def test_acc_to_v_with_bonferroni_with_sr(self):
        sr=4000
        sum = np.sum(self.s)/sr

        sum2 = np.cumsum(pd.Series(self.s))
        #print(sum2)
        self.assertEqual(sum,18/sr)

    def test_acc_to_v_with_bonferroni2(self):
        sum = np.sum(self.s)

        sum2 = np.cumsum(pd.Series(self.s))
        #print(sum2)
        self.assertEqual(sum,sum2[len(self.s)-1])

    def test_y_mean(self):
        y = get_data_Y()
        m_y =np.mean(y)
        self.assertEqual(m_y,-0.033256249999999994)

    def test_y_mean2(self):
        y = get_data_Y()
        m_y =np.mean(y)
        self.assertTrue(m_y+0.033256249999999994>=0)

    def test_acc_to_v_with_bonferroni3(self):
        sum = np.sum(self.s)
        self.assertTrue(sum>0)
