# from sqlalchemy.orm import Session
from typing import List
from db.schemas import *
from db.database import database_conn_obj

# def get_fpids_index(db:Session, species, expression):
#     exp='%{e}%'.format(e=expression)
#     species=species.lower()
#     if species=='lmpd':
#         return db.query(models.Lmpd_Index).filter(models.Lmpd_Index.identifier.like(exp)).all()
#     elif species=='camelina':
#         return db.query(models.Camelina_Index).filter(models.Camelina_Index.identifier.like(exp)).all()
#     elif species=='soya':
#         return db.query(models.Soya_Index).filter(models.Soya_Index.identifier.like(exp)).all()

async def get_fpids_index(species: str, expression: str):
    expression=expression.lower()
    exp='%{e}%'.format(e=expression)
    species=species.lower()
    query1='select fatplant_id from '+species+'_index where identifier like \''+exp+'\';'
    res1= await database_conn_obj.fetch_all(query1)
    res=[i[0] for i in res1]
    row_headers=['identifier','fatplant_id','type']

    return res
async def get_species_records_identifier(species: str,fp_list: List[str]):
    species=species.lower()
    query1 = 'select * from '+species+'_identifier where fatplant_id in ({fpl})'
    fps = ["\"" + fp + "\"" for fp in fp_list]
    fps_list = ",".join(fps)
    query1 = query1.format(fpl=fps_list)
    res1= await database_conn_obj.fetch_all(query1)
    if species=='lmpd':
        row_headers=['fatplants_id','gene_names','protein_name','refseq_id','tair_id','uniprot_id']
    elif species=='camelina':
        row_headers=['fatplants_id','cs_id','protein_name','refseq_id','tair_id','uniprot_id']
    elif species=='soya':
        row_headers=['fatplants_id','gene_names','protein_name','refseq_id','glyma_id','uniprot_id']

    json_data = []
    for result in res1:
        json_data.append(dict(zip(row_headers, result)))

    return json_data




# def get_species_records_identifier(db:Session,species,expression,fp_list):
#     exp='%{e}%'.format(e=expression)
#     if species=='lmpd':
#         return db.query(models.Lmpd_Identifier).filter(models.Lmpd_Identifier.fatplant_id.in(fp_list)).all()
#     elif species=='camelina':
#         return db.query(models.Camelina_Identifier).filter(models.Camelina_Identifier.fatplant_id.in(fp_list)).all()
#     elif species=='soya':
#         return db.query(models.Soya_Identifier).filter(models.Soya_Identifier.fatplant_id.in(fp_list)).all()