# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:13:44 2022

@author: Jack
"""

#import pandas as pd
#
#filePath = 'D:\workspace\exelFiles\메뉴별_매출현황(20220301)_20220321193029.xlsx'
#
##dataset2 = pd.read_excel(filePath)
#df = pd.read_excel(filePath, skiprows=[0,1], index_col = '메뉴코드')
#
#df_dic = df.to_dict('index')


import pandas as pd
import glob

file_format = ".xlsx"
file_path = "D:\workspace\exelFiles"
file_list = glob.glob(f"{file_path}/*{file_format}")


for i in range(len(file_list)):
    globals()['df_'+str(i)] = pd.read_excel(file_list[i], skiprows=[0,1], index_col = '메뉴코드')
    globals()['dic_'+str(i)] =globals()['df_'+str(i)].to_dict('index')
#for i in range(len(file_list)):
    
print(dic_0['C0000003']['매출건수'])
#file_df = pd.read_excel(file_list[0], skiprows=[0,1], index_col = '메뉴코드')
#df_dic = file_df.to_dict('index')
#df_dic_list[0] = df_dic

for i in range(len(file_list)):
    for key in globals()['dic_'+str(i)].keys():
        print(key)