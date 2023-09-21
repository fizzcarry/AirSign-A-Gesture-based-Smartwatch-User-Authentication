import numpy as np
import os
import scipy.stats

from numpy import unique

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import numpy as np
import scipy.stats
import os
import glob
from fastdtw import fastdtw


train_number=10
test_number=14
feature_setting1_len=4

down_sampling=5#论文中100HZ，我们手机500HZ，降采样5倍