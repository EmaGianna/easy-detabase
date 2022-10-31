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


def bulk_insert_to_deta(csv_path_file, separator, deta_base):
    """
    It takes a csv file, reads it into a pandas dataframe, converts the dataframe to a dictionary, and
    then inserts each row of the dataframe into a deta table
    
    :param csv_path_file: the path to the csv file you want to insert into deta
    :param separator: the separator used in the csv file
    :param deta_base: the name of the deta base you want to insert into
    """
    df = pd.read_csv(csv_path_file, sep = separator)
    dict = df.to_dict()
    columns = df.columns
    dict_to_insert ={}
    counter = 0
    for index in range(len(df)):
        for key in columns:
            dict_to_insert[key] = dict[key][index] 
        deta_base.insert(dict_to_insert)
        counter = counter +1 
    print(f'{counter} records was inserted')


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
