from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo1 = open("data/datos_clubs.txt","r")
archivo2 = open("data/datos_jugadores.txt", "r")

registros = archivo1.readlines();
registros2 = archivo2.readlines();

for r in registros:
        nombre = r.split(";")[0]
        deporte = r.split(";")[1] 
        fundacion = r.split(";")[2].replace("\n", "")
        Clubes = Club (nombre = nombre , deporte = deporte, fundacion=fundacion)
        session.add(Clubes)

for r in registros2:
        nombre = r.split(";")[3]
        dorsal = r.split(";")[2] 
        posicion = r.split(";")[1]
        cl = session.query(Club).filter_by(nombre = r.split(";")[0]).one()
        jugar = Jugador (nombre = nombre, dorsal = dorsal, posicion=posicion, club = cl)
        session.add(jugar)

session.commit()



