AirSign: A Gesture-based Smartwatch User Authentication
训练数据为known_train_positive_path=r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\train_set\positive_sample"
测试数据包括三个，地址为test_base_path = r"E:\mydesk\data_warehouse\identity_data\experiment_data\known_categories\vaild_set"
每个样例（正例或负例）的文件格式为json格式，用python读取后为一个字典，字典内有2个元素，表示配对的两个时间序列。
第一个元素的键为“series1”，值为一个二维列表，建议转换为一个二维array，大小为6*N，6表示6轴IMU信号，N表示时间序列的长度。
第二个元素类似，键为“series2”，值为一个二维列表，建议转换为一个二维array，大小为6*M。
采样频率为100HZ
