import warnings

def coefs_flesch_kincaid_grade_level(adjusted):
    if adjusted == False:
        coef_list = [0.39, 11.8, -15.59]
    else:
        coef_list = [0.1014, 20.89, -21.94]
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_fog_index(adjusted):
    if adjusted == False:
        coef_list = [0.4, 100, 0]
    else:
        coef_list = [0.1229, 415.7, 1.866]
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_smog_index(adjusted):
    if adjusted == False:
        coef_list = [1.043, 30, 3.129]
    else:
        coef_list = [2.694, 8.815, 3.367]
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_coleman_liau_index(adjusted):
    if adjusted == False:
        coef_list = [0.0588, -0.296, -15.8]
    else:
        coef_list = [0.03993, -0.4976, -5.747]
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_automated_readability_index(adjusted):
    if adjusted == False:
        coef_list = [4.71, 0.5, -21.43]
    else:
        coef_list = [6.000, 0.1035, -19.61]
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_common_readability_formula():
    coef_list = [0.04876, -0.1145, 0.3091, 0.1866, 0.2645, 1.1017, -4.125]
    return coef_list[0],coef_list[1],coef_list[2],coef_list[3],coef_list[4],coef_list[5],coef_list[6]