import pandas as pd
import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import codecs
import os

def save_f(Export_folder,send_dy_department,master_data_path):

    product_name = send_dy_department[0]
    with codecs.open(Export_folder+"send_data"+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
            df_fm_masuta = pd.read_table(file, delimiter=",")
    df_start = df_fm_masuta

    def concat_department_masuta(i):
        Department_name = str(send_dy_department[i])
        product_name = Department_name
        with codecs.open(Export_folder+"send_data"+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
                df_fm_masuta = pd.read_table(file, delimiter=",")
        pan_masuta = pd.concat([df_fm_masuta, df_start])
        return pan_masuta

    df_start2 = concat_department_masuta(1)
    print(df_start2)

    def concat_department_masuta_w(i,df_wont_m):
        Department_name = str(send_dy_department[i])
        product_name = Department_name
        with codecs.open(Export_folder+"send_data"+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
                df_fm_masuta = pd.read_table(file, delimiter=",")
        pan_masuta = pd.concat([df_fm_masuta, df_wont_m])
        return pan_masuta

    df_start3 = concat_department_masuta_w(2,df_start2)
    df_start4 = concat_department_masuta_w(3,df_start3)
    df_start5 = concat_department_masuta_w(4,df_start4)
    df_start6 = concat_department_masuta_w(5,df_start5)
    df_start7 = concat_department_masuta_w(6,df_start6)
    df_start8 = concat_department_masuta_w(7,df_start7)
    df_start9 = concat_department_masuta_w(8,df_start8)
    df_start10 = concat_department_masuta_w(9,df_start9)
    df_start11= concat_department_masuta_w(10,df_start10)
    df_start12 = concat_department_masuta_w(11,df_start11)
    df_start13 = concat_department_masuta_w(12,df_start12)
    df_start14 = concat_department_masuta_w(13,df_start13)
    df_start15 = concat_department_masuta_w(14,df_start14)
    df_start16 = concat_department_masuta_w(15,df_start15)
    df_start17 = concat_department_masuta_w(16,df_start16)
    df_start18 = concat_department_masuta_w(17,df_start17)
    df_start19 = concat_department_masuta_w(18,df_start18)
    df_start20 = concat_department_masuta_w(19,df_start19)
    df_start21= concat_department_masuta_w(20,df_start20)
    df_start22 = concat_department_masuta_w(21,df_start21)
    df_start23 = concat_department_masuta_w(22,df_start22)
    df_start24 = concat_department_masuta_w(23,df_start23)
    df_start25 = concat_department_masuta_w(24,df_start24)
    df_start26 = concat_department_masuta_w(25,df_start25)
    df_start27 = concat_department_masuta_w(26,df_start26)
    df_start28 = concat_department_masuta_w(27,df_start27)
    df_start29 = concat_department_masuta_w(28,df_start28)
    df_start30 = concat_department_masuta_w(29,df_start29)
    df_start31= concat_department_masuta_w(30,df_start30)
    df_start32 = concat_department_masuta_w(31,df_start31)


    df_send_data_total = df_start32.drop_duplicates()
    df_send_data_total1=df_send_data_total.drop('Department_Item', axis=1)
    df_send_data_total1.to_csv(Export_folder+"\df_send_data_total.csv", encoding = 'shift-jis')

    Department_name = str(send_dy_department[0])
    product_name = Department_name
    with codecs.open(Export_folder+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
            df_fm_masuta = pd.read_table(file, delimiter=",")
    df_start = df_fm_masuta

    def concat_department_masuta(i):
        Department_name = str(send_dy_department[i])
        product_name = Department_name
        with codecs.open(Export_folder+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
                df_fm_masuta = pd.read_table(file, delimiter=",")
        pan_masuta = pd.concat([df_fm_masuta, df_start])
        return pan_masuta

    df_start2 = concat_department_masuta(1)
    #print(df_start2)
    def concat_department_masuta_w(i,df_wont_m):
        Department_name = str(send_dy_department[i])
        product_name = Department_name
        with codecs.open(Export_folder+str(product_name)+'.csv', "r", "Shift-JIS", "ignore") as file:
                df_fm_masuta = pd.read_table(file, delimiter=",")
        pan_masuta = pd.concat([df_fm_masuta, df_wont_m])
        return pan_masuta
    df_start3 = concat_department_masuta_w(2,df_start2)
    #print(df_start3)

    df_start4 = concat_department_masuta_w(3,df_start3)
    df_start5 = concat_department_masuta_w(4,df_start4)
    df_start6 = concat_department_masuta_w(5,df_start5)
    df_start7 = concat_department_masuta_w(6,df_start6)
    df_start8 = concat_department_masuta_w(7,df_start7)
    df_start9 = concat_department_masuta_w(8,df_start8)
    df_start10 = concat_department_masuta_w(9,df_start9)
    df_start11= concat_department_masuta_w(10,df_start10)
    df_start12 = concat_department_masuta_w(11,df_start11)
    df_start13 = concat_department_masuta_w(12,df_start12)
    df_start14 = concat_department_masuta_w(13,df_start13)
    df_start15 = concat_department_masuta_w(14,df_start14)
    df_start16 = concat_department_masuta_w(15,df_start15)
    df_start17 = concat_department_masuta_w(16,df_start16)
    df_start18 = concat_department_masuta_w(17,df_start17)
    df_start19 = concat_department_masuta_w(18,df_start18)
    df_start20 = concat_department_masuta_w(19,df_start19)
    df_start21= concat_department_masuta_w(20,df_start20)
    df_start22 = concat_department_masuta_w(21,df_start21)
    df_start23 = concat_department_masuta_w(22,df_start22)
    df_start24 = concat_department_masuta_w(23,df_start23)
    df_start25 = concat_department_masuta_w(24,df_start24)
    df_start26 = concat_department_masuta_w(25,df_start25)
    df_start27 = concat_department_masuta_w(26,df_start26)
    df_start28 = concat_department_masuta_w(27,df_start27)
    df_start29 = concat_department_masuta_w(28,df_start28)
    df_start30 = concat_department_masuta_w(29,df_start29)
    df_start31 = concat_department_masuta_w(30,df_start30)
    df_start32 = concat_department_masuta_w(31,df_start31)

    df_masuta_data_total = df_start32.drop('Department_Item', axis=1)
    df_masuta_data_total.to_csv(Export_folder+"\df_masuta_data_total.csv", encoding = 'shift-jis')


if __name__ == '__main__':
    main()