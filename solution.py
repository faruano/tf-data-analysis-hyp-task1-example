import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 761791964 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    _, val = proportions_ztest(counts, nobs, alternative = 'larger')
    alpha = 0.02
    return val < alpha # Ваш ответ, True или False
