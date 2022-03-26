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


total_dic = {}
total_list = []

for i in range(len(file_list)):
    globals()['df_'+str(i)] = pd.read_excel(file_list[i], skiprows=[0,1], index_col = '메뉴코드')
    globals()['dic_'+str(i)] =globals()['df_'+str(i)].to_dict('index')
#for i in range(len(file_list)):
    
#print(dic_0['C0000003']['매출건수'])
#file_df = pd.read_excel(file_list[0], skiprows=[0,1], index_col = '메뉴코드')
#df_dic = file_df.to_dict('index')
#df_dic_list[0] = df_dic

for i in range(len(file_list)):
    temp_dic = globals()['dic_'+str(i)]
    for key in temp_dic.keys():
        if key in total_dic:
#            print("sum value")
            total_dic[key]['매출건수'] = total_dic[key]['매출건수'] + temp_dic[key]['매출건수']
            total_dic[key]['매출금액'] = total_dic[key]['매출금액'] + temp_dic[key]['매출금액']
            total_dic[key]['부가세'] = total_dic[key]['부가세'] + temp_dic[key]['부가세']
            total_dic[key]['순매출'] = total_dic[key]['순매출'] + temp_dic[key]['순매출']
            total_dic[key]['실매출'] = total_dic[key]['실매출'] + temp_dic[key]['실매출']
            total_dic[key]['판매건수'] = total_dic[key]['판매건수'] + temp_dic[key]['판매건수']
            total_dic[key]['판매수량'] = total_dic[key]['판매수량'] + temp_dic[key]['판매수량']
        else :
#            print("add dic")
            total_dic[key] = temp_dic[key]
            

total_df = pd.DataFrame(total_dic)
total_df.to_excel("output.xlsx")
