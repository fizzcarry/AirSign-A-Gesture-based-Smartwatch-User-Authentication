#数据集中的know_train是已经配对的样本，但一些论文中设计模型需要单个样本，因此先将配对样本转为未配对样本，方便后续论文使用
import os

import numpy as np

from identity_config import *
def get_one_from_pair():
    sample_dict={}
    base_path=r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\train_set"
    positive_sample_path = os.path.join(base_path, "positive_sample")
    json_files = glob.glob(os.path.join(positive_sample_path, '*.json'))
    for json_file in json_files:
        with open(json_file ,'r') as file:
                data_dict = json.load(file)
        if data_dict["series_information"][0] not in sample_dict:
            sample_dict[data_dict["series_information"][0]]={}
        if data_dict["series_information"][1] not in sample_dict[data_dict["series_information"][0]]:
            sample_dict[data_dict["series_information"][0]][data_dict["series_information"][1]] = np.array(data_dict["series1"])
        if data_dict["series_information"][2] not in sample_dict:
            sample_dict[data_dict["series_information"][2]]={}
        if data_dict["series_information"][3] not in sample_dict[data_dict["series_information"][2]]:
            sample_dict[data_dict["series_information"][2]][data_dict["series_information"][3]] = np.array(data_dict["series2"])
    # negative_sample_path = os.path.join(base_path, "negative_sample")
    # json_files = glob.glob(os.path.join(negative_sample_path, '*.json'))
    # for json_file in json_files:
    #     with open(json_file ,'r') as file:
    #             data_dict = json.load(file)
    #     if data_dict["series_information"][0] not in sample_dict:
    #         sample_dict[data_dict["series_information"][0]]={}
    #     if data_dict["series_information"][1] not in sample_dict[data_dict["series_information"][0]]:
    #         sample_dict[data_dict["series_information"][0]][data_dict["series_information"][1]] = np.array(data_dict["series1"])
    #     if data_dict["series_information"][2] not in sample_dict:
    #         sample_dict[data_dict["series_information"][2]]={}
    #     if data_dict["series_information"][3] not in sample_dict[data_dict["series_information"][2]]:
    #         sample_dict[data_dict["series_information"][2]][data_dict["series_information"][3]] = np.array(data_dict["series2"])
    save_path=r"E:\mydesk\data_warehouse\identity_data\experiment_data\unpaired_sample"
    for key1 in sample_dict.keys():
        os.makedirs(os.path.join(save_path,key1))
        for key2 in sample_dict[key1].keys():
            print(key1,key2)
            np.save(os.path.join(save_path,key1,key2+".npy"),sample_dict[key1][key2])
    return sample_dict
#输入是单样本数据地址，输出是一个字典，一个元素表示一个人的全部手势动作，用一个列表表示
def read_one_sample():
    base_path=r"E:\mydesk\data_warehouse\identity_data\experiment_data\unpaired_sample"
    one_sample_dict={}
    for i in range(10):
        file_path=os.path.join(base_path,"train"+str(i+1))
        temp_list=[]
        for j in range(20):
            file1_path=os.path.join(file_path,"motion"+str(j+1)+".npy")
            temp_list.append(np.load(file1_path).T)
        one_sample_dict["train"+str(i+1)]=temp_list
    return one_sample_dict


