import numpy as np
from scipy.stats import kurtosis, skew
import pandas as pd

def hello_world():
    return "hello world!"

"""
均值
"""
def mean(data,sampling_rate=40000):
    n = len(data)
    m = np.mean(data)

    return m


"""
最大
"""
def max(data):
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
    k= kurtosis(data)
    return k


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
    sk = skew(data)
    return sk



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
    #RMS_data = np.power(np.mean(data**2),0.5)
    RMS_data = root_mean_square(data)
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
    k = data.kurt()

    return k


"""
汉宁窗
"""
def hanning(data):
    h_data = np.hanning(data)

    return h_data


"""
fft
FFT结果任意一点的频率为：假设信号采样频率为fs，
从采样定理可以知道，信号抽样后，抽样信号的频谱是周期谱，
其频谱的周期是抽样频率fs，因此，对信号做FFT时，无论你取多少点，
其分析的频率范围就是0~fs，所以，如果你做N点的FFT（其实是离散傅里叶变换），
则，FFT结果的两点之间的频率间隔是fs/N，这样，任一点k（k=0~N-1)代表的频率就是k*fs/N。
另外，这N个点的FFT值是以N/2为对称的，所以，一般真正用到的只有N/2个点。N点取的大只说明谱线密一些而已，
注意：采样定理非常重要啊！

作者：李泽光
链接：https://www.zhihu.com/question/27452867/answer/84237312
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

return dataFrame
X轴是HZ
Y轴是高度

"""
def fft(data,sampling_rate=4000):
    fft_result = np.fft.fft(data)
    points = range(0,sampling_rate)
    n = len(data)
    #frequency = np.arange(n / 2) / (n * interval)
    frequency = np.arange(n / 2) / (n /sampling_rate)

    amp = abs(fft_result[range(int(n / 2))] / n)

    #spectrum = pd.Series(amp)
    freq = pd.Series(frequency)

    spectrum = pd.DataFrame()
    spectrum.insert(0,'AMP',amp )
    spectrum.insert(0, 'HZ',freq)

    return spectrum






"""
去除直流分量
return pd.Series
"""
def bonferroni(data):
    #assert isinstance(data, pd.Series)
    m = np.mean(data)   #均值为直流分量

    data_edit = data -m

    return data_edit


"""
从加速度到速度
默认采样频率是1HZ
"""
def acc_to_v_with_bonferroni(acc_data,sr=1):
    acc_edit = bonferroni(acc_data)
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
