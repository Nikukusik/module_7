from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://admin:admin@localhost/postgres"


engine = create_engine(DATABASE_URL, echo=True)


Session = sessionmaker(bind=engine, future=True)
Session = Session()
