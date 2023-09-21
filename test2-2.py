import pandas as pd

from identity_tools import *
from identity_config import *
from get_feature import *

from DTW_classification import *
from handle_data import *
feature_type=2
one_sample_dict=read_one_sample()

median_feature_dict,median_value_dict=DTW_classification2_get_median(feature_type=feature_type)
intermediate_results_base_path=r"E:\mydesk\code\AirSign\intermediate_results"
intermediate_results_path1=os.path.join(intermediate_results_base_path,"median_feature_dict.json")
intermediate_results_path2=os.path.join(intermediate_results_base_path,"median_value_dict.json")
with open(intermediate_results_path1, 'w') as file:
    json.dump(median_feature_dict, file)
with open(intermediate_results_path2, 'w') as file:
    json.dump(median_value_dict, file)
with open(intermediate_results_path1, 'r') as file:
    median_feature_dict = json.load(file)
with open(intermediate_results_path2, 'r') as file:
    median_value_dict = json.load(file)

#单样本字典，减低复杂度
sample_one_pre_dict={}

#计算know_vaild的TAR
test_base_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\vaild_set"
test_path=os.path.join(test_base_path,"positive_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
TA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag=data_dict["series_information"][0]+data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag]==sample_one_pre_dict[pre2_flag]:
        TA_number+=1
    print(i+1, TA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
know_vaild_TAR=TA_number/len(json_files)
#计算FAR
test_path=os.path.join(test_base_path,"negative_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
FA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag = data_dict["series_information"][0] + data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag] != sample_one_pre_dict[pre2_flag]:
        FA_number+=1
    print(i+1, FA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
know_vaild_FAR=FA_number/len(json_files)


#计算known_test的TAR
test_base_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\test_set"
test_path=os.path.join(test_base_path,"positive_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
TA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag=data_dict["series_information"][0]+data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag]==sample_one_pre_dict[pre2_flag]:
        TA_number+=1
    print(i+1, TA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
known_test_TAR=TA_number/len(json_files)
#计算FAR
test_path=os.path.join(test_base_path,"negative_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
FA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag = data_dict["series_information"][0] + data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag] != sample_one_pre_dict[pre2_flag]:
        FA_number+=1
    print(i+1, FA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
known_test_FAR=FA_number/len(json_files)


#计算unknown_test的TAR
test_base_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\unknown_categories"
test_path=os.path.join(test_base_path,"positive_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
TA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag=data_dict["series_information"][0]+data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag]==sample_one_pre_dict[pre2_flag]:
        TA_number+=1
    print(i+1, TA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
unknown_test_TAR=TA_number/len(json_files)
#计算FAR
test_path=os.path.join(test_base_path,"negative_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
FA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1_flag = data_dict["series_information"][0] + data_dict["series_information"][1]
    pre2_flag = data_dict["series_information"][2] + data_dict["series_information"][3]
    if pre1_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre1_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    if pre2_flag not in sample_one_pre_dict:
        sample_one_pre_dict[pre2_flag] = DTW_classification2(one_sample_dict,median_feature_dict,median_value_dict,np.array(data_dict["series2"]).T,feature_type=feature_type)
    if sample_one_pre_dict[pre1_flag] != sample_one_pre_dict[pre2_flag]:
        FA_number+=1
    print(i+1, FA_number, sample_one_pre_dict[pre1_flag], sample_one_pre_dict[pre2_flag])
unknown_test_FAR=FA_number/len(json_files)

print(know_vaild_TAR)
print(know_vaild_FAR)
print(known_test_TAR)
print(known_test_FAR)
print(unknown_test_TAR)
print(unknown_test_FAR)
