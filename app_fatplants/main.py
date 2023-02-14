from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from db import models,database,schemas,crud
from db.database import database_conn_obj

# models.Base.metadata.create_all(bind=engine)  #Creating db session engine

app = FastAPI(
    title="FastAPI",
    description="Not Tested",
    version="1.0",
)

sleep_time = 10

@app.on_event("startup")
async def startup():
    await database_conn_obj.connect()

@app.on_event("shutdown")
async def shutdown():
    await database_conn_obj.disconnect()
# Dependency for db connection
# def get_db():
#     dbc = SessionLocal()
#     try:
#         yield dbc
#     finally:
#         dbc.close()

@app.get('/')
def index():
    print("Entering index func")
    return {'message':'Welcome to fatplants FastAPI Homepage. Please enter any valid endpoint'}

@app.get('/get_species_records/')
async def get_Species_Records(species: str,expression: str):
    fpid_list= await crud.get_fpids_index(species,expression)
    result= await crud.get_species_records_identifier(species,fpid_list)
    return result


