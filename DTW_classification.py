import numpy as np

from identity_tools import *
from identity_config import *
from get_feature import *

def DTW_classification1_get_max_dist(feature_type=1):
    max_dist_dict = {}
    known_train_positive_path=r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\train_set\positive_sample"
    json_files = glob.glob(os.path.join(known_train_positive_path, '*.json'))
    for i,json_file in enumerate(json_files):
        with open(json_file, 'r') as file:
            data_dict = json.load(file)
        if data_dict["series_information"][0] not in max_dist_dict:
            max_dist_dict[data_dict["series_information"][0]] = 0
        if feature_type==1:
            temp_dict=fastdtw(get_feature_set1(np.array(data_dict["series1"]).T), get_feature_set1(np.array(data_dict["series2"]).T))[0]
        else:
            temp_dict=fastdtw(get_feature_set2(np.array(data_dict["series1"]).T), get_feature_set2(np.array(data_dict["series2"]).T))[0]
        if temp_dict>max_dist_dict[data_dict["series_information"][0]]:
            max_dist_dict[data_dict["series_information"][0]]=temp_dict
        print(i,data_dict["series_information"])
    return max_dist_dict
#测试样本小于最大距离比例最高就是那个
def DTW_classification1(one_sample_dict,max_dist_dict,sample_test,feature_type=1):
    max_rate=0
    pre_result=list(one_sample_dict.keys())[0]
    for key in one_sample_dict.keys():
        temp_n = len(one_sample_dict[key])
        temp_number=0
        for i in range(temp_n):
            if feature_type == 1:
                temp_dict = fastdtw(get_feature_set1(one_sample_dict[key][i]), get_feature_set1(sample_test))[0]
            else:
                temp_dict = fastdtw(get_feature_set2(one_sample_dict[key][i]), get_feature_set2(sample_test))[0]
            if temp_dict<max_dist_dict[key]:
                temp_number+=1
        if (temp_number/temp_n)>max_rate:
            max_rate=temp_number/temp_n
            pre_result=key
    return pre_result
def DTW_classification2_get_median(feature_type=1):
    median_feature_dict = {}#最小的号码1开始
    median_value_dict = {}
    temp_matrix_dict={}
    known_train_positive_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\train_set\positive_sample"
    json_files = glob.glob(os.path.join(known_train_positive_path, '*.json'))
    for i,json_file in enumerate(json_files):
        with open(json_file, 'r') as file:
            data_dict = json.load(file)
        if data_dict["series_information"][0] not in temp_matrix_dict:
            temp_n = 20
            temp_matrix_dict[data_dict["series_information"][0]]=np.zeros(((temp_n, temp_n)))
        number1=eval(data_dict["series_information"][1].replace("motion", ""))-1
        number2 = eval(data_dict["series_information"][3].replace("motion", "")) - 1
        print(i,data_dict["series_information"])
        if feature_type == 1:
            temp_matrix_dict[data_dict["series_information"][0]][number1][number2] = fastdtw(get_feature_set1(np.array(data_dict["series1"]).T), get_feature_set1(np.array(data_dict["series2"]).T))[0]
            temp_matrix_dict[data_dict["series_information"][0]][number2][number1] = fastdtw(get_feature_set1(np.array(data_dict["series1"]).T), get_feature_set1(np.array(data_dict["series2"]).T))[0]
        else:
            temp_matrix_dict[data_dict["series_information"][0]][number1][number2] = fastdtw(get_feature_set2(np.array(data_dict["series1"]).T), get_feature_set2(np.array(data_dict["series2"]).T))[0]
            temp_matrix_dict[data_dict["series_information"][0]][number2][number1] = fastdtw(get_feature_set2(np.array(data_dict["series1"]).T), get_feature_set2(np.array(data_dict["series2"]).T))[0]
    for key in temp_matrix_dict.keys():
        sum_array=np.zeros(20)
        for i in range(20):
            temp_number=0
            for j in range(20):
                if temp_matrix_dict[key][i][j]!=0:
                    sum_array[i]+=temp_matrix_dict[key][i][j]
                    temp_number+=1
            sum_array[i]/=temp_number
        median_value_dict[key] = float(np.min(sum_array))
        median_feature_dict[key] = int(np.argmin(sum_array))
    return median_feature_dict,median_value_dict
#测试样本小于最大距离比例最高就是那个
def DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,sample_test,feature_type=1):
    min_score=99999999
    pre_result = list(median_feature_dict.keys())[0]
    for key in median_feature_dict.keys():
        if feature_type == 1:
            temp_dict = fastdtw(get_feature_set1(one_sample_dict[key][median_feature_dict[key]]), get_feature_set1(sample_test))[0]
        else:
            temp_dict = fastdtw(get_feature_set2(one_sample_dict[key][median_feature_dict[key]]), get_feature_set2(sample_test))[0]

        temp_score=temp_dict/median_value_dict[key]
        if temp_score<min_score:
            min_score=temp_score
            pre_result=key
    return pre_result