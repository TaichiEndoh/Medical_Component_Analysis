import pandas as pd
import itertools
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import codecs
import os

from src import make_d_list


def make_FM_data_send(sent_data,master_data_path,Export_folder,Department_name,masuta_p_d_t,masuta_send_m):
    
    #Master data creation divided into departments　
    #multi-indexed masuta_send_m_3　
    #Execute pandas☛Department_set for the first target department taken from masuta_send_m_3
    def Per_Department_df(masuta_p_d_t):
        masuta_send_m_2 = masuta_p_d_t.set_index(["Department_code",'Department'])
        masuta_send_m_3 = masuta_send_m_2.xs(Department_name, level=1)
        df_d = masuta_send_m
        df_1=df_d.reset_index()
        df_2 = df_1.set_index(["Department_code",'use_signature'])

        #Department_name department is set here↓
        Department_set = df_2.xs(Department_name, level=1)
        send_dt_t = Department_set.groupby(['Date','Standards_Capacities','goods']).count()
        send_dt_t1 =send_dt_t
        send_dt_d2 = Department_set.groupby(['Date','Department_Item']).count()
        return masuta_send_m_3,Department_set

    masuta_send_m_3,Department_set = Per_Department_df(masuta_p_d_t)

    #Function to create all combinations of department, item number and Date for pandas☛Department_set separated by department 
    def make_itertools_department(send_dt):
        send_dy_p = send_dt['Department_Item'].values
        send_dy1 = send_dy_p.tolist()
        send_dy = list(dict.fromkeys(send_dy1))

        "".join([str(_) for _ in send_dy])
        dt_t1 = pd.DataFrame(data=send_dy,columns=['Product'])
        send_dy_p = send_dt["Date"].values
        send_dy3 = send_dy_p.tolist()
        send_dy3 = list(dict.fromkeys(send_dy3))
        dt_t = pd.DataFrame(data=send_dy3,columns=['day'])
        import itertools
        import pprint
        t = send_dy
        r = send_dy3
        l_p = list(itertools.product(r,t))
        pprint.pprint(l_p)
        name = ["Date",'Department_Item']
        dt_b_t = pd.DataFrame(l_p,columns=name)
        return dt_b_t
    #Used intertool on the whole data
    
    #Create pandas with all combinations of department, item number, and date in pandas☛Department_set divided by department.
    dt_b_t = make_itertools_department(Department_set)
    
    #Date and Department_Item are concatenated into a string, and the one-dimensional pandas is df_new4.
    def make_str_df(dt_b_t,columns_1,columns_2,new_columns_name):
        make_pd_merge_Adjustment = dt_b_t
        make_pd_merge_Adjustment2 = (make_pd_merge_Adjustment[columns_1].astype(str))
        df_new3 = make_pd_merge_Adjustment[columns_2] + ',' + make_pd_merge_Adjustment2
        df_new4 = pd.DataFrame(data=df_new3,columns=[new_columns_name])
        return df_new4
    
    df_new4 = make_str_df(dt_b_t,'Department_Item','Date','day')

    #Divided by department in pandas☛Department_set
    #Create function to count daily SPD usage and return pandas
    def count_data_preparation(send_dt): 
        send_dt_t = send_dt.groupby(['Date', 'Department_Item']).count()
        send_dt_t1 =send_dt_t.drop(columns=['Standards_Capacities','goods' ])
        send_dt_t2=send_dt_t.drop(columns=['Standards_Capacities','goods' ])
        df_r_all = send_dt_t2.reset_index()
        name = ['Date','Department_Item']
        print("df_r_all",df_r_all)
        df_new = df_r_all.rename(columns={'Date': 'Date','Department_Item':'Department_Item',"claim":"count"})
        send_count1 = df_new["count"].values
        send_count = send_count1.T
        df_new2 = df_new.astype(str)
        df_new3 = df_new2['Date'] + ',' + df_new2['Department_Item']
        SPDs_used = pd.DataFrame(data=df_new3,columns=['day'])
        SPDs_used['count'] = send_count1
        return SPDs_used

    # Run function to count the number of SPD used daily in setting department and return pandas
    # columns of day concatenated with Date_Department_Item as string
    # count columns Columns that count how much Department_Item was used on that day.
    send_dt_count1 = count_data_preparation(Department_set)


    def data_preparation_marge(dt1,da1):
        #Combine_column_data
        dt_a = pd.merge(dt1, da1, on='day', how='outer')
        return dt_a

    marge_Product_count = data_preparation_marge(df_new4,send_dt_count1)


    # List the value of Department_Item for the setting department
    def make_send_dy_list(Department_set):
        send_dy_p = Department_set['Department_Item'].values
        send_dy1 = send_dy_p.tolist()
        #Information on 'Department_Item' goes into a list called send_dy
        #fromkeys(send_dy1) to remove all duplicate elements
        send_dy = list(dict.fromkeys(send_dy1))
        return send_dy
    
    send_dy = make_send_dy_list(Department_set)

    #Use string method to separate Date and Department_Item str.split(): split by delimiter
    def pd_split_marge1(dt1):
        df_r1 = dt1['day'].str.split(',', expand=True)
        df_r1.columns = ['day1', 'Department_Item']
        df_m_1 = df_r1
        df_m_2 = dt1
        df_m_3 = pd.concat([df_m_1, df_m_2], axis=1) 
        return df_m_3

    #Use the following string methods: str.split(): split by delimiter Execute function
    #multi-indexed and assumed to be multi-indexed
    # If not used once, use large_Product_count with num value
    # Make multi-index pandas of df_m_3 separated by Date and Department_Item Create
    df_m_3_r = pd_split_marge1(marge_Product_count)
    df_m_3 = df_m_3_r.set_index(['day1', 'Department_Item'])


    l=[]
    #Using a list called send_dy that contains 'Department_Item' information with duplicates removed
    #Count by df_m_3 multi-index, separating Date and Department_Item
    for i in send_dy:
        send2 = df_m_3.xs(str(i), level=1)
        send_2 = send2["count"].values
        send_dy1 = send_2.tolist()
        send_dy = list(send_dy1)
        l.append(send_dy)
    

    np.nan_to_num(l)
    l2 = np.nan_to_num(l)
    l3 = l2.T
    df_f = pd.DataFrame(l3)
    send_dy_p = Department_set["Date"].values
    send_dy3 = send_dy_p.tolist()
    send_day3 = list(dict.fromkeys(send_dy3))
    masuta2 = masuta_p_d_t
    

    def make_cound_product_code(Enter_the_product_code_1): 
        send2 = df_m_3.xs(str(Enter_the_product_code_1), level=1)
        send2_n = send2.fillna(0)
        Total = send2_n["count"].sum()
        df_r2 = masuta_send_m_3.set_index(['Department_Item','Date'])
        df_r2_12 = df_r2.xs(pd.IndexSlice[str(Enter_the_product_code_1)], level=0)
        send2_n_pp = send2_n.reset_index()
        send2_n_d=  send2_n_pp
        send2_nn = send2_n_d.reset_index()
        day_nn = send2_nn
        Show_first_element = day_nn.iat[0,1]
        last_day = len(day_nn)
        Show_last_element = day_nn.iat[int(last_day)-1,1]
        df_p = df_r2_12[['item_code', 'standard']]
        df = df_p 
        df['Number_of_times_total']=int(Total)
        df["Department"]=str(Department_name)
        df["Department_Item"]=str(Enter_the_product_code_1)
        return df

    #Leave only the ones that match the sent data and the master.
    ##multi-index of masuta_send_m_3 with multi-index set　
    ##Multi-index of df_m_3 separating Date and Department_Item
    masuta_send_pre = pd.merge(df_m_3,masuta_send_m_3,on="Department_Item")
    departmentcode1=masuta_send_pre['Department_Item'].drop_duplicates()
    departmentcode2=departmentcode1.reset_index()
    departmentcode3=departmentcode2['Department_Item']
    buppinn1 =masuta_send_pre['item_code'].drop_duplicates()
    buppinn2=buppinn1.reset_index()
    buppinn3=buppinn2['item_code']
    numberlis_pre = (len(departmentcode3))
    numbe = range(numberlis_pre)
    df_code = make_cound_product_code(departmentcode3[0])
    int_list=[]
    
    for i in numbe:
        df_code_Temporarily = make_cound_product_code(departmentcode3[i])
        df_code_Temporarily_T = df_code_Temporarily
        df_append_df = df_code_Temporarily_T
        int_list.append(df_append_df)
        df_code=df_code.append(df_code_Temporarily_T,ignore_index=True)
    
    df_code_o = df_code.drop_duplicates()
    len(departmentcode3.drop_duplicates())
    product_name = Department_name
    
    df_code_o.to_csv(Export_folder+str(product_name)+'.csv', encoding = 'shift-jis')

    send2 = df_m_3.xs(str(departmentcode3[0]), level=1)
    send2_p = send2.reset_index()
    send2_n = send2_p.fillna(0)
    send2_n["Department_Item"]=departmentcode3[0]
    send2_n["use_signature"]=Department_name
    send2_n1=send2_n.drop(columns='day')

    numberlis_pre = (len(departmentcode3))
    numbe = range(numberlis_pre)
    send2_nn_p = send2_n1
    send2_nn = send2_nn_p.drop(range(0,len(send2_nn_p)))

    int_list=[]
    
    for i in numbe:
        send2_Temporarilyp = df_m_3.xs(str(departmentcode3[i]), level=1)
        send2_Temporarily = send2_Temporarilyp.reset_index()
        df_append_df = send2_Temporarily.fillna(0)
        df_append_df["Department_Item"]=departmentcode3[i]
        send2_n.append(df_append_df)
        send2_nn=send2_nn.append(df_append_df,ignore_index=True)
        send2_nn["use_signature"]=Department_name
        send2_n1=send2_n.drop(columns='day')

    send2_nn1=send2_nn.drop(columns='day')
    product_name = Department_name
    df_code_send2_nd=send2_nn1.drop_duplicates()
    #save to excel
    df_code_send2_nd.to_csv(Export_folder+"send_data"+str(product_name)+'.csv', encoding = 'shift-jis')

if __name__ == '__main__':
    main()