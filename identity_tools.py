import numpy as np

from identity_config import *
def list_npy(file_path):
    # 使用glob模块匹配文件夹下的所有.npy文件
    npy_files = glob.glob(os.path.join(file_path, '*.npy'))
    result=[]
    # 打印所有找到的.npy文件
    for npy_file in npy_files:
        temp_array=(np.load(npy_file).T)[::down_sampling,:]
        result.append(temp_array)
    return result
def get_all_sample(base_path):
    # all_data=np.zeros((0,6))#标准化时使用
    sample_dict={}
    train_path=os.path.join(base_path,"train_data")
    test_path = os.path.join(base_path, "test_data")
    for i in range(train_number):
        file1_path =os.path.join(train_path, "people"+str(i+1))
        sample_dict["train" + str(i + 1)] = list_npy(file1_path)
        # (all_data = np.concatenate((all_data, temp_array), axis=0))
    for i in range(test_number):
        file1_path = os.path.join(test_path, "people" + str(i + 1))
        sample_dict["test" + str(i + 1)] = list_npy(file1_path)
        # (all_data = np.concatenate((all_data, temp_array), axis=0))
    # if standardization:
    #     standardization_mean=np.mean(all_data,axis=0)
    #     standardization_std = np.std(all_data, axis=0)
    #     for key in sample_dict.keys():
    #         sample_dict[key]=((sample_dict[key]-standardization_mean)/standardization_std).reshape(-1,sample_len,6)
    # else:
    #     for key in sample_dict.items():
    #         sample_dict[key]=sample_dict[key].reshape(-1,sample_len,6)
    return sample_dict

file_path=r"E:\mydesk\data_warehouse\identity_data"
get_all_sample(file_path)

