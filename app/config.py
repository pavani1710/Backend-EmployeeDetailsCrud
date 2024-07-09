import os 

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('DATANASE_URL', 'postgresql://postgres:postgres@localhost/employee_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 