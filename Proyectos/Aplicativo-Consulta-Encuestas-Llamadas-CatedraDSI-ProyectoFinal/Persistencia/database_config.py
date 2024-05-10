from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



import os, sys

this_file_path = os.path.dirname(__file__)
print(__file__)
sys.path.append(os.path.join(this_file_path, "../"))


# print(sys.path)




Base = declarative_base()
path = "Persistencia\ppai.db"


engine = create_engine("sqlite:///" + path, echo=True)
Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()




