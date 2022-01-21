import warnings

def coefs_flesch_kincaid_grade_level(adjusted, texttype):
    if adjusted == False:
        coef_list = [0.39, 11.8, -15.59]
    elif adjusted == True and texttype == 'story':
        coef_list = [0.13, 20.66, -22.86]
    elif adjusted == True and texttype == 'poetry':
        coef_list = [0.1058, -2.631, 5.341]
    elif adjusted == True and texttype == 'informational':
        coef_list = [0.07316, 10.93, -9.709]
    elif adjusted == True and texttype == 'drama':
        coef_list = [0.01456, -5.269, 17.9]
    else:
        coef_list = [0.13, 20.66, -22.86]
        warnings.warn(
        "TEXTREADER's MESSAGE-> wrong adjusted(boolean) and type(string) entered, returning to default settings(adjusted:True, type:'story')"
        )
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_fog_count(adjusted, texttype):
    if adjusted == False:
        coef_list = [0.4, 100, 0]
    elif adjusted == True and texttype == 'story':
        coef_list = [0.1403, 397.6, 0.5744]
    elif adjusted == True and texttype == 'poetry':
        coef_list = [0.09664, -40.81, 2.228]
    elif adjusted == True and texttype == 'informational':
        coef_list = [0.06411, 451.3, 2.996]
    elif adjusted == True and texttype == 'drama':
        coef_list = [0.0125, -794.9, 11.67]
    else:
        coef_list = [0.1403, 397.6, 0.5744]
        warnings.warn(
        "TEXTREADER's MESSAGE-> wrong adjusted(boolean) and type(string) entered, returning to default settings(adjusted:True, type:'story')"
        )
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_smog_index(adjusted, texttype):
    if adjusted == False:
        coef_list = [1.043, 30, 3.1291]
    elif adjusted == True and texttype == 'story':
        coef_list = [3.338, 6.868, 2.258]
    elif adjusted == True and texttype == 'poetry':
        coef_list = [0.6161, 0.4613, 3.921]
    elif adjusted == True and texttype == 'informational':
        coef_list = [5.632, 0.7288, 3.67]
    elif adjusted == True and texttype == 'drama':
        coef_list = [0.5099, 1.091, 10.94]
    else:
        coef_list = [3.338, 6.868, 2.258]
        warnings.warn(
        "TEXTREADER's MESSAGE-> wrong adjusted(boolean) and type(string) entered, returning to default settings(adjusted:True, type:'story')"
        )
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_coleman_liau_index(adjusted, texttype):
    if adjusted == False:
        coef_list = [0.0588, -0.296, -15.8]
    elif adjusted == True and texttype == 'story':
        coef_list = [0.04671, -0.467, -9.626]
    elif adjusted == True and texttype == 'poetry':
        coef_list = [0.002538, -0.3767, 5.263]
    elif adjusted == True and texttype == 'informational':
        coef_list = [0.00654, -0.8432, 9.942]
    elif adjusted == True and texttype == 'drama':
        coef_list = [-0.02271, -0.2083, 22.42]
    else:
        coef_list = [0.04671, -0.467, -9.626]
        warnings.warn(
        "TEXTREADER's MESSAGE-> wrong adjusted(boolean) and type(string) entered, returning to default settings(adjusted:True, type:'story')"
        )
    return coef_list[0],coef_list[1],coef_list[2]

def coefs_automated_readability_index(adjusted, texttype):
    if adjusted == False:
        coef_list = [4.71, 0.5, -21.43]
    elif adjusted == True and texttype == 'story':
        coef_list = [5.893, 0.1329, -20.43]
    elif adjusted == True and texttype == 'poetry':
        coef_list = [-0.003815, 0.09098, 2.046]
    elif adjusted == True and texttype == 'informational':
        coef_list = [2.723, 0.09428, -6.888]
    elif adjusted == True and texttype == 'drama':
        coef_list = [-1.659, 0.01462, 17.96]
    else:
        coef_list = [5.893, 0.1329, -20.43]
        warnings.warn(
        "TEXTREADER's MESSAGE-> wrong adjusted(boolean) and type(string) entered, returning to default settings(adjusted:True, type:'story')"
        )
    return coef_list[0],coef_list[1],coef_list[2]