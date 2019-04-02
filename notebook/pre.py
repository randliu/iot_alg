import os
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

def show(ori_func, ft, sampling_period = 5): 
    
    n = len(ori_func) 
    interval = sampling_period / n 
    # 绘制原始函数
    plt.subplot(2, 1, 1) 
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black') 
    plt.xlabel('Time'), plt.ylabel('Amplitude') 
    # 绘制变换后的函数
    plt.subplot(2,1,2) 
    frequency = np.arange(n / 2) / (n * interval) 
    nfft = abs(ft[range(int(n / 2))] / n ) 
    plt.plot(frequency, nfft, 'red') 
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum') 
    plt.show()
    
    
def load_cwru(name):

    cur_file = os.path.abspath(__file__)
    cur_dir = os.path.dirname(cur_file)
    parent_path= os.path.dirname(cur_dir)
    data_dir = os.path.join(parent_path , "bearing_data","cwru","Datafiles/")
   
    data_file = os.path.join(data_dir,name)
    print("Loading mat file:%s"%data_file)

    data = sio.loadmat(data_file)
    return data
