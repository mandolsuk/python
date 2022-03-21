# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:13:44 2022

@author: Jack
"""

import pandas as pd

filePath = 'D:\workspace\exelFiles\메뉴별_매출현황(20220301)_20220321193029.xlsx'

#dataset2 = pd.read_excel(filePath)
df = pd.read_excel(filePath, skiprows=[0,1], index_col = '메뉴코드')

df_dic = df.to_dict('index')