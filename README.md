# easy-detabase

Easy-detabase offer a simple way to interact with Deta Base Service.
This library was built on top of deta official library

## Functionalities

Currently easy-detabase have three operations/functions:

* ### bulk_insert_to_deta

    Function provide a way to insert records loaded in csv file, separated by "[pandas separator](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)" in [deta base](https://www.deta.sh/) table   (*)

    #### Usage Mode:

    ```python
        from easy-detabase import bulk_insert_to_deta
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

* ### deta_table_to_dataframe
 
    Function provide a way to read a [deta base](https://www.deta.sh/) table and return a pandas dataframe to work on it.

    #### Usage Mode

    ```python
        from easy-detabase import deta_table_to_dataframe
        from deta import Deta
        
        if __name__ == '__main__':
        
            deta = Deta("project key")
            db = deta.Base("sample_db")
            fetch_res = db.fetch()
            df = deta_table_to_dataframe(fetch_res)
            print(df)
    ```

* ### truncate_deta_table

    Function provide a way to truncate a [deta base](https://www.deta.sh/) table.

    #### Usage Mode
    ```python
        from easy-detabase import truncate_deta_table
        from deta import Deta

        if __name__ == '__main__':
        
            deta = Deta("project key")
            db = deta.Base("sample_db")
            truncate_deta_table(db)
    ```

## Roadmap (Next improvements)



Inline-style: 
![pepe](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png)

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

