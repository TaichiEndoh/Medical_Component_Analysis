import pandas as pd
import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import codecs
import os

def Transmission_master_data_combining():
    #Combines 'use_signature' and 'item_code' of sent data
    dfpp = sent_data
    dfpp["Department_Item"] = dfpp['use_signature'].str.cat(dfpp['item_code'].astype(str),sep='_')       
    dfpp_m_send = dfpp
    dfpp_m_send2 = dfpp_m_send.drop_duplicates()
    #Combines 'Department' and 'item_code' of the master data
    with codecs.open(master_data_path, "r", "Shift-JIS", "ignore") as file:
        masuta_p = pd.read_table(file, delimiter=",")
    masuta_df = masuta_p
    masuta_df["Department_Item"]=masuta_df['Department'].str.cat(masuta_df['item_code'].astype(str),sep='_')
    masuta_p__m_masuta2= masuta_df
    #Create merged data masuta_send_m
    masuta_p_d_t = masuta_p__m_masuta2.drop_duplicates(subset="Department_Item",keep='last')
    masuta_p_d_t.to_csv(Export_folder+"/masuta_p_d_t.csv", encoding = 'shift-jis')
    masuta_send_m = pd.merge(dfpp_m_send,masuta_p_d_t,on="Department_Item")
    masuta_send_m.rename(columns={'Date_x':"Date"}, inplace=True)
    
    return masuta_send_m,masuta_p_d_t