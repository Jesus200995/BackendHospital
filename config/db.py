from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_VD6_sm2LUwoFm7Fmlw@test-utxicotepec-8d70.h.aivencloud.com:10780/defaultdb"

# Configuración SSL
ssl_args = {
    'ssl': {
        'ssl_ca': '/path/to/ca.pem',
        'ssl_cert': '/path/to/client-cert.pem',
        'ssl_key': '/path/to/client-key.pem'
    }
}

# Crear el motor con configuración SSL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=ssl_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

