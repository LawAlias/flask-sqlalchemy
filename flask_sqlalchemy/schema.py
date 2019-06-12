#coding:utf-8
from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine
#创建schema
def CreateSchemaByName(engine,schema_name,call_back=None):
    """创建schema,schema_name:架构名，call_back：回调函数"""
    obj = CreateSchema(schema_name)
#     print(link)
#     engine = create_engine(link,encoding = 'utf-8')
    engine.execute(obj)
    if call_back:
        call_back()