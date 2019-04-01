import numpy as np
import pandas as pd

def lst_to_series(lst_data):

    assert isinstance(lst_data, list)
    s = pd.Series(lst_data)
    return s


def series_to_list(s):
    assert isinstance(s, pd.Series)
    l = s.tolist()
    assert isinstance(l, list)
    return l
