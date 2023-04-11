import pandas as pd
import numpy as np
import math
from scipy import stats as st
chat_id = 761791964 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.02
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)   
    z = (p1 - p2) / math.sqrt(p * (1 - p) * (1/x_cnt + 1/y_cnt))
    distr = st.norm(0, 1) 
    p_value = (1 - distr.cdf(abs(z))) * 2
    if (p_value < alpha):
      return True
    else: 
      return False
