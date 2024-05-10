from Entidades.encuesta import Encuesta
from database_config import session

res = session.query(Encuesta).all()


# print(res)

for r in res:
    print(r)