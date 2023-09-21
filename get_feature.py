import numpy as np

from identity_config import *
class Feature_time(object):
    def __init__(self, sequence_data):
        self.data = sequence_data

    def time_mean(self):
        return np.mean(self.data)

    def time_std(self):
        return np.std(self.data)

    def time_skew(self):
        from scipy.stats import skew
        return skew(self.data)

    def time_kurtosis(self):
        from scipy.stats import kurtosis
        return kurtosis(self.data)

    def time_all(self):
        feature_all = list()
        feature_all.append(self.time_mean())
        feature_all.append(self.time_std())
        feature_all.append(self.time_skew())
        feature_all.append(self.time_kurtosis())

        return feature_all
def get_feature_interpretable(arr):
    feature_list = list()
    # get time domain features
    feature_time = Feature_time(arr).time_all()
    feature_list.extend(feature_time)
    return feature_list
#输入是一个二维数组,样本长度及通道数
def get_feature_set1(IMU_array):
    feature=[]
    for i in range(6):
        feature[i*4:(i+1)*4]=get_feature_interpretable(IMU_array[:,i])
    return feature
def get_feature_set2(IMU_array):
    feature=np.zeros((IMU_array.shape[0],8))
    feature[:,0:6]=IMU_array
    for i in range(IMU_array.shape[0]):
        feature[i,6]=np.sqrt(IMU_array[i,0]**2+IMU_array[i,1]**2+IMU_array[i,2]**2)
        feature[i,7] = np.sqrt(IMU_array[i, 3] ** 2 + IMU_array[i, 4] ** 2 + IMU_array[i, 5] ** 2)
    feature=feature.reshape(-1)
    return feature.tolist()

