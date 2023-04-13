import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 1266169265 # Ваш chat ID, не меняйте название переменной

def solution(NPV_control: list, NPV_test: list, alpha: float = 0.07) -> bool:
    t_stat, p_val = stats.ttest_ind(NPV_control, NPV_test, equal_var=False)
    if(p_val < alpha and t_stat > 0):
        return True
    else:
        return False


