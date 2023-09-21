import pandas as pd

from identity_tools import *
from identity_config import *
from get_feature import *

from DTW_classification import *
from handle_data import *
feature_type=1
one_sample_dict=read_one_sample()

max_dist_dict=DTW_classification1_get_max_dist(feature_type=feature_type)

#计算TAR
test_base_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\unknown_categories"
test_path=os.path.join(test_base_path,"positive_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
TA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1=DTW_classification1(one_sample_dict,max_dist_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    pre2 = DTW_classification1(one_sample_dict, max_dist_dict, np.array(data_dict["series2"]).T, feature_type=feature_type)
    if pre1==pre2:
        TA_number+=1
    print(i+1, TA_number, pre1, pre2)
TAR=TA_number/len(json_files)

#计算FAR
test_path=os.path.join(test_base_path,"negative_sample")
json_files = glob.glob(os.path.join(test_path, '*.json'))
FA_number=0
for i,json_file in enumerate(json_files):
    with open(json_file, 'r') as file:
        data_dict = json.load(file)
    pre1=DTW_classification1(one_sample_dict,max_dist_dict,np.array(data_dict["series1"]).T,feature_type=feature_type)
    pre2 = DTW_classification1(one_sample_dict, max_dist_dict, np.array(data_dict["series2"]).T, feature_type=feature_type)
    if pre1!=pre2:
        FA_number+=1
    print(i + 1, FA_number, pre1, pre2)
FAR=FA_number/len(json_files)
print(TAR)
print(FAR)

