#from deta import Deta
import pandas as pd


def deta_table_to_dataframe(deta_dict):
    """
    It takes a dictionary of dictionaries and returns a dataframe
    
    :param deta_dict: a dictionary of dictionaries, where each dictionary is a row of data
    :return: A dictionary with the data from the API
    """
    df  = pd.DataFrame()
    for item in deta_dict.items:
        df_aux = pd.DataFrame.from_dict(item, orient='index').transpose()
        df = pd.concat([df, df_aux])
    return df.reset_index(drop=True)


def bulk_insert_to_deta(df_aux, deta_base, chunksize=25):
    """
    It takes a dataframe, a deta base, and a chunk size, and inserts the dataframe into the deta base in
    chunks of the specified size
    
    :param df_aux: dataframe to insert
    :param deta_base: the name of the table you want to insert data into
    :param chunksize: The number of records to insert at a time, defaults to 25 (optional)
    """

    index_upper = 0
    counter_ok = 0
    counter_nok = 0
    dict_to_insert ={}
    for i in range(0,len(df_aux),chunksize):
        index_lower = i
        index_upper = index_upper + chunksize
        print(df_aux.iloc[index_lower:index_upper])
        df = df_aux.iloc[index_lower:index_upper]
        list_to_insert =[]
        df = df.reset_index(drop=True)
        dict = df.to_dict()
        columns = df.columns
        for index in range(df.shape[0]):
            for key in columns:
                dict_to_insert[key] = dict[key][index]
                dict_copy = dict_to_insert.copy()
            list_to_insert.append(dict_copy)
        try:
            deta_base.put_many(list_to_insert)
            counter_ok = counter_ok + len(list_to_insert)
        except Exception as e:
            counter_nok = counter_nok + len(list_to_insert)
            if (len(list_to_insert) <= 25):
                print(f' {e}\n Something was wrong with some record.\n Put value 1 to insert record and check the issue')
                print(' Suggestion: is good idea create output.log file if you try insert a lot of records;')
                print(' in that way you can find the error message on it and check.')
            else:
                print(e)
            continue
    print(f'Chunk step {chunksize}')
    print(f'{counter_ok} records was inserted')
    print(f'{counter_nok} records was no inserted')


def truncate_deta_table(deta_base):
    """
    It takes a deta base and deletes all the rows in the table
    
    :param deta_base: the name of the deta base
    """
    fetch_res = deta_base.fetch()
    df = deta_table_to_dataframe(fetch_res)
    counter = 0
    for index, row in df.iterrows():
        deta_base.delete(row['key'])
        counter = counter + 1
    print(f'{counter} rows was deleted')
