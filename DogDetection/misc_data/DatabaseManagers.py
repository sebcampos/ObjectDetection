from pymongo import MongoClient
from pymongo.database import Database
from credentials import CONNECTION_STRING
from pandas import DataFrame
import gridfs
import atexit


class MongoDBClient:
    mclient = MongoClient(CONNECTION_STRING)


    @classmethod
    def tear_down(cls) -> None:
        cls.mclient.close()
        print("Connection to Mongo db closed")

    @classmethod
    def update_table(cls, database: str, table: str, dataframe: DataFrame) -> None:
        """

        :param database:
        :param table:
        :param dataframe:
        :return:
        """
        cls.delete_table(database, table)
        cls.upload_dataframes(database, {table: dataframe})

    @staticmethod
    def get_dataframe(database, table, mclient=mclient) -> DataFrame:
        """
        This method returns a pandas dataframe of the requested database table
        :param: database string of the database name
        :param: table string of the table name
        :return: DataFrame 
        """
        cursor = mclient[database][table].find()
        return DataFrame(list(cursor))

    @staticmethod
    def database_names(mclient=mclient) -> list:
        """
        returns a list of database names
        for current connection
        """
        return mclient.list_database_names()

    @staticmethod
    def list_tables(database, mclient=mclient) -> list:
        """
        :param mclient:
        :param database: name of database
        :type database: str
        :return list of database collections
        """
        return mclient[database].list_collection_names()

    @staticmethod
    def create_db(database, mclient=mclient) -> Database:
        """
        :param mclient:
        :param database: name of the database
        :type database: str
        :return pymongo.database.Database
        """
        db = mclient[database]
        return db

    @staticmethod
    def delete_db(database, mclient=mclient) -> None:
        """
        :param mclient:
        :param database: database to drop_database
        :type database: str
        """
        mclient.drop_database(database)

    @staticmethod
    def delete_table(database, table, mclient=mclient) -> None:
        """
        :param mclient:
        :param database: name of database to drop table
        :type database: str
        :param table: name of table to drop
        :type table: str
        """
        mclient[database][table].drop()

    @staticmethod
    def delete_row(database, table, row) -> None:
        """
        :param database: name of db to drop from
        :type database: str
        :param table: name of table to drop from
        :type table: str
        :param row
        """
        pass

    @staticmethod
    def upload_dataframes(database: str, dataframes: dict, mclient=mclient) -> None:
        """
        This method updates a pandas DataFrame to the specified database with the given name
        :param mclient:
        :param database: string representation of the database name
        :param dataframes: dictionary holding a key of the table name and value being the dataframe
        :return: void
        """
        for name, df in dataframes.items():
            mclient[database][name].insert_many(df.to_dict("records"))

    @staticmethod
    def add_row(database, table, row, mclient=mclient) -> None:
        """
        :param mclient:
        :param database: database to add row too
        :type database: str
        :param table: table to add row to
        :type table: str
        :param row: row data to add
        :type row: dict
        """
        mclient[database][table].insert_one(row)
   
    @staticmethod
    def add_fs_file(database: str, binary, filename:str, mclient=mclient) -> None:
        fs = gridfs.GridFS(mclient[database])
        fs.put(binary, filename=filename)
        print(f"saved as [{filename}]")
    
    @staticmethod
    def retrieve_fs_file(database: str, filename: str, mclient=mclient) -> str:
    	fs = gridfs.GridFS(mclient[database])
    	return fs.get_last_version(filename).read()
    
    @staticmethod
    def delete_fs_file(database: str, uuid: str, mclient=mclient) -> None:
    	fs = gridfs.GridFS(mclient[database])
    	fs.delete(uuid)
   	

class SQLClient:
    pass


atexit.register(MongoDBClient.tear_down)
