import numpy as np
from scipy.stats import  skew
import pandas as pd

def hello_world():
    return "hello world!"

"""
均值
"""
def mean(data,sampling_rate=40000):
    assert(len(data)>0)
    n = len(data)
    m = np.mean(data)

    return m


"""
最大
"""
def max(data):

    assert (data is not None)

    n = len(data)
    #sampling_peroid = n/sampling_rate

    m = np.max(data)

    return m

"""
最小
"""
def min(data):
    n = len(data)
    #sampling_peroid = n/sampling_rate

    m = np.min(data)

    return m


"""
绝对平均值
"""
def abs_mean(data,sampling_rate=40000):
    n = len(data)
    m = np.mean(np.abs(data))

    return m


"""
根方根 RMS
"""
def root_mean_square(data,sampling_rate=40000):
    root_mean_square = np.sqrt(np.mean(data**2))
    return root_mean_square


"""
峭度
"""


def iot_kurtosis(data,sampling_rate=40000):
    Dx = np.mean((x-np.mean(x))**2)
    N = len(x)
    kurtosis = np.sum(((x-np.mean(x))/np.sqrt(Dx))**4)/N -3

    return kurtosis

"""
峰值
"""
def peak(x):
    p= np.max(np.abs(x))
    return p


"""
峰-峰值
"""
def peak_to_peak(x):
    pp = np.max(x)-np.min(x)

    return pp


"""
偏度
"""
def iot_skew(data):
    assert (data is not None)
    Dx = np.mean((x-np.mean(x))**2)
    N = len(x)
    skewness = np.sum(((x-np.mean(x))/np.sqrt(Dx))**3)/N
    return skewness



"""
脉冲因子
峰值与整流平均值的比值
"""
def pulse_factor(data):
    max_data = np.max(data)
    mean_data = np.mean(np.abs(data))
    pulse_factor = max_data / mean_data
    return pulse_factor



"""
峰值因子：
是信号峰值与有效值（RMS）的比值，代表的是峰值在波形中的极端程度
"""
def crest_factor(data):
    max_data = np.max(data)
    RMS_data = np.power(np.mean(data**2),0.5)
    crest_factor = max_data/RMS_data
    return crest_factor




"""
波形因子：
是有效值（RMS）与整流平均值的比值，用来判断损伤类型
"""
def waveform_factor(data):
    RMS_data = root_mean_square(data)
    mean_data = abs_mean(RMS_data)
    waveform_factor = RMS_data/mean_data
    return waveform_factor



"""
峰度：
样本值的峰度（四阶矩）
"""
def waveform_factor(data):
    RMS_data = np.power(np.mean(data**2),0.5)
    mean_data = np.mean(np.abs(data))
    waveform_factor = RMS_data/mean_data
    return waveform_factor



"""
汉宁窗
"""
def hanning(data):
    h_data = np.hanning(data)

    return h_data


"""
return dataFrame
X轴是HZ
Y轴是高度

"""
def fft(data,sampling_rate=4000):
    assert(len(data)>0)

    #做一次缺省的FFT变换
    fft_result = np.fft.fft(data)

    #先虚拟采样点数
    points = range(0,sampling_rate)
    n = len(data)

    #根据采样点数换算实际的采样频率矩阵
    frequency = np.arange(n / 2) / (n /sampling_rate)

    #根据采样点数换算采样幅度矩阵
    amp = abs(fft_result[range(int(n / 2))] / n)

    #生成（N*1的矩阵向量）
    #spectrum = pd.Series(amp)

    #这里却一个数据异常保护处理，需要补上
    #如果频率谱与幅度谱形状不一致的话，这里会报错
    freq = pd.Series(frequency)

    #两个（N*1）的向量合并成一个N*2的向量
    spectrum = pd.DataFrame()

    #列命名
    spectrum.insert(0,'AMP',amp )
    spectrum.insert(0, 'HZ',freq)

    return spectrum


"""
去除直流分量
return pd.Series
"""
def bonferroni(data):
    #assert isinstance(data, pd.Series)

    #去除误差基准向量长度N设为整个数据的长度
    m = np.mean(data)   #均值为直流分量

    data_edit = data -m

    return data_edit


"""
从加速度到速度
默认采样频率是1HZ
"""
def acc_to_v_with_bonferroni(acc_data,sr=1):
    assert(sr >0)
    acc_edit = bonferroni(acc_data)

    #采用系统默认积分即可
    v = acc_edit.cumsum()*1/sr

    return v


"""
从速度到位移
默认采样频率是1HZ

"""
def v_to_movement_with_bonferroni(v,sr=1):
    v_edit = bonferroni(v)
    movement = v_edit.cumsum()*1/sr

    return movement
