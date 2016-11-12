import sqlite3
import os

class DataBase():

    __slots__ = ('connect','cc','__queries')

    def __init__(self,path):
        self.__queries = {
            'SELECT': 'select {SELECT} from {FROM} where {WHERE}',
            'SELECT_ALL': 'select {SELECT} from {FROM}',
            'INSERT': 'insert into {INTO} values({VALUES})',
            'UPDATE': 'update {UPDATE} set {SET} where {WHERE}',
            'DELETE': 'delete from {FROM} where {WHERE}',
            'DELETE_ALL': 'delete from {FROM}',
            'CREATE_TABLE': 'create table if not exists {TABLE_NAME}({VALUES})',
            'DROP_TABLE': 'drop table {TABLE}',
            'CHECK_TABLE': 'select name from sqlite_master where type=\'table\' order by name'}
        self.connect= sqlite3.connect(database=os.path.normpath(str(path)))
        self.cc=self.connect.cursor()

    def __del__(self):
        self.connect.close()

    def __call__(self,queries,**arg):
        query = self.__queries[queries].format(**arg)
        self.cc.execute(query)
        self.connect.commit()
        return self.cc.fetchall()

    def create_table(self,**arg):
        return self(queries='CREATE_TABLE',**arg)
    def drop_table(self,**arg):
        return self(queries='DROP_TABLE',**arg)
    def delete_all(self,**arg):
        return self(queries='DELETE_ALL',**arg)
    def delete(self,**arg):
        return self(queries='DELETE',**arg)
    def update(self,**arg):
        return self(queries='UPDATE', **arg)
    def insert(self,**arg):
        return self(queries='INSERT',**arg)
    def select_all(self,**arg):
        return self(queries='SELECT_ALL', **arg)
    def select(self,**arg):
        return self(queries='SELECT', **arg)
    def check(self):
        return self(queries='CHECK_TABLE')