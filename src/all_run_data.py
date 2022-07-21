import pandas as pd
import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import codecs
import os
from src import make_d_list
from src import make_send_csv
from src import Open_save_file

def all_run_spd(sent_data,master_data_path,Export_folder):

    def Transmission_master_data_combining():
            #Combine 'use_signature' and 'item_code' of sent data
            dfpp = sent_data
            dfpp["Department_Item"] = dfpp['use_signature'].str.cat(dfpp['item_code'].astype(str),sep='_')       
            dfpp_m_send = dfpp
            dfpp_m_send2 = dfpp_m_send.drop_duplicates()
            #Combines 'Department' and 'item_code' of the master data
            with codecs.open(master_data_path, "r", "Shift-JIS", "ignore") as file:
                masuta_p = pd.read_table(file, delimiter=",")
            masuta_df = masuta_p
            masuta_df["Department_Item"]=masuta_df['Department_CD'].str.cat(masuta_df['item_code'].astype(str),sep='_')
            masuta_p__m_masuta2= masuta_df
            #Create merged data masuta_send_m
            masuta_p_d_t = masuta_p__m_masuta2.drop_duplicates(subset="Department_Item",keep='last')
            masuta_p_d_t.to_csv(Export_folder+"/masuta_p_d_t.csv", encoding = 'shift-jis')
            masuta_send_m = pd.merge(dfpp_m_send,masuta_p_d_t,on="Department_Item")
            masuta_send_m.rename(columns={'Date_x':"Date"}, inplace=True)
            return masuta_send_m,masuta_p_d_t

    masuta_send_m,masuta_p_d_t=Transmission_master_data_combining()
    
    #List all Departments
    df_send_bese = masuta_send_m
    send_dy_p = df_send_bese['Department'].values
    send_dy1 = send_dy_p.tolist()
    send_dy_department = list(dict.fromkeys(send_dy1))
    numberlis_pre = (len(send_dy_department))
    range_department = range(numberlis_pre)
    
    #Create Department_name using function
    Department_name = send_dy_department[0]
    make_send_csv.make_FM_data_send(sent_data,master_data_path,Export_folder,Department_name,masuta_p_d_t,masuta_send_m)
    
    for i in range_department:
        print(i)
        print(str(send_dy_department[i]))
        Department_name = str(send_dy_department[i])
        make_send_csv.make_FM_data_send(sent_data,master_data_path,Export_folder,Department_name,masuta_p_d_t,masuta_send_m)
        
    Open_save_file.save_f(Export_folder,send_dy_department,master_data_path)


if __name__ == '__main__':
    main()
