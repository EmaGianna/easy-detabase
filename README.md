# easydetabase

Easydetabase offer a simple way to interact with Deta Base Service.
This library was built on top of deta official library

## Functionalities

Currently easy-detabase have three operations/functions:

* ### bulk_insert_to_deta

    Function provide a way to insert records loaded in csv file, separated by [separator](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) in [deta base](https://www.deta.sh/) table

    #### Usage Mode:

    ```python
        from easydetabase import bulk_insert_to_deta
        from deta import Deta
        import pandas as pd 
        
        if __name__ == '__main__':
        
            deta = Deta("project key")
            db = deta.Base("sample_db")
            csv_path_file = './files/countries.csv'
            separator = ';'
            df_deta = pd.read_csv(csv_path_file, sep = separator)
            bulk_insert_to_deta(df_deta, db, 1)
    ```
    #### Output message:

    if insertion goes ok the message is:
    
    ```shell
            Chunk step 1
            245 records was inserted
    ```
    but if you have some issue on insertion process, message is 

     ```shell
            HTTP Error 400: Bad Request
            Something was wrong with some record.
            Put value 1 to insert record and check the issue
            Suggestion: is good idea create output.log file if you try insert a lot of records;
            in that way you can find the error message on it and check.
            Chunk step 1
            244 records was inserted
            1 records was no inserted
    ```

* ### deta_table_to_dataframe
 
    Function provide a way to read a [deta base](https://www.deta.sh/) table and return a pandas dataframe to work on it.

    #### Usage Mode

    ```python
        from easydetabase import deta_table_to_dataframe
        from deta import Deta
        
        if __name__ == '__main__':
        
            deta = Deta("project key")
            db = deta.Base("sample_db")
            fetch_res = db.fetch()
            df = deta_table_to_dataframe(fetch_res)
            print(df)
    ```
    #### Output message:

    You can see something this in terminal:

    ```shell
              country       fecha           key
        1          AU  2022-11-04  0cgr087icsk2
        3          DO  2022-11-04  0oymhwaqo7oa
        0          HM  2022-11-04  09upg9ncmite
        4          LK  2022-11-04  0r9lesxgf31p
        2          WF  2022-11-04  0j0l002gabpy
    ```

* ### truncate_deta_table

    Function provide a way to truncate a [deta base](https://www.deta.sh/) table.

    #### Usage Mode
    ```python
        from easydetabase import truncate_deta_table
        from deta import Deta

        if __name__ == '__main__':
        
            deta = Deta("project key")
            db = deta.Base("sample_db")
            truncate_deta_table(db)
    ```
    #### Output message:

    Out message must be like:

   ```shell
        244 rows was deleted
    ```